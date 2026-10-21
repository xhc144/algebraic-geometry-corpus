#!/usr/bin/env python3
"""Package only this project's native source and audit dependencies."""
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parent
out=root/'SGA6-zh-CN-source.zip'
exclude={'build','__pycache__','.git'}
skip={'SGA6-zh-CN-source.zip','audits/FINAL_ARTIFACTS.json'}
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(root.rglob('*')):
  if not p.is_file():continue
  rel=p.relative_to(root)
  if any(x in exclude for x in rel.parts) or rel.as_posix() in skip:continue
  z.write(p,'SGA6-zh-CN/'+rel.as_posix())
print(out.name,out.stat().st_size)
