#!/usr/bin/env python3
"""Freeze the currently buildable translated dependency closure into a source ZIP."""
from pathlib import Path
import argparse,hashlib,json,re,shutil,subprocess,zipfile
p=argparse.ArgumentParser();p.add_argument('--completed',nargs='+',required=True);p.add_argument('--visual',required=True);a=p.parse_args()
r=Path(__file__).resolve().parents[1]
log=(r/'build/main.log').read_text()
if 'Output written on' not in log or '\n! ' in log:raise SystemExit('Successful current build required')
info=subprocess.check_output(['pdfinfo',str(r/'build/main.pdf')],text=True)
pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
seen=set()
def visit(path):
 path=path.resolve()
 if path in seen:return
 if not path.is_file():raise FileNotFoundError(path)
 seen.add(path)
 if path.suffix!='.tex':return
 s=path.read_text()
 for n in re.findall(r'\\input\{([^{}#]+)\}',s)+re.findall(r'\{((?:chapters|figures)/[^{}#]+)\}',s):
  if '\\' in n:continue
  q=r/n
  if not q.suffix:q=q.with_suffix('.tex')
  if q.is_file():visit(q)
visit(r/'main.tex')
chapters=sorted(str(x.relative_to(r)) for x in seen if 'chapters' in x.parts)
d=json.loads((r/'PROGRESS.json').read_text());d.update({'state':'partial_translation_checkpoint','completed_exposes':a.completed,'unfinished_exposes':[x for x in d['assigned_exposes'] if x not in a.completed],'translated_components':[Path(x).stem.removesuffix('-zh') for x in chapters],'compile_status':'successful XeLaTeX/latexmk, '+str(pages)+' pages','scope_complete':len(a.completed)==len(d['assigned_exposes']),'proofreading_complete':False,'pdf':'sga3-a-zh.pdf','source_zip':'sga3-a-source.zip','source_zip_frozen_components':chapters,'last_durable_checkpoint':'Full translated text of exposés '+', '.join(a.completed)+' with native diagrams and bibliography; remaining assigned units unfinished.'})
(r/'PROGRESS.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
shutil.copyfile(r/'build/main.pdf',r/'sga3-a-zh.pdf')
qa={'compiled_exposes':a.completed,'command':'latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex','result':'success','pages':pages,'missing_character_messages':log.count('Missing character:'),'overfull_boxes':log.count('Overfull'),'underfull_boxes':log.count('Underfull'),'undefined_reference_warning_count':len(re.findall(r'Reference .* undefined',log)),'font_warnings':re.findall(r'LaTeX Font Warning: ([^\n]+)',log),'visual_status':a.visual,'reference_status':'See COMPONENT_CHECKS.json: source SGARefLink fallback suppresses absent-target warnings; zero warning is not a resolution certificate.','mathematical_review':'Known source issues and review limits remain in SOURCE_ISSUES.md; no final mathematical certification.','pdf_sha256':hashlib.sha256((r/'sga3-a-zh.pdf').read_bytes()).hexdigest()}
(r/'audit/BUILD-CURRENT.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2)+'\n')
for n in ['README.md','BUILD.md','PROGRESS.json','.gitignore','terminology.csv']:
 if (r/n).is_file():seen.add((r/n).resolve())
for folder in ['scripts','audit']:
 for f in (r/folder).rglob('*'):
  if f.is_file() and f.suffix not in ['.pyc','.log']:seen.add(f.resolve())
with zipfile.ZipFile(r/'sga3-a-source.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f in sorted(seen):z.write(f,f.relative_to(r))
print(json.dumps({'pages':pages,'included_chapter_files':len(chapters),'source_files':len(seen),'completed_exposes':a.completed,'pdf_sha256':qa['pdf_sha256']},ensure_ascii=False))
