"""Record a hash inventory of staged package paths; no publication or math run."""
import datetime,hashlib,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
run=subprocess.run([sys.executable,'-B','tools/verify_package.py'],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',timeout=30)
if run.returncode:raise SystemExit(run.stdout+run.stderr)
paths=subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode('utf-8').split('\0')
rows=[]
for name in paths:
    if not name or name=='verification/package.json':continue
    p=ROOT/name;data=p.read_bytes()
    rows.append({'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
receipt={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Package inventory and verification, not publication or formal acceptance','verification':json.loads(run.stdout),'review':'same-agent internal review only','visual_pages_inspected':[1,2,3,4,5],'manifest_excludes_itself':True,'files':rows}
(ROOT/'verification/package.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'pass','files':len(rows),'verification':receipt['verification']}))
