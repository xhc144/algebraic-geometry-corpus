#!/usr/bin/env python3
"""Inspect a real compiled PDF; does not certify mathematical correctness."""
from pathlib import Path
import argparse, collections, hashlib, json
import fitz
p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,default=Path('build/main.pdf'));p.add_argument('--report',type=Path,default=Path('audit/PDF-CURRENT.json'));a=p.parse_args()
doc=fitz.open(a.pdf);names=doc.resolve_names();missing=collections.Counter();invalid=[];offpage=[];links=0
texts=[]
for i,page in enumerate(doc):
    texts.append(hashlib.sha256(page.get_text().encode()).hexdigest())
    for link in page.get_links():
        links+=1
        if link.get('nameddest') and link['nameddest'] not in names:missing[link['nameddest']]+=1
        elif 'page' in link and not 0<=link['page']<len(doc):invalid.append({'page':i+1,'link':str(link)})
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                r=fitz.Rect(span['bbox'])
                if span['text'].strip() and (r.x0 < -1 or r.y0 < -1 or r.x1 > page.rect.width+1 or r.y1 > page.rect.height+1):offpage.append({'page':i+1,'text':span['text'],'bbox':list(r)})
result={'pdf':str(a.pdf),'pdf_sha256':hashlib.sha256(a.pdf.read_bytes()).hexdigest(),'pages':len(doc),'image_object_occurrences':sum(len(p.get_images()) for p in doc),'named_destinations':len(names),'sga_named_destinations':sum(k.startswith('sga3:') for k in names),'link_annotations':links,'missing_pdf_named_destinations':dict(missing),'invalid_internal_page_targets':invalid,'off_page_text_spans':offpage,'bookmarks':doc.get_toc(),'bookmark_key_leaks':[t for _,t,_ in doc.get_toc() if 'sga3:' in t or 'SGARef' in t],'per_page_text_sha256':texts,'limits':'Destination existence is checked, not semantic correctness of source cross-references. Bounding boxes and image counts do not replace rendered-page inspection or mathematical proofreading.'}
a.report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['pages','image_object_occurrences','named_destinations','link_annotations','missing_pdf_named_destinations','invalid_internal_page_targets','off_page_text_spans','bookmark_key_leaks']},ensure_ascii=False))
