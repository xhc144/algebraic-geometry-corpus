#!/usr/bin/env python3
"""Validate explicit review evidence; compilation never supplies review credit."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
SOURCE = REPO / 'en/KokunoYumeto-sga-en/release/08_SGA7I_EN_EXPOSES_I_II_VI_IX_READER.tex'
PATTERN = r'^% BEGIN INCLUDED ([^\n]+)\n(.*?)^% END INCLUDED \1[^\n]*'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def components(text):
    return {int(Path(m[1]).name.split('_')[0]): (Path(m[1]).name, m[0])
            for m in re.finditer(PATTERN, text, re.M | re.S)}


def main():
    ledger = json.loads((ROOT / 'qa/FIDELITY-R3-COVERAGE.json').read_text())
    source = components(SOURCE.read_text())
    assert set(source) == set(range(1, 188))
    targets = {}
    for path in sorted((ROOT / 'chapters').glob('*-zh.tex')):
        for number, item in components(path.read_text()).items():
            assert number not in targets
            targets[number] = item
    assert set(targets) == set(source)
    reports = {}
    for batch in ['VI-A', 'VI-B', 'VII', 'VIII', 'IX-A', 'IX-B']:
        path = ROOT / f'qa/FIDELITY-R3-{batch}.json'
        for item in json.loads(path.read_text())['components']:
            number = item['component']
            assert number not in reports and item['status'] == 'reviewed'
            assert item['content_checked'] and item['statement_or_proof_anchors']
            reports[number] = (item, path)
    prior = json.loads((ROOT / 'qa/FIDELITY-R2-SCOPE.json').read_text())
    prior_ids = {int(x['component'].split('_')[0])
                 for group in prior['scope'].values() for x in group}
    assert len(prior_ids) == 38 and len(reports) == 141
    assert not prior_ids.intersection(reports)
    assert set(range(1, 9)) | prior_ids | set(reports) == set(source)
    assert len(ledger['components']) == 187
    for row in ledger['components']:
        number = row['component']
        assert source[number][0] == row['name'] == targets[number][0]
        assert sha(source[number][1].encode()) == row['source_sha256']
        assert row['review_status'].startswith('independent_AI_bilingual_reviewed')
        if number in reports:
            item, path = reports[number]
            assert item['source_sha256'] == row['source_sha256']
            assert item['translation_component_sha256'] == row['baseline_translation_component_sha256']
            assert sha(path.read_bytes()) == row['evidence_sha256']
        else:
            assert (ROOT / row['evidence']).is_file()
        if 'final_translation_component_sha256' in row:
            assert row['final_translation_component_sha256'] == sha(targets[number][1].encode())
    result = {
        'status': 'evidence_validated', 'source_components': 187,
        'independent_AI_English_Chinese_component_reviews': 187,
        'inherited_I_II': 8, 'inherited_R2_VI_IX': 38, 'resumed_R3_complement': 141,
        'unreviewed_component_ids': [],
        'source_reader_sha256': sha(SOURCE.read_bytes()),
        'professional_human_certification': False,
        'full_original_French_collation': False,
        'all_original_mathematical_proofs_certified': False,
        'meaning': 'Every assigned component has explicit independent bilingual reading evidence. Named corrections and original uncertainties remain separate.'
    }
    (ROOT / 'qa/FIDELITY-R3-COVERAGE-VALIDATION.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
