#!/usr/bin/env python3
"""Apply explicitly selected, human-reviewed French-collation patches.

Every patch must match once. Only chapter files in this output directory may
change. Journal stores exact before/after text and primary-source evidence.
"""
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOURNAL = ROOT / 'audit/review-20261022/APPLIED.json'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('report', type=Path)
    p.add_argument('--indices', required=True, help='Comma-separated zero-based indices approved by editor')
    args = p.parse_args()
    report = args.report.resolve()
    data = json.loads(report.read_text())
    patches = data if isinstance(data, list) else data['patches']
    journal = json.loads(JOURNAL.read_text()) if JOURNAL.exists() else []
    for index in map(int, args.indices.split(',')):
        item = patches[index]
        identity = hashlib.sha256((item['file'] + '\0' + item['old'] + '\0' + item['new']).encode()).hexdigest()
        if any(row['identity'] == identity for row in journal):
            print('Already applied:', item['file'], index)
            continue
        path = ((ROOT.parents[2] if item['file'].startswith('zh-CN/') else ROOT) / item['file']).resolve()
        assert path.is_relative_to(ROOT / 'chapters') and path.suffix == '.tex', path
        text = path.read_text()
        expected = item.get('old_occurrences', 1)
        assert text.count(item['old']) == expected, (path, text.count(item['old']), expected)
        relative_report = str(report.relative_to(ROOT))
        output = text.replace(item['old'], item['new'], expected)
        entry = dict(item, identity=identity, report=relative_report, index=index,
                     output_sha256=hashlib.sha256(output.encode()).hexdigest())
        path.write_text(output)
        journal.append(entry)
        JOURNAL.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + '\n')
        print('Applied:', item['file'], index, item.get('id', ''))


if __name__ == '__main__':
    main()
