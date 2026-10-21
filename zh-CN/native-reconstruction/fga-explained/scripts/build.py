#!/usr/bin/env python3
"""Build the native book with a frozen source census and mechanical PDF checks."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import time

import fitz

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'
JOB = 'FGA-explained-zh-CN'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_census():
    return {str(p.relative_to(ROOT)): digest(p) for p in sorted(ROOT.rglob('*.tex'))
            if 'build' not in p.relative_to(ROOT).parts}


def main():
    BUILD.mkdir(exist_ok=True)
    census = source_census()
    start = time.monotonic()
    for number in range(1, 4):
        print(f'XeLaTeX pass {number}/3', flush=True)
        with (BUILD / f'pass-{number}.txt').open('w') as output:
            subprocess.run(['xelatex', '-no-shell-escape', '-interaction=nonstopmode',
                            '-halt-on-error', '-recorder', '-output-directory=build',
                            f'-jobname={JOB}', 'main.tex'], cwd=ROOT,
                           stdout=output, stderr=subprocess.STDOUT, check=True)
    if census != source_census():
        raise RuntimeError('Source changed during build: rerun on a stable source tree.')
    log = (BUILD / f'{JOB}.log').read_text(errors='replace')
    pdf = BUILD / f'{JOB}.pdf'
    doc = fitz.open(pdf)
    outside = []
    for number, page in enumerate(doc, 1):
        for block in page.get_text('blocks'):
            if block[0] < -1 or block[1] < -1 or block[2] > page.rect.width + 1 or block[3] > page.rect.height + 1:
                outside.append({'page': number, 'bbox': list(block[:4])})
    report = {
        'built_at_utc': datetime.now(timezone.utc).isoformat(),
        'engine': subprocess.check_output(['xelatex', '--version'], text=True).splitlines()[0],
        'passes': 3,
        'shell_escape': False,
        'elapsed_seconds': round(time.monotonic() - start, 2),
        'source_tex_sha256': census,
        'pdf': f'{JOB}.pdf',
        'pdf_sha256': digest(pdf),
        'pages': len(doc),
        'missing_glyphs': len(re.findall(r'Missing character:', log)),
        'undefined_references': len(re.findall(r'(?:Reference .* undefined|There were undefined references)', log)),
        'overfull_boxes': len(re.findall(r'Overfull \\[hv]box', log)),
        'underfull_boxes': len(re.findall(r'Underfull \\[hv]box', log)),
        'font_warnings': re.findall(r'LaTeX Font Warning:[^\n]*', log),
        'latex_warnings': re.findall(r'(?:LaTeX|Package [^\n]+) Warning:[^\n]*', log),
        'text_outside_physical_pages': outside,
        'visual_review': 'Recorded separately; mechanical success is not proofreading.',
        'source_completeness': 'Recorded in PROGRESS.json and source-coverage.json; compilation does not establish it.',
    }
    (ROOT / 'evidence/build-review.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    shutil.copy2(pdf, ROOT / pdf.name)
    shutil.copy2(BUILD / f'{JOB}.log', ROOT / 'evidence/build.log')
    print(json.dumps({k: report[k] for k in ['pages', 'missing_glyphs', 'undefined_references', 'overfull_boxes', 'underfull_boxes']}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    main()
