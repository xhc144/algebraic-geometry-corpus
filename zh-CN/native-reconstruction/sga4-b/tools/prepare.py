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
def norm(s):
    # Only prose within mathematical text commands is normalized. Mathematical
    # content inside such text boxes remains visible to human review.
    s=re.sub(r'\s+','',s)
    for a,b in [('where','其中'),('for','对于'),('if','若'),('and','且'),('but','但')]:
        s=s.replace(a,b)
    return s
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
registry+= [r'\let\SGAoriginalhyperref\hyperref',r'\renewcommand{\hyperref}[2][]{\ifcsname SGAsource@#1\endcsname #2\else\SGAoriginalhyperref[#1]{#2}\fi}',r'\let\SGAoriginalref\ref',r'\renewcommand{\ref}[1]{\ifcsname SGAsource@#1\endcsname\csname SGAsource@#1\endcsname\else\SGAoriginalref{#1}\fi}']
(ROOT/'style/external-references.tex').write_text('\n'.join(registry)+'\n')
report={'archive_manifest_entries':len(manifest),'archive_manifest_failures':fail,'archive_sha256':sha(args.source_zip.read_bytes()),'source_reader_sha256':sha(z.read('release/04_SGA4_EN_COMPLETE_READER.tex')),'internal_label_count':len(internal),'referenced_external_labels':sorted(refs&set(external)),'unknown_source_reference_keys':unknown,'notes':['Known out-of-scope references print their original explicit citation or source-backed number without dead PDF links.','Unknown source keys are preserved and remain real warnings. They are not fabricated or hidden.','Math counters below are mechanical aids; translator statuses record more precise protected-block checks.'],'chapters':[]}
for i in ROMAN:
    files=[ROOT/'chapters'/f'exp-{i:02}-zh.tex']
    if not files[0].exists():files=sorted((ROOT/'chapters').glob(f'exp-{i:02}-part*-zh.tex'))
    t='\n'.join(f.read_text() for f in files)
    a=Counter(norm(x) for x in math(src[i]));b=Counter(norm(x) for x in math(t))
    pats={'semantic_labels':r'\\etiquette\[[^]]*\]\{[^}]+\}','bibliography_keys':r'\\bibitem\{[^}]+\}','environments':r'\\(?:begin|end)\{[^}]+\}'}
    entry={'expose':ROMAN[i],'source_expanded_sha256':sha(src[i].encode()),'source_lines':len(src[i].splitlines()),'translation_files':[str(f.relative_to(ROOT)) for f in files],'translation_hashes':{str(f.relative_to(ROOT)):sha(f.read_bytes()) for f in files},'math_blocks_source':sum(a.values()),'math_blocks_output':sum(b.values()),'math_multiset_normalized_equal':a==b,'math_source_only_count':sum((a-b).values()),'math_output_only_count':sum((b-a).values())}
    for name,pat in pats.items():
        ac=Counter(re.findall(pat,clean(src[i])));bc=Counter(re.findall(pat,clean(t)))
        entry[name]={'source_count':sum(ac.values()),'output_count':sum(bc.values()),'multiset_equal':ac==bc}
    report['chapters'].append(entry)
(ROOT/'evidence/SOURCE_AND_REFERENCE_AUDIT.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'manifest_failures':fail,'unknown_source_reference_keys':unknown,'exposes_audited':len(report['chapters'])},ensure_ascii=False))
