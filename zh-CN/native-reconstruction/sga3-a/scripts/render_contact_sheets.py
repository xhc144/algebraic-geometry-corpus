#!/usr/bin/env python3
"""Render the compiled PDF for genuine visual review; these images are QA only."""
from pathlib import Path
import argparse,fitz
from PIL import Image,ImageDraw
p=argparse.ArgumentParser();p.add_argument('pdf',type=Path);p.add_argument('out',type=Path);p.add_argument('--first',type=int,default=1);p.add_argument('--last',type=int);a=p.parse_args()
doc=fitz.open(a.pdf);a.out.mkdir(parents=True,exist_ok=True)
nums=list(range(a.first-1,min(a.last or len(doc),len(doc))))
for start in range(0,len(nums),20):
    sub=nums[start:start+20];sheet=Image.new('RGB',(1200,1440),'#ddd');draw=ImageDraw.Draw(sheet)
    for j,i in enumerate(sub):
        pix=doc[i].get_pixmap(matrix=fitz.Matrix(.36,.36),alpha=False)
        im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples);im.thumbnail((230,326))
        x=j%5*240+(240-im.width)//2;y=j//5*360+25;sheet.paste(im,(x,y));draw.text((x,y-18),str(i+1),fill='black')
    sheet.save(a.out/f'contact-{sub[0]+1}-{sub[-1]+1}.png')
print('Rendered',len(nums),'pages to',a.out)
