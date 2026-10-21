#!/usr/bin/env python3
"""Apply the reviewed collation ledger, with exact-count and overlap checks.

All replacements are located against one frozen snapshot, so swapping two
symbols cannot accidentally replace a symbol introduced by an earlier edit.
Default is a dry run.  The ledger retains original readings; originals outside
this reconstruction directory are never opened for writing.
"""
from pathlib import Path
from collections import defaultdict
import argparse, hashlib, json, re

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT / 'qa/content-verification-20261021'
ap = argparse.ArgumentParser()
ap.add_argument('--apply', action='store_true')
args = ap.parse_args()
ledger = json.loads((QA / 'adjudication-ledger.json').read_text())
byfile = defaultdict(list)
for item in ledger['items']:
    for patch in item['patches']:
        if patch.get('apply', True) and patch['old'] != patch['new']:
            byfile[patch['file']].append((item['id'], patch))

results = []
pending = {}
for name, patches in byfile.items():
    path = ROOT / name
    assert path.resolve().is_relative_to(ROOT), name
    assert name.startswith('chapters/'), name
    before = path.read_text()
    spans = []
    for item_id, patch in patches:
        found = list(re.finditer(re.escape(patch['old']), before))
        assert len(found) == patch['expected_occurrences'], (item_id, name, len(found), patch['expected_occurrences'], patch['old'])
        for match in found:
            spans.append((match.start(), match.end(), patch['new'], item_id))
    spans.sort()
    for left, right in zip(spans, spans[1:]):
        assert left[1] <= right[0], ('overlapping patches', name, left[3], right[3])
    after = before
    for start, end, replacement, _ in reversed(spans):
        after = after[:start] + replacement + after[end:]
    pending[path] = after
    results.append({
        'file': name,
        'sha256_before': hashlib.sha256(before.encode()).hexdigest(),
        'sha256_after': hashlib.sha256(after.encode()).hexdigest(),
        'replacement_occurrences': len(spans),
        'ids': sorted(set(item_id for item_id, _ in patches)),
    })

if args.apply:
    # All files are validated before any file is changed.
    for path, text in pending.items():
        path.write_text(text)
    (QA / 'applied-patches.json').write_text(json.dumps({
        'status': 'applied', 'method': 'simultaneous exact snapshot replacements',
        'ledger_sha256': hashlib.sha256((QA / 'adjudication-ledger.json').read_bytes()).hexdigest(),
        'files': results,
    }, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'applied': args.apply, 'files': results}, ensure_ascii=False, indent=2))
