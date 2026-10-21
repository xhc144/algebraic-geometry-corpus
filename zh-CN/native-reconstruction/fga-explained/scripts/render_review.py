#!/usr/bin/env python3
"""Render every compiled page and create numbered contact sheets for visual review."""
import hashlib
import json
from pathlib import Path
import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'FGA-explained-zh-CN.pdf'
OUT = ROOT / 'build/rendered'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    pages = []
    for n, page in enumerate(doc, 1):
        target = OUT / f'page-{n:03d}.png'
        page.get_pixmap(dpi=110).save(target)
        pages.append({'page': n, 'file': target.name,
                      'sha256': hashlib.sha256(target.read_bytes()).hexdigest()})
    sheets = []
    for first in range(1, len(doc) + 1, 12):
        sheet = Image.new('RGB', (1040, 1200), '#ddd')
        for j, n in enumerate(range(first, min(first + 12, len(doc) + 1))):
            with Image.open(OUT / f'page-{n:03d}.png') as source:
                source.thumbnail((250, 370))
                tile = Image.new('RGB', (260, 400), 'white')
                tile.paste(source, ((260 - source.width) // 2, 24))
            ImageDraw.Draw(tile).text((5, 4), f'PDF {n}', fill='black')
            sheet.paste(tile, ((j % 4) * 260, (j // 4) * 400))
        target = OUT / f'contact-{first:03d}.jpg'
        sheet.save(target, quality=90)
        sheets.append({'first': first, 'last': min(first + 11, len(doc)), 'file': target.name})
    (ROOT / 'evidence/render-manifest.json').write_text(json.dumps({
        'pdf_sha256': hashlib.sha256(PDF.read_bytes()).hexdigest(),
        'dpi': 110, 'pages': pages, 'contact_sheets': sheets,
        'status': 'rendered; viewing must be documented separately'
    }, indent=2) + '\n')
    print(f'Rendered {len(doc)} pages, {len(sheets)} contact sheets', flush=True)


if __name__ == '__main__':
    main()
