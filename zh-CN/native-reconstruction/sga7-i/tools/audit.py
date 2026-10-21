#!/usr/bin/env python3
"""Audit completed native translation components against the locked reader.

This is a structural comparison, not a semantic or mathematical proofreader.
It never treats successful compilation as proof of complete translation.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
SOURCE = REPO / 'en/KokunoYumeto-sga-en/release/08_SGA7I_EN_EXPOSES_I_II_VI_IX_READER.tex'


def write_json(name, value):
    (ROOT / 'qa' / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def components(text):
    pattern = r'^% BEGIN INCLUDED ([^\n]+)\n(.*?)^% END INCLUDED \1[^\n]*'
    return {Path(m.group(1)).name: m.group(0) for m in re.finditer(pattern, text, re.M | re.S)}


def uncomment(text):
    return '\n'.join(re.split(r'(?<!\\)%', line)[0] for line in text.splitlines())


def formulas(text):
    # The source reader uses dollar inline math and backslash-bracket displays.
    # Include equation/aligned environments and TikZ displays in the comparison.
    text = uncomment(text)
    pattern = (r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|'
               r'(?<!\\)\$(?!\$).*?(?<!\\)\$|'
               r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}')
    return [m.group(0) for m in re.finditer(pattern, text, re.S)]


def normalized(formula):
    # Translation of textual math annotations is permitted. Do not remove
    # symbols, indices, numbers, tags, operators, or target identifiers.
    # Eight flat labels and one surjective label in VI are localized as text.
    # They are text on arrows, not operator or variable changes.
    formula = formula.replace(r'\mathrm{flat}', '').replace(r'\mathrm{surjective}', '')
    for match in reversed(list(re.finditer(r'\\(?:text|textrm|textnormal|mbox|hbox)\{', formula))):
        depth, end = 1, match.end()
        while end < len(formula) and depth:
            if formula[end] == '{' and (end == 0 or formula[end-1] != '\\'):
                depth += 1
            elif formula[end] == '}' and (end == 0 or formula[end-1] != '\\'):
                depth -= 1
            end += 1
        if depth == 0:
            formula = formula[:match.start()] + formula[end:]
    return re.sub(r'\s+', '', formula)


def summary_difference(left, right):
    return [{'formula': s, 'count': n} for s, n in (Counter(left) - Counter(right)).items()]


def source_expose(name):
    return re.search(r'_expose_(I|II|VI|VII|VIII|IX)_', name).group(1)


def main():
    source_text = SOURCE.read_text()
    locked = json.loads((ROOT / 'SOURCE_LOCK.json').read_text())['sources'][0]['sha256']
    assert hashlib.sha256(SOURCE.read_bytes()).hexdigest() == locked, 'Locked source changed'
    source = components(source_text)
    chapters = sorted((ROOT / 'chapters').glob('*-zh.tex'))
    targets, duplicates = {}, []
    for chapter in chapters:
        for name, text in components(chapter.read_text()).items():
            if name in targets:
                duplicates.append(name)
            targets[name] = (chapter.relative_to(ROOT).as_posix(), text)

    # Work-in-progress files can still contain an English tail. Explicit
    # translator checkpoints, not mere component markers, govern coverage.
    approved = set()
    statuses = {}
    for path in sorted((ROOT / 'chapters').glob('*-status.json')):
        status = json.loads(path.read_text())
        statuses[path.name] = status
        filename = path.name.replace('-status.json', '-zh.tex')
        names = [name for name, (f, _) in targets.items() if Path(f).name == filename]
        state = str(status.get('status', status.get('translation_status', ''))).lower()
        if ('complete' in state and 'incomplete' not in state and 'partial' not in state):
            approved.update(names)
            continue
        ids = status.get('completed_components', status.get('components_complete', []))
        boundary = status.get('last_complete_component')
        if isinstance(boundary, str):
            found = re.search(r'(\d+)_expose_', boundary)
            boundary = int(found.group(1)) if found else None
        for name in names:
            number = int(name.split('_')[0])
            if number in ids or isinstance(boundary, int) and number <= boundary:
                approved.add(name)

    audits = []
    refs_available = set()
    refs_used = Counter()
    for name, original in source.items():
        if name not in approved:
            continue
        filename, translated = targets[name]
        original_math = formulas(original)
        target_math = formulas(translated)
        # IX3.9's long chain is split ONLY at two invisible break opportunities.
        # Preserve and report the raw block count as well as the logical count.
        canonical_target = re.sub(r'(?<!\\)\$\\allowbreak\s*\$(?!\$)', '', translated)
        target_logical_math = formulas(canonical_target)
        named_repairs = []
        checked_original = original
        if name.startswith('69_') and 'G,qquad' in checked_original:
            named_repairs.append({'source': 'G,qquad', 'translation': r'G,\qquad', 'count': checked_original.count('G,qquad'), 'evidence': 'chapters/expose-VII-status.json'})
            checked_original = checked_original.replace('G,qquad', r'G,\qquad')
        bad_exponent = r'\underline m^{,n+1}'
        if bad_exponent in checked_original:
            named_repairs.append({'source': bad_exponent, 'translation': r'\underline m^{n+1}', 'evidence': 'Original scan PDF521/printed516; chapters/expose-IX-d-status.json'})
            checked_original = checked_original.replace(bad_exponent, r'\underline m^{n+1}')
        layout_repairs = []
        if 'column sep=0.8em' in canonical_target:
            layout_repairs.append({'source': 'column sep=small', 'translation': 'column sep=0.8em', 'reason': '5.07216pt diagram overflow; symbols/arrows unchanged'})
            canonical_target = canonical_target.replace('column sep=0.8em', 'column sep=small')
        if name.startswith('97_'):
            checked_original = checked_original.replace(r'\footnotesize', '')
            layout_repairs.append({'source': r'\footnotesize in display math', 'translation': 'ignored switch removed', 'reason': 'Invalid-in-math warning; switch had no effect'})
        # Named syntax repair in VII is reported separately, not hidden in a
        # universal normalizer.
        normalized_original = [normalized(f) for f in formulas(checked_original)]
        normalized_target = [normalized(f) for f in formulas(canonical_target)]
        refs_available.update(re.findall(r'\\SGARef(?:Alias)?Target\{([^}]+)\}', translated))
        refs_used.update(re.findall(r'\\SGARefLink\{([^}]+)\}', translated))
        audits.append({
            'component': name, 'translation_file': filename,
            'source_formula_count': len(original_math), 'translation_formula_count': len(target_math),
            'translation_logical_formula_count': len(target_logical_math),
            'named_source_repairs': named_repairs, 'named_layout_repairs': layout_repairs,
            'inline_fragment_rejoining_count': len(target_math) - len(target_logical_math),
            'formula_multiset_equal_after_text_localization': Counter(normalized_original) == Counter(normalized_target),
            'unmatched_source_formulas': summary_difference(normalized_original, normalized_target),
            'unmatched_translation_formulas': summary_difference(normalized_target, normalized_original),
            'source_targets': re.findall(r'\\SGARef(?:Alias)?Target\{([^}]+)\}', original),
            'translation_targets': re.findall(r'\\SGARef(?:Alias)?Target\{([^}]+)\}', translated),
            'references_same_multiset': Counter(re.findall(r'\\SGARefLink\{([^}]+)\}', original)) == Counter(re.findall(r'\\SGA(?:RefLink|ExternalRef)\{([^}]+)\}', translated)),
            'environments_same_order': re.findall(r'\\begin\{([^}]+)\}', original) == re.findall(r'\\begin\{([^}]+)\}', translated),
            'translation_sha256': hashlib.sha256(translated.encode()).hexdigest(),
        })
    counts = {}
    for expose in ['I', 'II', 'VI', 'VII', 'VIII', 'IX']:
        expected = [n for n in source if source_expose(n) == expose]
        done = [n for n in expected if n in approved]
        counts[expose] = {'source_components': len(expected), 'translated_components': len(done),
                          'translation_complete': len(done) == len(expected),
                          'unfinished_components': [n for n in expected if n not in approved]}
    all_targets = set(re.findall(r'\\SGARef(?:Alias)?Target\{([^}]+)\}', source_text))
    coverage = {'status': 'translation_draft_complete' if len(approved) == len(source) else 'partial',
                'source_component_count': len(source), 'translated_component_count': len(approved),
                'exposes': counts, 'duplicate_components': duplicates,
                'not_a_semantic_review': True}
    write_json('coverage.json', coverage)
    write_json('formula-audit.json', audits)
    write_json('cross-references.json', {
        'available_target_count': len(refs_available),
        'references_to_untranslated_components': sorted(t for t in refs_used if t not in refs_available and t in all_targets),
        'targets_absent_even_from_complete_reader': sorted(t for t in refs_used if t not in all_targets),
        'policy': 'Only available targets are linked. Missing and external citations remain printed and are inventoried here.'})
    included_files = set(re.findall(r'\\input\{(chapters/[^}]+)\}', (ROOT / 'main.tex').read_text()))
    compiled_targets = set()
    for filename in included_files:
        compiled_targets.update(re.findall(r'\\SGARef(?:Alias)?Target\{([^}]+)\}', (ROOT / filename).read_text()))
    available = '\n'.join('\\expandafter\\def\\csname SGAavailable@' + target + '\\endcsname{}'
                          for target in sorted(compiled_targets)) + '\n'
    (ROOT / 'available-targets.tex').write_text(available)
    print(json.dumps({'coverage': coverage['status'], 'translated_components': len(approved),
                      'source_components': len(source), 'formula_difference_components':
                      [a['component'] for a in audits if not a['formula_multiset_equal_after_text_localization']]}, ensure_ascii=False))


if __name__ == '__main__':
    main()
