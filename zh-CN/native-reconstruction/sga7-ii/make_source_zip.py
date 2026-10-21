#!/usr/bin/env python3
from pathlib import Path
import json,hashlib,zipfile
r=Path(__file__).resolve().parent
excluded={'SGA7-II-zh-CN.pdf','SGA7-II-zh-CN-source.zip','SOURCE_ARCHIVE_MANIFEST.json','DELIVERY_SHA256SUMS.txt'}
files=sorted(p for p in r.rglob('*') if p.is_file() and 'build' not in p.relative_to(r).parts and '__pycache__' not in p.relative_to(r).parts and p.name not in excluded)
rows=[{'path':p.relative_to(r).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]
(r/'SOURCE_ARCHIVE_MANIFEST.json').write_text(json.dumps({'scope':'Chinese native source and its pinned runtime dependencies, documentation and audit evidence; build cache and separately delivered PDF excluded','files':rows},ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(r/'SGA7-II-zh-CN-source.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in files+[r/'SOURCE_ARCHIVE_MANIFEST.json']:
  info=zipfile.ZipInfo('sga7-ii/'+p.relative_to(r).as_posix(),date_time=(2026,10,21,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;z.writestr(info,p.read_bytes())
with zipfile.ZipFile(r/'SGA7-II-zh-CN-source.zip') as z:
 for row in rows:assert hashlib.sha256(z.read('sga7-ii/'+row['path'])).hexdigest()==row['sha256'],row['path']
names=['main.tex','SGA7-II-zh-CN.pdf','SGA7-II-zh-CN-source.zip','SOURCE_LOCK.json','PROGRESS.json','SOURCE_ARCHIVE_MANIFEST.json']
(r/'DELIVERY_SHA256SUMS.txt').write_text(''.join(hashlib.sha256((r/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))
print('Verified archive source files:',len(rows))
