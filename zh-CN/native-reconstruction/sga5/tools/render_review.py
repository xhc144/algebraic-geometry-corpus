#!/usr/bin/env python3
from pathlib import Path
import fitz,json
from PIL import Image,ImageOps,ImageDraw
r=Path(__file__).resolve().parents[1]
pdf=fitz.open(r/'SGA5-zh-CN.pdf');tmp=Path('/tmp/sga5-render-review');tmp.mkdir(exist_ok=True)
thumbs=[];boxes=[];images=0
for i,p in enumerate(pdf):
 images+=len(p.get_images(full=True))
 pix=p.get_pixmap(matrix=fitz.Matrix(.65,.65),alpha=False)
 path=tmp/f'page-{i+1:03d}.png';pix.save(path)
 img=Image.open(path).convert('RGB');img.thumbnail((300,430))
 cell=Image.new('RGB',(320,460),'#ddd');cell.paste(img,((320-img.width)//2,20));ImageDraw.Draw(cell).text((10,442),f'PDF {i+1}',fill='black');thumbs.append(cell)
 for b in p.get_text('blocks'):
  if b[0]<-1 or b[1]<-1 or b[2]>p.rect.width+1 or b[3]>p.rect.height+1:boxes.append({'page':i+1,'bbox':list(b[:4])})
sheets=[]
for start in range(0,len(thumbs),24):
 sheet=Image.new('RGB',(320*6,460*4),'white')
 for j,im in enumerate(thumbs[start:start+24]):sheet.paste(im,((j%6)*320,(j//6)*460))
 path=tmp/f'contact-{start+1:03d}-{min(start+24,len(thumbs)):03d}.jpg';sheet.save(path,quality=90);sheets.append(str(path))
(r/'qa/render-inventory.json').write_text(json.dumps({'pages':len(pdf),'raster_image_objects':images,'out_of_page_text_blocks':boxes,'rendered_all_pages':True,'contact_sheets':sheets,'render_location':'/tmp/sga5-render-review (temporary QA views, not source dependencies)','visual_inspection':'pending actual opening of contact sheets and selected full pages'},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':len(pdf),'raster_images':images,'outside_page_blocks':len(boxes),'contact_sheets':sheets},indent=2))
