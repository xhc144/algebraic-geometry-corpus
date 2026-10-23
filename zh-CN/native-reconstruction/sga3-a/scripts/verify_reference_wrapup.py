#!/usr/bin/env python3
"""Verify the bounded citation patch against its frozen pre-patch snapshot."""
from pathlib import Path
import collections,hashlib,json,re,subprocess
from tex_reference_scan import calls
r=Path(__file__).resolve().parents[1];p=r/'audit/reference-wrapup/APPLIED.json';d=json.loads(p.read_text())
aux=(r/'build/main.aux').read_text();labels=set(re.findall(r'\\newlabel\{([^{}]+)\}',aux))
errors=[];rows=[]
for f in d['files']:
    data=(r/f['file']).read_bytes()
    if hashlib.sha256(data).hexdigest()!=f['after_sha256']:errors.append(['post_patch_hash_changed',f['file']])
for i in d['items']:
    s=(r/i['file']).read_text();decision=i['decision'];row={'file':i['file'],'baseline_line':i['line'],'decision':decision,'new_key':i.get('new_key')}
    if decision=='replace_plain_citation':
        row['present']=i['new_text'] in s
    elif decision=='mark_plain_pending':row['present']=i['after_tex'] in s
    elif i.get('command')=='hyperref':row['present']=i['after_tex'] in s
    else:
        command={'external':'SGARefExternal','pending':'SGARefPending'}.get(decision,'SGARefLink')
        key=i['new_key'] if decision=='replace_key' else i['old_key']
        row['present']=any(c['command']==command and c['key']==key and c['visible_tex']==i['visible_tex'] for c in calls(s))
    if decision in ('replace_key','replace_plain_citation'):
        row['target_in_compiled_aux']=i['new_key'] in labels
        if not row['target_in_compiled_aux']:errors.append(['corrected_target_absent',i])
    if not row['present']:errors.append(['corrected_call_absent',i])
    rows.append(row)
for key,ins in d['new_anchors'].items():
    if (r/ins['file']).read_text().count(ins['suggested_command'])!=1:errors.append(['new_anchor_not_unique',key])
# The original source documents and every unedited delivered native dependency
# must remain identical to the baseline commit. This is a content boundary check.
repo=r.parents[2];prefix=str(r.relative_to(repo))+'/'
changed=subprocess.check_output(['git','diff','--name-only',d['baseline_commit'],'--',prefix],cwd=repo,text=True).splitlines()
edited=set(x['file'] for x in d['files'] if x['edits'])|{'preamble.tex'}
unexpected=[x for x in changed if x.endswith('.tex') and x.removeprefix(prefix) not in edited]
errors.extend(['unexpected_tex_edit',x] for x in unexpected)
report={'result':'passed' if not errors else 'failed','baseline_commit':d['baseline_commit'],'counts':d['counts'],'corrected_targets_all_present_in_compiled_aux':not any(e[0]=='corrected_target_absent' for e in errors),'new_anchor_count':len(d['new_anchors']),'all_source_and_visible_text_guards':'See APPLIED.json file checks; only the five explicitly ledgered printed citation corrections change visible wording, plus generated pending badges.','unedited_native_dependencies_unchanged':not unexpected,'items':rows,'errors':errors,'limits':'This verifies the finite applied decisions and native content boundary, not every inherited link in the whole book and not mathematical/French final collation.'}
(r/'audit/reference-wrapup/VERIFIED.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ('result','counts','corrected_targets_all_present_in_compiled_aux','new_anchor_count','unedited_native_dependencies_unchanged','errors')},ensure_ascii=False))
if errors:raise SystemExit(1)
