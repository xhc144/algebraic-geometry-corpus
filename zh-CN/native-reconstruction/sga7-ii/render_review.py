from pathlib import Path
from PIL import Image,ImageDraw
import fitz,json
root=Path(__file__).resolve().parent
# Discard obsolete generated page images so stale repagination cannot be mistaken for current evidence.
import re
for folder in ['build/render','build/contact']:
 (root/folder).mkdir(parents=True,exist_ok=True)
for old in (root/'build/render').glob('*.png'):
 if re.fullmatch(r'(?:high-)?\d{3}\.png',old.name):old.unlink()
for old in (root/'build/contact').glob('sheet-*.jpg'):old.unlink()
doc=fitz.open(root/'SGA7-II-zh-CN.pdf')
print('page count',len(doc),'page labels',doc.get_page_labels())
print('chapter bookmarks', [x for x in doc.get_toc() if x[1].startswith('第 ')])
for i,page in enumerate(doc):
 pix=page.get_pixmap(matrix=fitz.Matrix(.7,.7),alpha=False)
 pix.save(root/'build/render'/f'{i+1:03}.png')
for start in range(0,len(doc),25):
 sheet=Image.new('RGB',(1000,1510),'#dddddd');draw=ImageDraw.Draw(sheet)
 for j in range(25):
  i=start+j
  if i>=len(doc):break
  im=Image.open(root/'build/render'/f'{i+1:03}.png');im.thumbnail((188,277))
  x=(j%5)*200+6;y=(j//5)*302+21
  sheet.paste(im,(x,y));draw.text((x,y-15),f'PDF {i+1}',fill='black')
 sheet.save(root/'build/contact'/f'sheet-{start//25+1:02}.jpg',quality=88)
chapters=[x for x in doc.get_toc() if x[1].startswith('第 ')]
selected=sorted(set([1,2,3,4,5,17,18,len(doc)]+[x[2] for x in chapters]))
for page in selected:
 doc[page-1].get_pixmap(matrix=fitz.Matrix(1.5,1.5),alpha=False).save(root/'build/render'/f'high-{page:03}.png')
(root/'build/render/manifest.json').write_text(json.dumps({'pdf_sha256':__import__('hashlib').sha256((root/'SGA7-II-zh-CN.pdf').read_bytes()).hexdigest(),'pages_rendered':len(doc),'contact_sheets':(len(doc)+24)//25,'high_resolution_pdf_pages':selected,'chapters':chapters},ensure_ascii=False,indent=2))
