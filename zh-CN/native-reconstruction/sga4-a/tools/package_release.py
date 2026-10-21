#!/usr/bin/env python3
"""Package this independently compilable translation, without original scans."""
from pathlib import Path
import hashlib
import json
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def eligible(path):
    rel = path.relative_to(ROOT)
    return (path.is_file() and not any(x in {'build', '__pycache__', '.git'} for x in rel.parts)
            and path.suffix not in {'.pdf', '.zip', '.aux', '.toc', '.out', '.log', '.pyc'}
            and path.name not in {'DELIVERABLES.json', 'SOURCE_FILE_MANIFEST.json'})


def main():
    pdf = ROOT / 'sga4-a.pdf'
    shutil.copyfile(ROOT / 'build/main.pdf', pdf)
    files = sorted(p for p in ROOT.rglob('*') if eligible(p))
    manifest = [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
                 'sha256': digest(p)} for p in files]
    manifest_path = ROOT / 'audit/SOURCE_FILE_MANIFEST.json'
    manifest_path.write_text(json.dumps({'files': manifest, 'excludes':
        'This manifest itself, PDFs, ZIPs, generated build/cache files and DELIVERABLES.json.'},
        ensure_ascii=False, indent=2) + '\n')
    files.append(manifest_path)
    archive_path = ROOT / 'sga4-a-source.zip'
    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            archive.write(path, str(path.relative_to(ROOT)))
    # Kept outside the ZIP to avoid a self-referential archive hash.
    data = {'scope': 'I II III IV V Vbis VI VII VIII IX, both prefaces and tome I/II indexes',
            'artifacts': [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
                           'sha256': digest(p)} for p in [pdf, archive_path]],
            'source_zip_members': len(files)}
    (ROOT / 'audit/DELIVERABLES.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
