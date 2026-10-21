#!/usr/bin/env python3
"""Include real translated files; never fill missing units with source prose."""
import json
from pathlib import Path
p=Path(__file__).resolve().parents[1]
units=['XIII','XIV','XV','XVI','XVII','XVIII','GUIDE','XIX','XX','XXI','XXII','XXIII','XXIV','XXV','XXVI','TERMINAL_INDEX']
text=[];status=[]
for u in units:
 f=p/'chapters'/(u+'-zh.tex');cov=p/'coverage'/(u+'.json')
 c=json.loads(cov.read_text()) if cov.exists() else {}
 status.append({'unit':u,'file_exists':f.exists(),'coverage':c})
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
(p/'PROGRESS.json').write_text(json.dumps({'complete':False,'state':'partial_translation_in_progress','scope':'XIII--XXVI; GUIDE; TERMINAL_INDEX','units':status,'source_coverage_and_proofreading_distinct':True},ensure_ascii=False,indent=2)+'\n')
print('Included',sum(s['file_exists'] for s in status),'actual translated files')
