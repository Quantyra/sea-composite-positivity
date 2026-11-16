"""Verify frozen package receipts and evidence; never reruns mathematics or publishes."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def require(ok,msg):
    if not ok:raise SystemExit(msg)
build=read('verification/build.json')
require(build['source_sha256']==sha(ROOT/'manuscript/main.tex'),'LaTeX/build mismatch')
require(build['pdf_sha256']==sha(ROOT/'manuscript/main.pdf'),'PDF/build mismatch')
require(not build['final_log_diagnostics'],'Build diagnostics unresolved')
check=read('verification/exact-check.json');proc=read('verification/exact-process.json')
require(check['status']=='pass' and check['assertions']==122,'Exact receipt mismatch')
require(check['script_sha256']==sha(ROOT/'tools/check_exact.py'),'Check script changed')
require(proc['exit_code']==0 and proc['within_cap'] and proc['wall_seconds']<60,'Process failed/cap exceeded')
require(json.loads(proc['stdout'])==check,'Check and process receipts disagree')
provenance=read('evidence/provenance.json');verified=0
for entry in provenance['files']:
    p=ROOT/entry['file']
    if entry.get('tracked',True) or p.exists():
        require(p.exists() and sha(p)==entry['sha256'],'Provenance mismatch '+entry['file']);verified+=1
old=read('evidence/s279/artifacts/s279-process-receipt.json')
require(old['exitCode'] is None,'Original missing-exit-code caveat changed')
required=['README.md','CLAIMS.md','SOURCES.md','LICENSE','CITATION.cff','.zenodo.json','formal/CERTIFICATION-PLAN.md','reviews/INTERNAL-REVIEW.md']
for name in required:require((ROOT/name).is_file(),'Missing '+name)
metadata=read('.zenodo.json')
require(metadata['creators'][0]['orcid']=='0009-0002-9123-7435','Metadata mismatch')
require('doi' not in metadata,'Unassigned DOI unexpectedly present')
missing=[]
for path in [ROOT/name for name in required if name.endswith('.md')]:
    for link in re.findall(r'\]\(([^)]+)\)',path.read_text(encoding='utf-8')):
        if '://' in link or link.startswith('#'):continue
        target=(path.parent/link.split('#')[0])
        if not target.exists():missing.append(str(path.relative_to(ROOT))+': '+link)
require(not missing,'Broken local links: '+str(missing))
print(json.dumps({'status':'pass','source_sha256':build['source_sha256'],'pdf_sha256':build['pdf_sha256'],'pages':build['pages'],'preserved_evidence_files_checked':verified,'diagnostic_assertions':check['assertions'],'formal_certification':False,'scope':'package, hashes, receipts and links; not an additional mathematical experiment'}))
