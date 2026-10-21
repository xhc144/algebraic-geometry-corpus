#!/usr/bin/env python3
"""Package the independently buildable native source, excluding generated PDF/cache."""
from pathlib import Path
import hashlib,zipfile
r=Path(__file__).resolve().parents[1]
exclude={'SGA5-zh-CN-source.zip','SHA256SUMS','SOURCE_BUNDLE_MANIFEST.sha256'}
files=sorted(p for p in r.rglob('*') if p.is_file() and '.build' not in p.relative_to(r).parts and p.name not in exclude and p.suffix.lower() not in ('.pdf','.png','.jpg','.aux','.log','.out','.toc','.fls','.fdb_latexmk'))
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(r).as_posix()+'\n' for p in files)
(r/'SOURCE_BUNDLE_MANIFEST.sha256').write_text(manifest)
with zipfile.ZipFile(r/'SGA5-zh-CN-source.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in files:z.write(p,'sga5/'+p.relative_to(r).as_posix())
 z.write(r/'SOURCE_BUNDLE_MANIFEST.sha256','sga5/SOURCE_BUNDLE_MANIFEST.sha256')
print('packaged',len(files)+1,'source files')
