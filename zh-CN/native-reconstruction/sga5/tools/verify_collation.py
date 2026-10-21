#!/usr/bin/env python3
"""Verify every integrated body change against the accepted exact patch ledger.

--record-from-git additionally captures the immutable pre-edit snapshot offsets.
Ordinary verification needs only files in the independently buildable ZIP.
"""
from pathlib import Path
from collections import defaultdict
import argparse, hashlib, json, re, subprocess

ROOT = Path(__file__).resolve().parents[1]
QA = ROOT/'qa/content-verification-20261021'
ap = argparse.ArgumentParser()
ap.add_argument('--record-from-git', action='store_true')
args=ap.parse_args()
ledger=json.loads((QA/'adjudication-ledger.json').read_text())
log=json.loads((QA/'applied-patches.json').read_text())
sha=lambda text:hashlib.sha256(text.encode()).hexdigest()
patches=defaultdict(list)
for item in ledger['items']:
    for p in item['patches']:
        if p['old']!=p['new']:
            patches[p['file']].append((item['id'],p))

if args.record_from_git:
    repo=ROOT.parents[2]
    prefix=ROOT.relative_to(repo).as_posix()+'/'
    for entry in log['files']:
        name=entry['file']
        old=subprocess.check_output(['git','show',ledger['frozen_translation_commit']+':'+prefix+name],cwd=repo).decode()
        assert sha(old)==entry['sha256_before'],name
        spans=[]
        for iid,p in patches[name]:
            matches=list(re.finditer(re.escape(p['old']),old))
            assert len(matches)==p['expected_occurrences'],(iid,name)
            for m in matches:
                spans.append({'id':iid,'old_start':m.start(),'old_end':m.end(),'old':p['old'],'new':p['new']})
        spans.sort(key=lambda p:p['old_start'])
        shift=0
        for p in spans:
            p['new_start']=p['old_start']+shift
            p['new_end']=p['new_start']+len(p['new'])
            shift+=len(p['new'])-len(p['old'])
        entry['replacements']=spans
    (QA/'applied-patches.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n')

rows=[]
for entry in log['files']:
    current=(ROOT/entry['file']).read_text()
    assert sha(current)==entry['sha256_after'],entry['file']
    restored=current
    for p in reversed(entry['replacements']):
        assert restored[p['new_start']:p['new_end']]==p['new'],(entry['file'],p['id'])
        restored=restored[:p['new_start']]+p['old']+restored[p['new_end']:]
    assert sha(restored)==entry['sha256_before'],entry['file']
    tags=lambda x:re.findall(r'\\(?:tag|label|ref|eqref|pageref)\{[^}]+\}',x)
    assert tags(current)==tags(restored),('numbered formula/reference token sequence changed',entry['file'])
    envs=lambda x:re.findall(r'\\(?:begin|end)\{[^}]+\}',x)
    assert envs(current)==envs(restored),('environment sequence changed',entry['file'])
    rows.append({'file':entry['file'],'sha256':sha(current),'restored_pre_edit_sha256':sha(restored),
        'exact_ledger_reversal':True,'numbered_tag_label_reference_sequence_preserved':True,
        'environment_sequence_preserved':True,'replacement_occurrences':len(entry['replacements'])})

notes=(ROOT/'chapters/09-collation-notes.tex').read_text()
for item in ledger['items']:
    assert notes.count('\\hypertarget{collation-'+item['id']+'}{}')==1,item['id']
    assert item['note_tex'] in notes,item['id']
for report in ledger['source_reports']:
    assert hashlib.sha256((ROOT/report['file']).read_bytes()).hexdigest()==report['sha256'],report['file']
result={'status':'PASS','method':'Every body edit reversed by frozen character offsets; exact pre-edit hashes recovered; all notes and report hashes verified.',
    'initial_issues':ledger['initial_recorded_issues'],'adjudicated_items':ledger['total_adjudicated_items'],
    'residual_source_uncertainty_ids':ledger['residual_source_uncertainty_ids'],
    'unrecorded_body_changes':0,'files':rows,'notes_sha256':sha(notes),
    'limits':'This verifies application fidelity, not a new independent proof of all source mathematics.'}
(QA/'application-verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
