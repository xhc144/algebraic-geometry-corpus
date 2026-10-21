#!/usr/bin/env python3
"""Local OCR of the actual source scan. Output is UNCORRECTED, never translation."""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile

import fitz

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parents[2] / 'FGA/FGA-Explained-Fantechi-AMS-2005.pdf'
OUT = ROOT / 'evidence/ocr-uncorrected'


def page_ocr(number):
    target = OUT / f'pdf-{number:03d}.txt'
    if target.exists():
        return number, 'cached'
    with fitz.open(SOURCE) as doc:
        pix = doc[number - 1].get_pixmap(dpi=220, colorspace=fitz.csGRAY)
    with tempfile.TemporaryDirectory(prefix='fga-ocr-') as directory:
        scan = Path(directory) / 'page.png'
        pix.save(scan)
        env = dict(os.environ, OMP_THREAD_LIMIT='1')
        result = subprocess.run(['tesseract', str(scan), 'stdout', '-l', 'eng', '--psm', '3'],
                                check=True, capture_output=True, env=env)
    target.write_bytes(result.stdout)
    return number, 'ocr'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--first', type=int, default=1)
    parser.add_argument('--last', type=int, default=354)
    parser.add_argument('--workers', type=int, default=6)
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    with concurrent.futures.ProcessPoolExecutor(max_workers=args.workers) as pool:
        for number, status in pool.map(page_ocr, range(args.first, args.last + 1)):
            print(f'PDF {number}: {status}', flush=True)
    manifest = [{'pdf_page': int(p.stem.split('-')[1]), 'file': p.name,
                 'bytes': p.stat().st_size, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                for p in sorted(OUT.glob('pdf-*.txt'))]
    (OUT / 'MANIFEST.json').write_text(json.dumps({
        'source': str(SOURCE.relative_to(ROOT.parents[2])),
        'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'engine': 'tesseract 5, eng, psm 3, 220 dpi grayscale',
        'status': 'UNCORRECTED OCR: mathematical notation must be checked against scan',
        'pages': manifest}, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
