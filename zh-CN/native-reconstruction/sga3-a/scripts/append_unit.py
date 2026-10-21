#!/usr/bin/env python3
"""Append one fully translated, source-enumerated exposé without rewriting completed units."""
from pathlib import Path
import argparse,re
p=argparse.ArgumentParser();p.add_argument('unit');p.add_argument('--source-root',type=Path,required=True);a=p.parse_args()
r=Path(__file__).resolve().parents[1]
unit=a.unit
mapping={'V':('V','tex/components','*'), 'VI-A':('VI','tex_reference_v2/components','*VIA_*'),'VI-B':('VI','tex_reference_v2/components','*VIB_*')}
if unit not in mapping:raise SystemExit('Add an inspected unit mapping first')
chap,component_dir,glob_pat=mapping[unit]
originals=sorted((a.source_root/'inputs'/chap/component_dir).glob(glob_pat+'.tex'))
if not originals:raise SystemExit('No source components')
translated=[r/'chapters'/unit/(x.stem+'-zh.tex') for x in originals]
for f in translated:
 if not f.is_file() or not f.read_text().strip():raise SystemExit('Missing translated component: '+str(f))
main_path=r/'main.tex';main_text=main_path.read_text()
marker='% TRANSLATED UNIT '+unit
if marker in main_text:raise SystemExit('Already assembled: '+unit)
pre='\n'+marker+'\n'
if unit=='V':
 pre+=r'''\SGAStartExpose{V}
\providecommand{\SGAThreeDiagram}[5][0.92\textwidth]{%
  \begin{figure}[H]
    \centering
    \resizebox{#1}{!}{\input{#2.tex}}%
    \caption{#3}\label{#4}
    \par\smallskip
    {\footnotesize\itshape 根据经订正的 Polo--Gille 图以原生 \LaTeX{} 重建; 来源定位: #5.}
  \end{figure}%
}
'''
elif unit=='VI-A':pre+='\\SGAStartExpose{VI}\n'
# VI-B retains the original combined-VI wrapper's counter behavior.
pre+=''.join('\\input{'+str(f.relative_to(r).with_suffix(''))+'}\n' for f in translated)
pre+='% END TRANSLATED UNIT '+unit+'\n'
assert main_text.count('\\end{document}')==1
last='IV' if unit=='V' else 'V' if unit=='VI-A' else 'VI-A'
main_text=main_text.replace('第 I--'+last+' 篇','第 I--'+unit+' 篇')
main_path.write_text(main_text.replace('\\end{document}',pre+'\\end{document}'))
print('Appended',unit,len(translated),'components')
