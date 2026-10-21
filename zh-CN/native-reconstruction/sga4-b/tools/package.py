#!/usr/bin/env python3
"""Package the current native project and generate delivery checksums."""
from pathlib import Path
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]
archive = ROOT / 'SGA4-b-zh-CN-source.zip'
checksums = ROOT / 'SHA256SUMS'

def files():
    return sorted(p for p in ROOT.rglob('*') if p.is_file()
                  and not any(x in {'build', '__pycache__'} for x in p.relative_to(ROOT).parts)
                  and p not in {archive, checksums}
                  and p.suffix not in {'.aux', '.out', '.toc', '.gz'}
                  and not p.name.startswith('SGA4-native-'))

with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in files():
        if p.suffix == '.pdf':
            continue
        info = zipfile.ZipInfo(p.relative_to(ROOT).as_posix(), (2026, 10, 21, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = (0o100644 << 16)
        z.writestr(info, p.read_bytes())

all_files = sorted(files() + [archive])
checksums.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(ROOT).as_posix() + '\n' for p in all_files))
print(f'Packaged {archive.name}; {len(all_files)} delivery checksums.')
