#!/usr/bin/env python3
"""Audit the frozen source and prepare references without inventing missing targets.
Run from any directory. No network, TeX execution or source mutation.
"""
from pathlib import Path
from collections import Counter
import argparse, hashlib, json, re, zipfile
ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parents[2]
PREFIX='native/SGA4/SGA4_English_current_buildable_source_20260906/source/'
ROMAN={10:'X',11:'XI',12:'XII',13:'XIII',14:'XIV',15:'XV',16:'XVI',17:'XVII',18:'XVIII',19:'XIX'}
def sha(b): return hashlib.sha256(b).hexdigest()
def expand(z,i):
    base=PREFIX+f'{i:02}/'
    s=z.read(base+f'{i:02}_English.tex').decode().replace('\r\n','\n')
    s=s.split('\\else\n',1)[1].replace('\\fi\n','',1)
    for _ in range(12):
        t=re.sub(r'\\input\{([^}]+)\}',lambda m:z.read(base+m[1]).decode().replace('\r\n','\n'),s)
        if t==s: break
        s=t
    return re.sub(r'\\ifx\\danslelivre\\undefined\s*\\end\{document\}\s*\\fi\s*','',s)
def clean(s): return re.sub(r'(?m)(?<!\\)%.*$','',s)
def math(s):
    return re.findall(r'(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$(?!\$).*?(?<!\\)\$',clean(s),re.S)
def reference_keys(s):
    keys=[]
    for m in re.finditer(r'\\(?:eq)?hyperref(?:ext)?(?:\[[^\]]*\])+|\\(?:ref|pageref|cite)(?:\[[^\]]*\])?\{([^}]+)\}',clean(s)):
        if m.group(1) is not None:
            keys.extend(k.strip() for k in m.group(1).split(','))
        else:
            keys.append(re.findall(r'\[([^\]]*)\]',m.group())[-1])
    return Counter(keys)
def norm(s):
    # Normalize translated prose inside text boxes, retaining every nested
    # dollar-delimited mathematical expression. Mathematical operators such
    # as mathrm/ operatorname are NOT stripped.
    def textboxes(t):
        out='';pos=0
        pat=re.compile(r'\\(?:text|mbox|hbox|txt|nde|acorriger)\{')
        while (m:=pat.search(t,pos)):
            out+=t[pos:m.start()];depth=1;j=m.end()
            while j<len(t) and depth:
                if t[j]=='{' and (j==0 or t[j-1]!='\\'):depth+=1
                elif t[j]=='}' and (j==0 or t[j-1]!='\\'):depth-=1
                j+=1
            body=t[m.end():j-1]
            nested=re.findall(r'(?<!\\)\$.*?(?<!\\)\$',body,re.S)
            out+='TEXTBOX{'+''.join(sorted(re.sub(r'\s+','',n) for n in nested))+'}';pos=j
        return out+t[pos:]
    s=s.replace(r'\rm adjunction',r'\text{伴随}').replace(r'\rm adj',r'\text{伴随}').replace('structural',r'\text{结构}')
    # XVIII Lemma3.1.10.3: translate only the prose in the arrow label,
    # retaining the reference number and the mathematical object V.
    s=s.replace(r'3.1.4.3\; on\; V',r'3.1.4.3\;\text{在}\; V')
    s=textboxes(s)
    s=s.replace(r'n\sisi{th}{-th}',r'n\sisi{}{}').replace(r'\tag*{if}',r'\tag*{若}').replace(r'\tag*{where}',r'\tag*{其中}')
    s=s.replace('TEXTBOX{}','')
    s=re.sub(r'@([CR])=-?[0-9.]+(?:em|cm|pt|pc)',r'@\1=LAYOUT',s)
    s=s.replace(r'\begin{gathered}','').replace(r'\end{gathered}','').replace(r'\allowbreak','')
    s=s.replace(r'\quav',',').replace(r'\quad','').replace(r'\\','')
    return re.sub(r'\s+','',s)

p=argparse.ArgumentParser();p.add_argument('--source-zip',type=Path,default=REPO/'en/KokunoYumeto-sga-en/release/00_SGA_EN_CUMULATIVE_SOURCE_PROJECTS.zip');args=p.parse_args()
z=zipfile.ZipFile(args.source_zip);manifest=json.loads(z.read('SOURCE_MANIFEST.json'))
fail=[e['name'] for e in manifest if len(z.read(e['name']))!=e['bytes'] or sha(z.read(e['name'])).lower()!=e['sha256'].lower()]
if fail:raise SystemExit('Source manifest failures: '+str(fail))
src={i:expand(z,i) for i in ROMAN}
reader=z.read('release/04_SGA4_EN_COMPLETE_READER.tex').decode().replace('\r\n','\n')
labels=dict((key,num) for num,key in re.findall(r'\\etiquette\[([^]]*)\]\{([^}]+)\}',reader))
for key in re.findall(r'\\label\{([^}]+)\}',reader):labels.setdefault(key,key.split('.')[-1])
outputs=sorted((ROOT/'chapters').glob('*-zh.tex'))
active=[ROOT/m for m in re.findall(r'\\input\{(chapters/[^}]+)\}',(ROOT/'main.tex').read_text())]
target='\n'.join(clean(f.read_text()) for f in active if f.exists())
internal=set(re.findall(r'\\(?:label|bibitem)\{([^}]+)\}',target))|set(re.findall(r'\\etiquette\[[^]]*\]\{([^}]+)\}',target))
external={k:v for k,v in labels.items() if k not in internal and '#' not in k+v}
refs=set(re.findall(r'\\(?:hyperref|eqhyperref|pagehyperref)\[([^]]+)\]',target))|set(re.findall(r'\\(?:hyperrefext|eqhyperrefext|neweqhyperrefext)\[[^]]*\]\[([^]]+)\]',target))|set(re.findall(r'\\(?:ref|pageref)\{([^}]+)\}',target))
unknown=sorted(refs-internal-set(labels))
registry=['% Generated source-backed external reference registry. No synthetic content/pages.']
for k,v in sorted(external.items()):registry.append('\\expandafter\\def\\csname SGAsource@'+k+'\\endcsname{'+v+'}')
registry+= [r'\let\SGAoriginalhyperref\hyperref',r'\renewcommand{\hyperref}[2][]{\ifcsname SGAsource@#1\endcsname #2\else\SGAoriginalhyperref[#1]{#2}\fi}',r'\AtBeginDocument{\let\SGAoriginalref\ref\renewcommand{\ref}[1]{\ifcsname SGAsource@#1\endcsname\csname SGAsource@#1\endcsname\else\SGAoriginalref{#1}\fi}}']
(ROOT/'style/external-references.tex').write_text('\n'.join(registry)+'\n')
report={'archive_manifest_entries':len(manifest),'archive_manifest_failures':fail,'archive_sha256':sha(args.source_zip.read_bytes()),'source_reader_sha256':sha(z.read('release/04_SGA4_EN_COMPLETE_READER.tex')),'internal_label_count':len(internal),'referenced_external_labels':sorted(refs&set(external)),'static_unknown_keys_including_inactive_original_alternatives':unknown,'notes':['Known out-of-scope references print their original explicit citation or source-backed number without dead PDF links.','Unknown source keys are preserved and remain real warnings. They are not fabricated or hidden.','Math counters below are mechanical aids; translator statuses record more precise protected-block checks.'],'chapters':[]}
for i in ROMAN:
    files=[ROOT/'chapters'/f'exp-{i:02}-zh.tex']
    if not files[0].exists():files=sorted((ROOT/'chapters').glob(f'exp-{i:02}-part*-zh.tex'))
    t='\n'.join(f.read_text() for f in files)
    original_a=Counter(norm(x) for x in math(src[i]));b=Counter(norm(x) for x in math(t))
    comparison_source=src[i]
    corrections=[]
    for correction in json.loads((ROOT/'evidence/SOURCE_CORRECTIONS.json').read_text())['corrections']:
        if correction['expose']==i and 'source_before' in correction:
            before=correction['source_before'];after=correction['source_comparison_after']
            if comparison_source.count(before)!=1:
                raise ValueError('Source correction context not unique: '+correction['id'])
            comparison_source=comparison_source.replace(before,after,1)
            corrections.append(correction['id'])
    a=Counter(norm(x) for x in math(comparison_source))
    pats={'semantic_labels':r'\\etiquette\[[^]]*\]\{[^}]+\}','bibliography_keys':r'\\bibitem(?:\[[^\]]*\])?\{[^}]+\}','environments':r'\\(?:begin|end)\{[^}]+\}'}
    entry={'expose':ROMAN[i],'source_expanded_sha256':sha(src[i].encode()),'source_lines':len(src[i].splitlines()),'translation_files':[str(f.relative_to(ROOT)) for f in files],'translation_hashes':{str(f.relative_to(ROOT)):sha(f.read_bytes()) for f in files},'math_blocks_source':sum(a.values()),'math_blocks_output':sum(b.values()),'original_frozen_math_multiset_normalized_equal':original_a==b,'original_frozen_math_source_only_count':sum((original_a-b).values()),'original_frozen_math_output_only_count':sum((b-original_a).values()),'documented_source_corrections_for_comparison':corrections,'math_multiset_normalized_equal':a==b,'math_source_only_count':sum((a-b).values()),'math_output_only_count':sum((b-a).values())}
    ra=reference_keys(src[i]);rb=reference_keys(t);expected=ra.copy()
    ref_corrections=[]
    if i==12:
        expected['XII.prop3.1']-=1
        ref_corrections.append('XII-5.10-Artin-link')
    if i==15:
        expected['XV.prop1.6']-=1;expected['XV.prop1.1']+=1
        ref_corrections.append('XV-1.10-proof-reference')
    entry['reference_keys']={'original_source_count':sum(ra.values()),'output_count':sum(rb.values()),'original_multiset_equal':ra==rb,'documented_corrections':ref_corrections,'equal_after_documented_corrections':expected==rb,'unexplained_source_only':dict(expected-rb),'unexplained_output_only':dict(rb-expected)}
    display_pat=r'\\\[.*?\\\]|\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?|displaymath)\}.*?\\end\{\1\}'
    def displays(t):
        return [m.group() for m in re.finditer(display_pat,clean(t),re.S)]
    def dn(v):
        v=norm(v)
        if r'\xymatrix' not in v:v=v.replace('&','')
        return v
    da=Counter(dn(v) for v in displays(src[i]));db=Counter(dn(v) for v in displays(t))
    entry['additional_display_environments']={'source_count':sum(da.values()),'output_count':sum(db.values()),'normalized_multiset_equal':da==db,'source_only_count':sum((da-db).values()),'output_only_count':sum((db-da).values())}
    for name,pat in pats.items():
        ac=Counter(re.findall(pat,clean(src[i])));bc=Counter(re.findall(pat,clean(t)))
        entry[name]={'source_count':sum(ac.values()),'output_count':sum(bc.values()),'multiset_equal':ac==bc}
    report['chapters'].append(entry)
(ROOT/'evidence/SOURCE_AND_REFERENCE_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_failures':fail,'static_unknown_keys_including_inactive_original_alternatives':unknown,'exposes_audited':len(report['chapters'])},ensure_ascii=False))
