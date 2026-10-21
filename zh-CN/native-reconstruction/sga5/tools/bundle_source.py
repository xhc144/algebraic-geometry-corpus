#!/usr/bin/env python3
"""Package the independently buildable native source, excluding generated PDF/cache."""
from pathlib import Path
import hashlib,zipfile
r=Path(__file__).resolve().parents[1]
exclude={'SGA5-zh-CN-source.zip','SHA256SUMS','SOURCE_BUNDLE_MANIFEST.sha256','FINAL_ARCHIVE_VERIFICATION.json'}
files=sorted(p for p in r.rglob('*') if p.is_file() and '.build' not in p.relative_to(r).parts and p.name not in exclude and p.suffix.lower() not in ('.pdf','.png','.jpg','.aux','.log','.out','.toc','.fls','.fdb_latexmk'))
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(r).as_posix()+'\n' for p in files)
(r/'SOURCE_BUNDLE_MANIFEST.sha256').write_text(manifest)
with zipfile.ZipFile(r/'SGA5-zh-CN-source.zip','w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in files+[r/'SOURCE_BUNDLE_MANIFEST.sha256']:
  info=zipfile.ZipInfo.from_file(p,'sga5/'+p.relative_to(r).as_posix())
  info.create_system=3
  info.external_attr=(0o100755 if p.name=='build.sh' else 0o100644)<<16
  info.compress_type=zipfile.ZIP_DEFLATED
  z.writestr(info,p.read_bytes())
print('packaged',len(files)+1,'source files')
