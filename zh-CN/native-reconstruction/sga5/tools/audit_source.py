#!/usr/bin/env python3
"""Compare source-aligned native chapter structure and math with pinned source.
This checks preservation, not mathematical correctness or translation quality.
"""
from pathlib import Path
from collections import Counter
import re,json,hashlib
root=Path(__file__).resolve().parents[1]
source=root.parents[2]/'en/KokunoYumeto-sga-en/release/06_SGA5_EN_COMPLETE_PUBLISHED_CONTENT_READER.tex'
s=source.read_text().splitlines()
units=[('01-expose-i.tex',323,2150),('02-expose-iii.tex',2151,4477),('03-expose-iii-b.tex',4478,6947),('04-expose-v-vi.tex',6948,9352),('05-expose-vii-viii.tex',9353,12530),('06-expose-x-xii.tex',12531,14583),('07-expose-xv.tex',14584,15704),('08-indexes.tex',15705,15817)]
math=lambda x:re.findall(r'(?<!\\)\$(.+?)(?<!\\)\$|\\\((.*?)\\\)',x)
norm=lambda x:re.sub(r'\s+','',x)
report={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'scope':'source-aligned chapters323–15817; sourcepreamble/Englishtitlepage adapted separately, Frenchfrontmatter added separately','checks':[],'limitations':['Counts and tokens do not prove mathematical correctness.','Translated text labels inside math may legitimately differ.','Historical source references are predominantly literal rather than LaTeX refs; manual source issues remain recorded.']}
inline=[]
for name,a,b in units:
 original='\n'.join(s[a-1:b]);p=root/'chapters'/name;t=p.read_text();ls=t.splitlines()
 def inventory(x):return Counter(re.findall(r'\\(?:begin|end)\{[^}]+\}|\\(?:tag|label|ref|eqref|pageref)\{[^}]+\}',x))
 delta=inventory(t)-inventory(original);lost=inventory(original)-inventory(t)
 row={'file':str(p.relative_to(root)),'source_range':[a,b],'source_lines':b-a+1,'translation_lines':len(ls),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'structure_lost':dict(lost),'structure_added':dict(delta),'control_characters':sorted(set(ord(c) for c in t if ord(c)<32 and c not in '\n\t\r')),'inline_math_differences':0}
 if len(ls)!=b-a+1:
  row['inline_math_differences']=None
  row['inline_math_check']='Physical lines reflowed; use independent review and display/structure inventories, not a false zero. '
 if len(ls)==b-a+1:
  for i,(x,y) in enumerate(zip(s[a-1:b],ls)):
   c1=Counter(norm(v or w) for v,w in math(x));c2=Counter(norm(v or w) for v,w in math(y))
   if c1!=c2:
    inline.append({'file':name,'source_line':a+i,'target_line':i+1,'source':x,'target':y,'lost':dict(c1-c2),'added':dict(c2-c1)})
    row['inline_math_differences']+=1
 report['checks'].append(row)
(root/'qa/source-structure-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(root/'qa/inline-math-differences.json').write_text(json.dumps(inline,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
print('inline rows for review',len(inline))
