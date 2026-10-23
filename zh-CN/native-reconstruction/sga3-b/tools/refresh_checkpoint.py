#!/usr/bin/env python3
"""Include real translated files; never fill missing units with source prose."""
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]
units=['XIII','XIV','XV','XVI','XVII','XVIII','GUIDE','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','TERMINAL_INDEX']
lock=json.loads((p/'SOURCE_LOCK.json').read_text())
source_units={r['unit']:r for r in lock['expanded_units']}
text=[];status=[]
for u in units:
 f=p/'chapters'/(u+'-zh.tex');cov=p/'coverage'/(u+'.json')
 c=json.loads(cov.read_text()) if cov.exists() else {}
 intervals=next((c[k] for k in ['translated_source_intervals','translated_source_lines','covered_source_intervals'] if k in c),[])
 total=source_units[u]['lines']
 full=intervals==[[1,total]] and bool(c.get('complete',c.get('translation_complete',False))) and f.exists()
 status.append({'unit':u,'file_exists':f.exists(),'source_lines':total,'translated_source_lines':sum(z-a+1 for a,z in intervals),'translation_complete':full,'coverage':c})
 if not f.exists() or not f.stat().st_size:continue
 text.append('\\clearpage' if u in ['GUIDE','TERMINAL_INDEX'] else '\\SGAStartExpose{'+u+'}')
 if u=='XIV':text.append('\\chapter*{第 XIV 讲\\\\正则元素（续）\\\\在代数群中的应用}\n\\addcontentsline{toc}{chapter}{第 XIV 讲. 正则元素（续）}\n\\begin{center}A. Grothendieck 著, 附录由 J.-P. Serre 撰写\\end{center}')
 if u=='XX':text.append('\\chapter*{第 XX 讲\\\\半单秩为 1 的约化群}\n\\addcontentsline{toc}{chapter}{第 XX 讲. 半单秩为 1 的约化群}\n\\begin{center}M. Demazure 著\\end{center}')
 if u=='XXI':text.append('\\counterwithin{theorem}{subsection}\n\\renewcommand{\\thesubsection}{\\thesection.\\arabic{subsection}}')
 if u=='XXIII':text.append('\\renewcommand{\\SGAProof}{\\par\\smallskip\\noindent\\textit{证明.}\\quad}')
 if u=='XXVI':
  for op in ['rad','Of']:text.append('\\providecommand{\\'+op+'}{\\operatorname{'+op+'}}')
  for op in ['Transt','Tor','Lev','Par','Crit','Bor','Gen','Opp','Stand','TypeStand']:text.append('\\providecommand{\\'+op+'}{\\underline{\\operatorname{'+op+'}}}')
  text.append('\\providecommand{\\Int}{\\operatorname{int}}\n\\renewcommand{\\Centr}{\\underline{\\operatorname{Centr}}}\n\\renewcommand{\\Norm}{\\underline{\\operatorname{Norm}}}')
 text.append('\\input{chapters/'+u+'-zh}')
 if u=='XXI':text.append('\\counterwithin{theorem}{section}')
(p/'chapters-current.tex').write_text('\n'.join(text)+'\n')
translation_complete=all(s['translation_complete'] for s in status)
review_path=p/'review/20261022/STATUS.json'
review=json.loads(review_path.read_text()) if review_path.exists() else {}
review_complete=bool(review.get('independent_fidelity_reading_complete',False))
parts=[]
for cf in sorted((p/'coverage-parts').glob('*.json')):
 c=json.loads(cf.read_text())
 parts.append({'file':str(cf.relative_to(p)),'coverage':c})
(p/'PROGRESS.json').write_text(json.dumps({'complete':translation_complete and review_complete,'translation_complete':translation_complete,'independent_fidelity_reading_complete':review_complete,'independent_proofreading_complete':review_complete,'mathematical_source_validity_certified':False,'state':'independently_reviewed_translation' if review_complete else 'translation_complete_review_pending' if translation_complete else 'partial_translation_in_progress','review_record':'review/20261022/STATUS.json' if review else None,'scope':'XIII--XXVI; GUIDE; TERMINAL_INDEX','source_lines':sum(s['source_lines'] for s in status),'translated_source_lines':sum(s['translated_source_lines'] for s in status),'units':status,'separate_part_checkpoints':parts,'source_coverage_and_proofreading_distinct':True,'complete_explanation':'Complete means assigned translation coverage and independent bilingual fidelity reading. It does not certify every mathematical statement in the inherited source or every external citation.'},ensure_ascii=False,indent=2)+'\n')
print('Included',sum(s['file_exists'] for s in status),'actual translated files')
