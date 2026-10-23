#!/usr/bin/env python3
"""Apply the frozen, occurrence-specific bounded citation decisions once.

Refuses changed inputs; never globally substitutes a repeated reference key.
The ledger records every retained, repaired, external and pending occurrence.
"""
from pathlib import Path
from collections import Counter,defaultdict
import argparse,hashlib,json,re,subprocess
from tex_reference_scan import calls,visible_only,hyperref_visible_only
r=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('--from-baseline',action='store_true',help='Reconcile final decisions only if every prior output still matches its recorded hash.');args=p.parse_args()
baseline='ea116c5f61fcfa9c499922abdb7be5622c71bfb3';repo=r.parents[2];prefix=str(r.relative_to(repo))+'/'
prior=json.loads((r/'audit/reference-wrapup/APPLIED.json').read_text()) if args.from_baseline else None
prior_hashes={x['file']:x['after_sha256'] for x in prior['files']} if prior else {}
def source(file):
    if not args.from_baseline:return (r/file).read_text()
    current=hashlib.sha256((r/file).read_bytes()).hexdigest()
    assert current==prior_hashes[file],('prior checkpoint changed',file)
    return subprocess.check_output(['git','show',baseline+':'+prefix+file],cwd=repo).decode()
out=r/'audit/reference-wrapup';items=[]
for name in ('I-VI-decisions.json','VII-decisions.json','VIII-XI-decisions.json'):
    d=json.loads((out/name).read_text())
    items.extend(d['items'])
    items.extend(d.get('non_sga_ref_calls',[]))
    for i in d.get('reported_reference_without_link',[]):
        i=dict(i)
        if i['decision']=='pending':i['decision']='mark_plain_pending'
        items.append(i)
byfile=defaultdict(list)
for i in items:byfile[i['file']].append(i)
edits=defaultdict(list);originals={};anchors={};ledger=[]
def edit(file,start,end,new,why):edits[file].append((start,end,new,why))
for file,rows in byfile.items():
    s=source(file);originals[file]=s;digest=hashlib.sha256(s.encode()).hexdigest()
    allcalls=list(calls(s));lines=s.splitlines(keepends=True)
    for row in rows:
        i=dict(row)
        if i.get('file_sha256'):assert i['file_sha256']==digest,(file,'changed input')
        decision=i['decision'];i['baseline_sha256']=digest
        if decision in ('replace_plain_citation','mark_plain_pending'):
            old=i.get('old_text',i.get('text'))
            matches=[m.start() for m in re.finditer(re.escape(old),s) if s.count('\n',0,m.start())+1==i['line']]
            assert len(matches)==1,(file,old,i['line']);p=matches[0]
            new=i['new_text'] if decision=='replace_plain_citation' else '\\SGARefPending{}{'+old+'}'
            edit(file,p,p+len(old),new,decision)
            i['before_tex']=old;i['after_tex']=new;ledger.append(i);continue
        if i.get('command')=='hyperref':
            old=i['call_tex'];positions=[m.start() for m in re.finditer(re.escape(old),s)]
            ps=[p for p in positions if s.count('\n',0,p)+1==i['line']];assert len(ps)==1,(file,i)
            p=ps[0]
            if decision=='replace_key':new=old.replace('['+i['old_key']+']','['+i['new_key']+']',1)
            elif decision=='pending':new='\\SGARefPending{'+i['old_key']+'}{'+i['visible_tex']+'}'
            else:raise ValueError(i)
            edit(file,p,p+len(old),new,decision)
            i['before_tex']=old;i['after_tex']=new;ledger.append(i);continue
        matches=[c for c in allcalls if c['line']==i['line'] and c['key']==i['old_key'] and c['visible_tex']==i['visible_tex']]
        if len(matches)!=1:
            same=[c for c in allcalls if c['macro_tex']==i['call_tex']]
            c=same[i['identical_call_occurrence_in_file']-1]
            assert c in matches,(file,i)
        else:c=matches[0]
        i['before_tex']=c['macro_tex'];i['baseline_offset']=c['start']
        if decision=='replace_key':
            edit(file,c['key_start'],c['key_end'],i['new_key'],decision)
            i['after_tex']=c['macro_tex'].replace('{'+i['old_key']+'}','{'+i['new_key']+'}',1)
        elif decision in ('pending','external'):
            command='SGARefPending' if decision=='pending' else 'SGARefExternal'
            edit(file,c['start']+1,c['command_end'],command,decision)
            i['after_tex']=c['macro_tex'].replace('\\SGARefLink','\\'+command,1)
        elif decision=='retain':i['after_tex']=i['before_tex']
        else:raise ValueError(i)
        ins=i.get('insert_target')
        if ins:
            ins=dict(ins)
            if i.get('target_line_after_insertion'):
                target_line=i['target_line_after_insertion'];marker=ins['suggested_command']
                assert target_line.replace(marker,'')==ins['exact_existing_line'],(i,target_line)
                ins['insertion_column']=target_line.index(marker)
            key=i['new_key'];existing=anchors.get(key)
            if existing:assert existing==ins,(key,existing,ins)
            anchors[key]=ins
        ledger.append(i)
for key,ins in anchors.items():
    file=ins['file'];s=originals.get(file)
    if s is None:s=source(file)
    originals[file]=s
    lines=s.splitlines(keepends=True);line=ins['before_line'];text=lines[line-1].rstrip('\n')
    assert text==ins['exact_existing_line'],(key,text,ins)
    pos=sum(map(len,lines[:line-1]))
    # Put the anchor inside the optional item label, at its visible numeral.
    marker=ins['suggested_command']
    assert re.fullmatch(r'\\SGAInline(?:Ref|Equation)Target\{'+re.escape(key)+r'\}',marker),ins
    if 'insertion_column' in ins:pos+=ins['insertion_column']
    elif re.match(r'\s*\\item\[',text):pos+=re.match(r'\s*\\item\[',text).end()
    edit(file,pos,pos,marker,'insert_target')
checks=[];outputs={}
for file,s in originals.items():
    pending=sorted(edits[file],key=lambda e:(e[0],e[1]))
    for a,b in zip(pending,pending[1:]):assert a[1]<=b[0],('overlapping edits',file,a,b)
    t=s
    for start,end,new,why in reversed(pending):t=t[:start]+new+t[end:]
    expected=s
    for start,end,new,why in reversed(pending):
        if why=='replace_plain_citation':expected=expected[:start]+new+expected[end:]
    before=hyperref_visible_only(visible_only(expected));after=hyperref_visible_only(visible_only(t))
    for key,ins in anchors.items():
        if ins['file']==file:after=after.replace(ins['suggested_command'],'')
    # Explicit, source/context-confirmed printed citation corrections are the only
    # visible-word changes; pending badges are macro-generated and disclosed.
    if before!=after:
        import difflib
        raise AssertionError(('visible content changed unexpectedly',file,list(difflib.unified_diff(before.splitlines(),after.splitlines()))[:20]))
    if pending:outputs[file]=t
    checks.append({'file':file,'before_sha256':hashlib.sha256(s.encode()).hexdigest(),'after_sha256':hashlib.sha256(t.encode()).hexdigest(),'edits':len(pending),'visible_content_preserved_except_documented_printed_citation':True})
for file,t in outputs.items():(r/file).write_text(t)
report={'baseline_commit':'ea116c5f61fcfa9c499922abdb7be5622c71bfb3','scope':'Bounded repair of previously reported semantic wrong-links, plus explicitly identified adjacent same-kind references; not a new full-book review.','counts':dict(Counter(i['decision'] for i in ledger)),'new_anchors':anchors,'files':checks,'items':ledger,'policy':'replace_key preserves visible text; external preserves known external citation text without internal hyperlink; pending preserves original text, removes misleading hyperlink and prints 〔引文待核〕. Historical review reports remain unchanged; this ledger supersedes their link disposition.'}
(out/'APPLIED.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
md=['# 已报告语义错链：最终逐项处置','',report['scope'],'','原行号据基线 `'+report['baseline_commit']+'`；新增锚点会移动后续行。实际调用、完整显示参数及证据见 APPLIED.json。','',str(report['counts']),'','| 原文件:行 | 原引用/键 | 处置/新目标 | 依据 |','|---|---|---|---|']
for i in ledger:
    def cell(v):return str(v or '').replace('|','\\|').replace('\n',' ')
    md.append('| '+cell(i['file'])+':'+str(i['line'])+' | `'+cell(i.get('visible_tex',i.get('old_text',i.get('text'))))+'` / `'+cell(i.get('old_key'))+'` | '+i['decision']+(' → `'+i['new_key']+'`' if i.get('new_key') else '')+' | '+cell(i['evidence'])+' |')
(out/'APPLIED.md').write_text('\n'.join(md)+'\n')
print(json.dumps({'counts':report['counts'],'new_anchors':len(anchors),'files':len(checks)},ensure_ascii=False))
