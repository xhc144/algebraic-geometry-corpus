#!/usr/bin/env python3
"""Bounded mechanical audit; does not certify translation or original completeness."""
from pathlib import Path
from collections import Counter
import re,json,hashlib
r=Path(__file__).resolve().parent
files=sorted((r/'chapters').glob('*.tex'))
texts={str(p.relative_to(r)):p.read_text() for p in files}
alltext='\n'.join(texts.values())
pat=r'\\sgaStableTarget(?:Inline)?\{([^}]+)\}'
targets=Counter(re.findall(pat,alltext))
links=Counter(re.findall(r'\\hyperlink\{([^}]+)\}',alltext))
missing=sorted(set(links)-set(targets))
source=r.parents[2]/'en/KokunoYumeto-sga-en/release/07_SGA6_EN_CURRENT_LAYERED_READER.tex'
source_info={}
if source.exists():
 s=source.read_text(); st=set(re.findall(pat,s));sl=set(re.findall(r'\\hyperlink\{([^}]+)\}',s))
 source_info={'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'stable_target_count':len(st),'targets_absent_from_translation':sorted(st-set(targets)),'missing_link_destinations_in_english':sorted(sl-st),'new_missing_link_destinations_in_chinese':sorted(set(missing)-(sl-st))}
log=r/'build/SGA6-zh-CN.log';console=r/'build/compile-pass2.txt';check={}
if log.exists():
 l=log.read_text(errors='replace');c=console.read_text(errors='replace') if console.exists() else ''
 check={'missing_glyph_messages':l.count('Missing character:'),'undefined_control_sequences':l.count('Undefined control sequence'),'overfull_hbox_count':l.count('Overfull \\hbox'),'overfull_vbox_count':l.count('Overfull \\vbox'),'undefined_latex_reference_messages':len(re.findall(r'Reference .* undefined',l)),'font_warnings':len(re.findall(r'LaTeX Font Warning:',l)),'latex_errors':re.findall(r'^!.*$',l,re.M),'compile_pass2_pdf_output':bool(re.search(r'Output written on .*\.pdf',c))}
 warnings=[];current='?'
 for line in c.splitlines():
  f=re.findall(r'\(\./(chapters/[^\s()]+\.tex)',line)
  if f:current=f[-1]
  if 'Overfull' in line:warnings.append({'file':current,'message':line})
 check['overflow_locations']=warnings
pdf_info={}
try:
 import fitz
 p=fitz.open(r/'build/SGA6-zh-CN.pdf');outside=[]
 for i,page in enumerate(p):
  for b in page.get_text('blocks'):
   if b[0]<-.5 or b[1]<-.5 or b[2]>page.rect.width+.5 or b[3]>page.rect.height+.5:
    outside.append({'page':i+1,'bbox':list(b[:4]),'text':b[4][:140]})
 pdf_info={'pages':len(p),'page_size_pt':list(p[0].rect)[2:],'text_blocks_outside_page':outside}
except Exception as e:pdf_info={'error':str(e)}
res={'scope':'Mechanical audit only; not proofreading, mathematical validation or original-completeness certificate','chapter_files':list(texts),'stable_targets':len(targets),'hyperlinks':sum(links.values()),'duplicate_targets':{k:v for k,v in targets.items() if v>1},'missing_hyperlink_targets':missing,'source_comparison':source_info,'compile':check,'pdf':pdf_info,'native_tex_sha256':{str(p.relative_to(r)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(r.rglob('*.tex')) if 'dependencies' not in p.parts and 'build' not in p.parts}}
(r/'audits/MECHANICAL.json').write_text(json.dumps(res,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'targets':len(targets),'duplicates':len(res['duplicate_targets']),'missing_targets':len(missing),'source_targets_absent':len(source_info.get('targets_absent_from_translation',[])),'compile':check,'pdf':pdf_info},ensure_ascii=False,indent=2))
