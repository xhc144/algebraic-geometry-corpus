from pathlib import Path
import json
root=Path(__file__).resolve().parent
lock=json.loads((root/'SOURCE_LOCK.json').read_text())
prev=None; lines=[]; present=[]; missing=[]
for c in lock['components']:
 p=root/c['translation']
 if not p.exists(): missing.append(c['source_component']); continue
 if c['expose']!=prev:
  prev=c['expose']
  lines += [r'\clearpage',r'\renewcommand{\CurrentExpose}{第 '+prev+r' 讲}']
  if prev=='X': lines += [r'\ExposeTOC',r'\begin{center}\underline{第 X 讲}\end{center}']
 lines.append(r'\input{'+c['translation']+'}')
 present.append(c['source_component'])
if missing: raise SystemExit('Untranslated or absent source components: '+repr(missing))
(root/'included-chapters.tex').write_text('\n'.join(lines)+'\n')
print('Present:',len(present),'Missing:',len(missing))
