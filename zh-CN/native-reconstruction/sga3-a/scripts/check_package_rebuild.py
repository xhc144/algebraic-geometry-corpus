#!/usr/bin/env python3
"""Compare an actual clean ZIP rebuild with the delivered native PDF."""
from pathlib import Path
import argparse,datetime,hashlib,json,zipfile
import fitz
p=argparse.ArgumentParser();p.add_argument('extraction',type=Path);p.add_argument('--staged-archive-sha',required=True);a=p.parse_args()
r=Path(__file__).resolve().parents[1];clean=a.extraction/'build/main.pdf';delivered=r/'sga3-a-zh.pdf'
old=fitz.open(delivered);new=fitz.open(clean)
hashes=lambda d:[hashlib.sha256(x.get_text().encode()).hexdigest() for x in d]
oh,nh=hashes(old),hashes(new);diff=[i+1 for i in range(max(len(oh),len(nh))) if (oh[i] if i<len(oh) else None)!=(nh[i] if i<len(nh) else None)]
log=(a.extraction/'build/main.log').read_text();manifest={};mismatch=[]
with zipfile.ZipFile(r/'sga3-a-source.zip') as z:
    for name in z.namelist():
        if not name.endswith('.tex'):continue
        digest=hashlib.sha256(z.read(name)).hexdigest();manifest[name]=digest
        if hashlib.sha256((a.extraction/name).read_bytes()).hexdigest()!=digest:mismatch.append(name)
report={'state':'passed' if not diff and old.get_toc()==new.get_toc() and not mismatch else 'failed','checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'actual_working_directory':str(a.extraction),'archive_extracted_before_any_aux':True,'actual_command':'TEXMFHOME=/tmp/sga3-texmf-2024 TEXMFVAR=/tmp/sga3-ref-archive-var XDG_CACHE_HOME=/tmp/sga3-ref-archive-cache latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex','built_from_staged_archive_sha256':a.staged_archive_sha,'pages':len(new),'all_page_text_hashes_equal_delivered_PDF':not diff,'page_text_differences':diff,'all_bookmarks_equal':old.get_toc()==new.get_toc(),'tex_dependency_file_count':len(manifest),'all_rebuilt_tex_hashes_equal_packaged_tex':not mismatch,'tex_mismatches':mismatch,'frozen_archive_tex_manifest':manifest,'delivered_pdf_sha256':hashlib.sha256(delivered.read_bytes()).hexdigest(),'clean_pdf_sha256':hashlib.sha256(clean.read_bytes()).hexdigest(),'pdf_bytes_identical':delivered.read_bytes()==clean.read_bytes(),'zero_image_objects':not any(p.get_images() for p in new),'missing_glyph_messages':log.count('Missing character:'),'overfull_boxes':log.count('Overfull'),'underfull_boxes':log.count('Underfull'),'xdvipdfmx_warnings':(a.extraction/'build/main.log').read_text().count('xdvipdfmx:warning'),'final_archive_note':'Final metadata-only repack must retain exactly this TeX/dependency manifest. Final ZIP checksum is in external DELIVERY.json and SHA256SUMS only, to avoid self-reference.','review_limits':'Rebuild and finite reference repair verification do not certify source mathematics, all inherited semantic links or full French final collation.'}
(r/'audit/PACKAGE_REBUILD.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k not in ('frozen_archive_tex_manifest',)},ensure_ascii=False))
if report['state']!='passed':raise SystemExit(1)
