"""Retrieve primary-source snapshots; failures are recorded, never replaced silently."""
import concurrent.futures, datetime, hashlib, json, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ITEMS={
 'ray-beretta-publisher.pdf':'https://mdpi-res.com/d_attachment/entropy/entropy-27-01018/article_deploy/entropy-27-01018.pdf',
 'publisher-version-notes.html':'https://www.mdpi.com/1099-4300/27/10/1018/notes',
 'ray-beretta-v5.html':'https://arxiv.org/html/2301.11548v5',
}
def fetch(item):
 name,url=item
 row={'file':'sources/'+name,'url':url,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (research source verification)'})
  with urllib.request.urlopen(req,timeout=45) as response:
   data=response.read(20_000_001); row['final_url']=response.url; row['http_status']=response.status
  if len(data)>20_000_000: raise ValueError('source exceeds 20 MB cap')
  if name.endswith('.pdf') and not data.startswith(b'%PDF'): raise ValueError('not a PDF')
  (ROOT/'sources'/name).write_bytes(data)
  row.update(status='retrieved',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as e: row.update(status='failed',error=str(e))
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: rows=list(pool.map(fetch,ITEMS.items()))
(ROOT/'verification/source-downloads.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print(json.dumps(rows,indent=2))
