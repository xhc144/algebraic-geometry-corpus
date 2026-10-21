#!/usr/bin/env python3
"""Compare frozen source components with Chinese translation; compile proof is separate."""
from pathlib import Path
from collections import Counter
import re,json,hashlib
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
lock=json.loads((ROOT/'SOURCE_LOCK.json').read_text())
source=(REPO/lock['chosen_source']).read_text()
parts={m[1]:m[3] for m in re.finditer(r'% Original input: (.*?)\n\\begin\{filecontents\*\}\[overwrite,noheader\]\{(.*?)\}\n(.*?)\\end\{filecontents\*\}',source,re.S)}
pat=re.compile(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|tikzcd|tikzpicture)\}.*?\\end\{\1\}|\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',re.S)
def textless(s):
    # Remove translated descriptions only, retaining dollar-delimited math inside them.
    nested_math=[]
    def minipage(m):
        nested_math.extend(re.findall(r'(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',m[2]))
        return m[1]+m[3]
    s=re.sub(r'(\\begin\{minipage\}\{[^}]*\})(.*?)(\\end\{minipage\})',minipage,s,flags=re.S)
    found=True
    while found:
        found=False
        m=re.search(r'\\(?:text|textrm|textnormal|textup|mbox)\s*\{',s)
        if m:
            depth=1;j=m.end()
            while j<len(s) and depth:
                if s[j]=='{' and (j==0 or s[j-1]!='\\'):depth+=1
                if s[j]=='}' and (j==0 or s[j-1]!='\\'):depth-=1
                j+=1
            inner=s[m.end():j-1]
            keep=''.join(x[0] for x in re.finditer(r'(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',inner))
            nested_math.extend(re.findall(r'(?<!\\)\$(?:\\.|[^$])*?(?<!\\)\$',inner))
            s=s[:m.start()]+s[j:];found=True
    s=re.sub(r'\\mathrm\{(?:proximate|to|on)\}','',s)
    # One English transcription error verified against French printed p.377.
    s=s.replace('q^{,i-\\dim X}','q^{i-\\dim X}')
    return re.sub(r'\s+','',s)+';TEXTMATH:'+repr(sorted(re.sub(r'\s+','',x) for x in nested_math))
rows=[]
for c in lock['components']:
    src=parts[c['source_component']];p=ROOT/c['translation']
    row={'component':c['source_component'],'translation':c['translation'],'exists':p.exists(),'source_lines':len(src.splitlines())}
    if not p.exists():rows.append(row);continue
    dst=p.read_text();sm=[m[0] for m in pat.finditer(src)];dm=[m[0] for m in pat.finditer(dst)]
    si=[x for x in sm if x.startswith('$')];di=[x for x in dm if x.startswith('$')]
    sd=[x for x in sm if not x.startswith('$')];dd=[x for x in dm if not x.startswith('$')]
    row.update(output_lines=len(dst.splitlines()),source_math_fragments=len(sm),output_math_fragments=len(dm),source_inline=len(si),output_inline=len(di),source_displays=len(sd),output_displays=len(dd),inline_math_multiset_equal=Counter(map(textless,si))==Counter(map(textless,di)),display_math_sequence_equal=list(map(textless,sd))==list(map(textless,dd)),tags_equal=re.findall(r'\\tag\*?\{([^}]*)\}',src)==re.findall(r'\\tag\*?\{([^}]*)\}',dst),labels_refs_equal=re.findall(r'\\(?:label|ref|eqref|pageref)\{[^}]*\}',src)==re.findall(r'\\(?:label|ref|eqref|pageref)\{[^}]*\}',dst),environment_sequence_equal=re.findall(r'\\(?:begin|end)\{[^}]*\}',src)==re.findall(r'\\(?:begin|end)\{[^}]*\}',dst),translation_sha256=hashlib.sha256(dst.encode()).hexdigest())
    if not row['inline_math_multiset_equal']:
        a=Counter(map(textless,si));b=Counter(map(textless,di));row['inline_difference_source']=list((a-b).elements());row['inline_difference_translation']=list((b-a).elements())
    if not row['display_math_sequence_equal']:
        row['display_differences']=[{'index':i,'source':textless(a),'translation':textless(b)} for i,(a,b) in enumerate(zip(sd,dd)) if textless(a)!=textless(b)]
    rows.append(row)
report={'method':'Automated source structure/math comparison; translated text nodes and minipage prose ignored; embedded dollar math retained as a multiset per display to allow Chinese word order. Formula proof and prose proofreading remain separate.','known_emendation':'XXI Theorem 2.1 stray exponent comma removed only after French PDF page 387 (printed377) verification; see review/xxi-xxii.json.','components':rows}
(ROOT/'review/mechanical-audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
for r in rows:
    bad=[k for k,v in r.items() if (k.endswith('_equal') and not v)]
    if bad:print(r['component'],bad)
print('Translated',sum(x['exists'] for x in rows),'/',len(rows),'Math',sum(x.get('source_math_fragments',0) for x in rows),sum(x.get('output_math_fragments',0) for x in rows))
failed=[r['component'] for r in rows if not r['exists'] or any(not v for k,v in r.items() if k.endswith('_equal'))]
if failed:raise SystemExit('Audit differences need review: '+repr(failed))
