#!/usr/bin/env python3
"""Reproduce source/body coverage and flag math differences for editorial review.

Does not certify translation quality, source correctness or arbitrary TeX expansion.
The source archive is intentionally not copied into the translation source ZIP.
"""
from pathlib import Path
import argparse
from collections import Counter
import hashlib
import json
import zipfile

from check_sources import compare, digest

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--archive', type=Path, default=REPO / 'en/KokunoYumeto-sga-en/release/00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip')
    args = parser.parse_args()
    pin = json.loads((ROOT / 'audit/SOURCE_AUDIT.json').read_text())
    assert digest(args.archive.read_bytes()) == pin['archive_sha256']
    with zipfile.ZipFile(args.archive) as archive:
        raw = archive.read(pin['chosen_member'])
    assert digest(raw) == pin['chosen_member_sha256']
    lines = raw.decode().replace('\r\n', '\n').splitlines(True)
    mapping = json.loads((ROOT / 'audit/FULL_CHUNK_MAP.json').read_text())
    result = {'status': 'complete_assigned_body_coverage_mechanical_review',
              'source_archive_sha256': pin['archive_sha256'],
              'translation_quality_certified': False,
              'all_original_mathematics_independently_proofread': False,
              'source_defects': 'See chapter review files and REFERENCE_AUDIT.md; no blanket mathematical correction.',
              'chunks': []}
    for item in mapping['chunks']:
        a, b = item['reader_lines_inclusive']
        source = ''.join(lines[a - 1:b])
        assert digest(source.encode()) == item['source_normalized_sha256'], item
        path = ROOT / item['output']
        target = path.read_text()
        check = compare(source, target)
        # Full signature sequences are hashed and counted here; detailed changed
        # spans remain visible rather than a misleading binary "math passed".
        for key in ['source_signature', 'translation_signature']:
            sig = check[key]
            check[key] = {k: ({'count': len(v), 'sequence_sha256': digest(json.dumps(v, ensure_ascii=False).encode())}
                             if isinstance(v, list) else v) for k, v in sig.items()}
        result['chunks'].append(dict(item, output_sha256=digest(path.read_bytes()),
                                    output_lines=len(target.splitlines()), **check))
    (ROOT / 'audit/FULL_MECHANICAL_AUDIT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    for row in result['chunks']:
        print(row['output'], 'source/target math', row['delimited_math_counts'],
              'structure flags', list(row['structural_differences']),
              'math review spans', len(row['math_review_spans']))


if __name__ == '__main__':
    main()
