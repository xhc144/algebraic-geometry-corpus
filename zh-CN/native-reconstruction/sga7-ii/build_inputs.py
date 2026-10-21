#!/usr/bin/env python3
"""Freeze the actual compiler inputs and reject an in-flight source mutation."""
from pathlib import Path
import hashlib,json,sys,datetime
r=Path(__file__).resolve().parent
files=sorted([r/'main.tex',r/'included-chapters.tex',r/'build.sh']+list((r/'chapters').glob('*/*.tex'))+list((r/'frontmatter').glob('*.tex'))+list((r/'dependencies').glob('*.tar.xz')))
rows=[{'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
p=r/'build/input-before.json'
if sys.argv[1]=='before':p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
else:
 if rows!=json.loads(p.read_text()):raise SystemExit('Compiler inputs changed during build; no delivery copied.')
 (r/'review/build-input-manifest.json').write_text(json.dumps({'compiled_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inputs_unchanged_across_two_passes':True,'files':rows},ensure_ascii=False,indent=2)+'\n')
