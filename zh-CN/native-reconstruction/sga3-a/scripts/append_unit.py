#!/usr/bin/env python3
"""Append one fully translated, source-enumerated exposé without rewriting completed units."""
from pathlib import Path
import argparse,re
p=argparse.ArgumentParser();p.add_argument('unit');p.add_argument('--source-root',type=Path,required=True);a=p.parse_args()
r=Path(__file__).resolve().parents[1]
unit=a.unit
mapping={'V':('V','tex/components','*'), 'VI-A':('VI','tex_reference_v2/components','*VIA_*'),'VI-B':('VI','tex_reference_v2/components','*VIB_*'), 'VII-A':('VII','tex/components','*VIIA_*'), 'VII-B':('VII','tex/components','*VIIB_*'), 'TOMEI_INDEX':('TOMEI_INDEX','index_tomeI/tex/components','*')}
for number in ['VIII','IX','X','XI','XII']:mapping[number]=(number,'tex/components','*')
if unit not in mapping:raise SystemExit('Add an inspected unit mapping first')
chap,component_dir,glob_pat=mapping[unit]
originals=sorted((a.source_root/'inputs'/chap/component_dir).glob(glob_pat+'.tex'))
if unit in ['VIII','IX','X','XI','XII']:
 body=(a.source_root/'inputs'/chap/'body.tex').read_text()
 originals=[(a.source_root/'inputs'/chap/n).with_suffix('.tex') for n in re.findall(r'\\input\{([^{}]+)\}',body)]
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
elif unit=='VII-A':pre+='\\SGAStartExpose{VII}\n'
elif unit=='TOMEI_INDEX':
 pre+=r'''\clearpage
\chapter*{第一卷索引}
\addcontentsline{toc}{chapter}{第一卷索引}
\markboth{第一卷索引}{第一卷索引}
\noindent\emph{页码指 Polo--Gille 重版本的页码.}
\medskip
\begin{multicols}{2}
\small
\setlength{\parskip}{1.2pt}
\interlinepenalty=10000
'''
elif unit in ['VIII','IX','X','XI','XII']:
 if unit=='VIII':pre+='\\newgeometry{margin=30mm}\n\\SGATagsLeft\n'
 pre+='\\SGAStartExpose{'+unit+'}\n'
 if unit=='X':pre+='\\markboth{第 X 篇. 乘法型群}{第 X 篇. 乘法型群}\n'
 if unit=='XII':
  pre+=r'''\chapter*{第 XII 篇\\极大环面、Weyl 群、Cartan 子群与约化中心}
\addcontentsline{toc}{chapter}{第 XII 篇. 极大环面、Weyl 群、Cartan 子群与约化中心}
\markboth{第 XII 篇. 极大环面与 Weyl 群}{第 XII 篇. 极大环面与 Weyl 群}
\begin{center}
\textit{A. Grothendieck 著}
\end{center}
'''
# VI-B retains the original combined-VI wrapper's counter behavior.
pre+=''.join('\\input{'+str(f.relative_to(r).with_suffix(''))+'}\n' for f in translated)
if unit=='TOMEI_INDEX':pre+='\\end{multicols}\n'
pre+='% END TRANSLATED UNIT '+unit+'\n'
assert main_text.count('\\end{document}')==1
if unit!='TOMEI_INDEX':main_text=re.sub(r'第 I--[A-Z-]+ 篇；分配范围', '第 I--'+unit+' 篇；分配范围', main_text)
main_path.write_text(main_text.replace('\\end{document}',pre+'\\end{document}'))
print('Appended',unit,len(translated),'components')
