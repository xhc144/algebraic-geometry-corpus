#!/usr/bin/env python3
"""Compare translated components to the pinned native ZIP, without modifying sources."""
from pathlib import Path
import argparse, collections, hashlib, json, re, zipfile
p=argparse.ArgumentParser();p.add_argument('archive',type=Path);p.add_argument('--through',type=int,default=99);a=p.parse_args()
root=Path(__file__).resolve().parents[1]
z=zipfile.ZipFile(a.archive)
prefix='native/SGA3/SGA3_English_current_buildable_source_20260823/source/'
allnames=z.namelist()
def prose(s):
    s=re.sub(r'\\text\{[^{}]*\}',r'\\text{LANG}',s)
    return re.sub(r'\s+','',s)
def math(s):
    pats=[r'\\\((.*?)\\\)',r'(?<!\\)\\\[(.*?)\\\]',r'(?<!\\)\$(?!\$)(.*?)(?<!\\)\$',r'\\begin\{(?:align\*?|equation\*?|gather\*?|multline\*?)\}(.*?)\\end\{(?:align\*?|equation\*?|gather\*?|multline\*?)\}']
    return [collections.Counter(prose(t) for t in re.findall(q,s,re.S)) for q in pats]
def keys(s,cmd):return re.findall(r'\\'+cmd+r'\{([^{}]+)\}',s)
active=set()
def inputs(f):
    f=f.resolve()
    if f in active or not f.is_file():return
    active.add(f)
    for n in re.findall(r'\\input\{([^{}#]+)\}',f.read_text()):
        if '\\' in n:continue
        q=root/n
        if not q.suffix:q=q.with_suffix('.tex')
        if q.is_file():inputs(q)
inputs(root/'main.tex')
result=[];refs=[];targets=[]
for f in sorted((root/'chapters').rglob('*-zh.tex')):
    if f.resolve() not in active:continue
    if int(f.name.split('_')[0])>a.through:continue
    name=f.name.replace('-zh.tex','.tex')
    matches=[n for n in allnames if n.startswith(prefix) and n.endswith('/'+name)]
    if len(matches)!=1:raise ValueError((f,matches))
    src=z.read(matches[0]);s=src.decode('utf8').replace('\r\n','\n');t=f.read_text()
    sm,tm=math(s),math(t)
    diffs=[]
    for kind,x,y in zip(['inline_parens','display_brackets','dollar_math','equation_align'],sm,tm):
        if x!=y:diffs.append({'kind':kind,'source_only':list((x-y).elements()),'translation_only':list((y-x).elements())})
    k={}
    for cmd in ['SGARefTarget','SGAInlineRefTarget','SGAInlineEquationTarget','SGANextSectionTarget','SGARefLink','label','tag']:
        k[cmd]={'source':len(keys(s,cmd)),'translation':len(keys(t,cmd)),'same_key_multiset':collections.Counter(keys(s,cmd))==collections.Counter(keys(t,cmd))}
    refs.extend(keys(t,'SGARefLink'))
    for cmd in ['SGARefTarget','SGAInlineRefTarget','SGAInlineEquationTarget','SGANextSectionTarget','label']:targets.extend(keys(t,cmd))
    result.append({'file':str(f.relative_to(root)),'source_member':matches[0],'source_sha256':hashlib.sha256(src).hexdigest(),'translation_sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'source_lines':len(s.splitlines()),'translation_lines':len(t.splitlines()),'math_counts_source':[sum(x.values()) for x in sm],'math_counts_translation':[sum(x.values()) for x in tm],'math_differences':diffs,'keys':k,'footnotes_source':len(re.findall(r'\\footnote\{',s)),'footnotes_translation':len(re.findall(r'\\footnote\{',t))})
missing=collections.Counter(x for x in refs if x not in set(targets))
report={'scope':'all currently saved translated component files, including components not yet included in main.tex; not a completeness or mathematical proof certification','math_comparison':'whitespace normalized; simple text{} natural-language arguments normalized; named source errata listed separately','components':result,'unresolved_sga_ref_links':dict(sorted(missing.items())),'reference_fallback_warning':'SGARefLink intentionally prints its text when a target is absent. Therefore zero LaTeX undefined-reference warnings does NOT mean every SGARefLink resolves. See this list and SOURCE_ISSUES.md.'}
(root/'audit/COMPONENT_CHECKS.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'components':len(result),'math_difference_components':[r['file'] for r in result if r['math_differences']],'key_difference_components':[r['file'] for r in result if any(not k['same_key_multiset'] for k in r['keys'].values())],'unresolved_ref_keys':len(missing)},ensure_ascii=False))
