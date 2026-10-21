#!/usr/bin/env python3
"""Render the compiled Chinese PDF for internal visual review. Requires PyMuPDF/Pillow."""
from pathlib import Path
import argparse,json,hashlib
import fitz
from PIL import Image,ImageDraw
p=argparse.ArgumentParser();p.add_argument('--pdf',type=Path,default=Path('SGA4-b-zh-CN.pdf'));p.add_argument('--dest',type=Path,required=True);a=p.parse_args();a.dest.mkdir(parents=True,exist_ok=True)
d=fitz.open(a.pdf);bounds=[];sizes=[];pages=[]
for i,page in enumerate(d):
 pix=page.get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False);f=a.dest/f'page-{i+1:03}.png';pix.save(f);pages.append(f);sizes.append([pix.width,pix.height])
 for block in page.get_text('dict')['blocks']:
  for line in block.get('lines',[]):
   for span in line.get('spans',[]):
    x0,y0,x1,y1=span['bbox']
    if min(x0,y0)<-1 or x1>page.rect.width+1 or y1>page.rect.height+1:bounds.append({'pdf_page':i+1,'bbox':span['bbox'],'text':span['text']})
for first in range(0,len(pages),16):
 canvas=Image.new('RGB',(1280,4*473),'#dddddd');draw=ImageDraw.Draw(canvas)
 for j,f in enumerate(pages[first:first+16]):
  im=Image.open(f);im.thumbnail((312,444));x=(j%4)*320+4;y=(j//4)*473+24;canvas.paste(im,(x,y));draw.text((x,y-18),f'PDF page {first+j+1}',fill='black')
 canvas.save(a.dest/f'sheet-{first+1:03}-{min(first+16,len(pages)):03}.jpg',quality=88)
result={'pdf_sha256':hashlib.sha256(a.pdf.read_bytes()).hexdigest(),'rendered_pages':len(d),'page_pixel_dimensions':sizes,'text_outside_physical_page':bounds,'contact_sheets':19,'note':'Rendering and bounds inspection are mechanical; actual viewed sheets/pages are recorded separately.'}
(a.dest/'RENDER_REPORT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'rendered_pages':len(d),'outside_page_text_spans':len(bounds)}))
