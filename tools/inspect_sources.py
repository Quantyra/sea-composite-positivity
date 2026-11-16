"""Extract and render pinned primary PDFs for source correspondence (not proof checking)."""
from pathlib import Path
import hashlib,json,pymupdf
ROOT=Path(__file__).resolve().parents[1]
rows=[]
for name in ['ray-beretta-publisher.pdf','ray-beretta-v5.pdf']:
 file=ROOT/'sources'/name;doc=pymupdf.open(file)
 (ROOT/'.build'/name.replace('.pdf','.txt')).write_text('\n'.join(p.get_text() for p in doc),encoding='utf-8')
 selected=[]
 for i,page in enumerate(doc):
  targets=[x for x in ['(19)','(39)','(59)','(61)','(62)'] if x in page.get_text()]
  if targets:
   page.get_pixmap(dpi=105).save(ROOT/'.build'/f'{file.stem}-page-{i+1:02}.png')
   selected.append({'page':i+1,'targets':targets})
 rows.append({'file':'sources/'+name,'sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'pages':len(doc),'equation_pages':selected})
print(json.dumps(rows,indent=2))
(ROOT/'verification/source-pages.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
