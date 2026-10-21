#!/usr/bin/env python3
"""Make a deterministic, self-contained source ZIP and verify its file manifest."""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'FGA-explained-zh-CN.pdf'
ZIP = ROOT / 'FGA-explained-zh-CN-source.zip'
MANIFEST = ROOT / 'evidence/source-package-manifest.json'
PREFIX = 'fga-explained/'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    files = [p for p in sorted(ROOT.rglob('*')) if p.is_file()
             and 'build' not in p.relative_to(ROOT).parts
             and '__pycache__' not in p.relative_to(ROOT).parts
             and p not in {PDF, ZIP, MANIFEST, ROOT / 'SHA256SUMS'}]
    payload = {str(p.relative_to(ROOT)): p.read_bytes() for p in files}
    manifest = {
        'format': 1,
        'archive_prefix': PREFIX,
        'excluded': ['build/', PDF.name, ZIP.name, 'SHA256SUMS'],
        'self_hash': 'The manifest omits its own hash; the ZIP hash is in external SHA256SUMS.',
        'files': {name: {'sha256': digest(data), 'bytes': len(data)}
                  for name, data in payload.items()},
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    payload[str(MANIFEST.relative_to(ROOT))] = MANIFEST.read_bytes()
    with zipfile.ZipFile(ZIP, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(PREFIX + name, date_time=(2026, 10, 21, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 << 16)
            archive.writestr(info, data, compresslevel=9)
    with zipfile.ZipFile(ZIP) as archive:
        assert set(archive.namelist()) == {PREFIX + name for name in payload}
        for name, data in payload.items():
            assert digest(archive.read(PREFIX + name)) == digest(data), name
    (ROOT / 'SHA256SUMS').write_text(''.join(
        f'{digest(p.read_bytes())}  {p.name}\n' for p in [PDF, ZIP]))
    print(json.dumps({'zip': ZIP.name, 'files': len(payload),
                      'bytes': ZIP.stat().st_size, 'sha256': digest(ZIP.read_bytes())}))


if __name__ == '__main__':
    main()
