#!/usr/bin/env python3
"""Mechanical source/translation audit; not a proof of linguistic completeness."""
from pathlib import Path
import argparse
import collections
import difflib
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]

def digest(b):
    return hashlib.sha256(b).hexdigest()

def uncomment(s):
    return re.sub(r'(?m)(?<!\\)%.*$', '', s)

def signature(s):
    s = uncomment(s)
    patterns = {
        'semantic_labels': r'\\etiquette\[[^\]]*\]\{([^}]*)\}',
        'ordinary_labels': r'\\label\{([^}]*)\}',
        'hyperref_targets': r'\\hyperref\[([^\]]*)\]',
        'hyperlink_targets': r'\\hyperlink\{([^}]*)\}',
        'hypertargets': r'\\hypertarget\{([^}]*)\}',
        'environments_begin': r'\\begin\{([^}]*)\}',
        'environments_end': r'\\end\{([^}]*)\}',
        'bibliography_keys': r'\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}',
        'citation_keys': r'\\cite(?:\[[^\]]*\])?\{([^}]*)\}',
        'equation_tags': r'\\tag\{([^}]*)\}',
    }
    out = {k: re.findall(p, s) for k, p in patterns.items()}
    out['original_page_markers'] = len(re.findall(r'\\pageoriginale(?:d)?\b', s))
    out['xymatrix_count'] = len(re.findall(r'\\xymatrix\b', s))
    out['heading_command_counts'] = dict(collections.Counter(re.findall(r'\\(section|subsection|subsubsection|paragraph)\*?\{', s)))
    out['footnote_command_counts'] = dict(collections.Counter(re.findall(r'\\(footnote|footnotemark|footnotetext|nde|ndemark|ndetext)\b', s)))
    return out

def math(s):
    # Delimited math only. Xy-pic macros and undelimited math remain separate
    # checks; all changed spans are review candidates, never auto-certified.
    s = uncomment(s)
    p = r'(?s)(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$(?!\$).*?(?<!\\)\$|(?<!\\)\\\[.*?(?<!\\)\\\]|(?<!\\)\\\(.*?(?<!\\)\\\)'
    return [re.sub(r'\s+', '', x) for x in re.findall(p, s)]

def compare(source, target):
    a, b = signature(source), signature(target)
    differences = {k: {'source': a[k], 'translation': b[k]} for k in a if (collections.Counter(a[k]) != collections.Counter(b[k]) if isinstance(a[k], list) else a[k] != b[k])}
    am, bm = math(source), math(target)
    changed = []
    for op, i, j, k, l in difflib.SequenceMatcher(a=am, b=bm, autojunk=False).get_opcodes():
        if op != 'equal':
            changed.append({'operation': op, 'source_indices': [i, j], 'translation_indices': [k, l],
                            'source': am[i:j], 'translation': bm[k:l]})
    return {'source_signature': a, 'translation_signature': b,
            'structural_differences': differences,
            'delimited_math_counts': [len(am), len(bm)],
            'math_multiset_missing': list((collections.Counter(am)-collections.Counter(bm)).elements()),
            'math_multiset_added': list((collections.Counter(bm)-collections.Counter(am)).elements()),
            'math_review_spans': changed}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--archive', type=Path, default=REPO / 'en/KokunoYumeto-sga-en/release/00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip')
    args = p.parse_args()
    audit = json.loads((ROOT / 'audit/SOURCE_AUDIT.json').read_text())
    assert digest(args.archive.read_bytes()) == audit['archive_sha256']
    z = zipfile.ZipFile(args.archive)
    source = z.read(audit['chosen_member']).decode().replace('\r\n', '\n')
    prefix = 'SGA4_English_current_buildable_source_20260906/source/'
    start = source.index('% BEGIN INCLUDED ' + prefix + '01/01_English.tex')
    end = source.index('% BEGIN INCLUDED ' + prefix + '02/02_English.tex')
    flat = source[start:end].splitlines(True)
    chunks = json.loads((ROOT / 'audit/CHUNK_MAP.json').read_text())['chunks']
    result = {'status': 'mechanical_audit_only', 'source_archive_verified': True,
              'linguistic_completeness_certified': False, 'chunks': []}
    for c in chunks:
        a, b = c['source_flat_lines_inclusive']
        src = ''.join(flat[a-1:b])
        assert digest(src.encode()) == c['source_normalized_sha256']
        target = ROOT / c['output']
        row = dict(c)
        if target.exists():
            out = target.read_text()
            row.update({'output_sha256': digest(target.read_bytes()),
                        'output_lines': len(out.splitlines()), **compare(src, out)})
        else:
            row['status'] = 'not_written'
        result['chunks'].append(row)
    (ROOT / 'audit/MECHANICAL_AUDIT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    for row in result['chunks']:
        print(row['output'], 'structure differences:', list(row.get('structural_differences', {})),
              'math review spans:', len(row.get('math_review_spans', [])))

if __name__ == '__main__':
    main()
