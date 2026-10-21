#!/usr/bin/env python3
"""Package the native source closure and its audit files, excluding generated caches."""
from pathlib import Path
import zipfile,json,hashlib,datetime
root=Path(__file__).resolve().parents[1]
archive=root/'SGA4half-zh-CN-source.zip';manifest=root/'audit/archive-source-manifest.json'
def admitted(p):
 rel=p.relative_to(root)
 return p.is_file() and not any(x in rel.parts for x in ['build','__pycache__','.git']) and p.suffix not in ['.pdf','.zip','.pyc'] and p.name not in ['DELIVERABLES.sha256','archive-source-manifest.json']
files=sorted(p for p in root.rglob('*') if admitted(p))
manifest.write_text(json.dumps({'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'self_excluding':True,'files':[{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]},ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in [*files,manifest]:z.write(p,p.relative_to(root))
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 for r in json.loads(z.read('audit/archive-source-manifest.json'))['files']:
  assert hashlib.sha256(z.read(r['path'])).hexdigest()==r['sha256']
items=[root/'main.tex',root/'SGA4half-zh-CN.pdf',archive]
(root/'DELIVERABLES.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n' for p in items))
print(json.dumps({'archive':archive.name,'bytes':archive.stat().st_size,'entries':len(files)+1,'verified':True},ensure_ascii=False))
