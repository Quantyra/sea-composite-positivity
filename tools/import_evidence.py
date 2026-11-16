"""Preserve selected S279 evidence as immutable Git blob bytes."""
import hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'quantyra-quantum-complexity-s288'
COMMIT='7b50583bb96679d6213c6e47b25f234d3ad30fb2'
PATHS=['proofs/e004-s279-sea-composite-audit-2026-11-15.md','scripts/s279_check_sea_generator.cjs','artifacts/s279-source-receipt.json','artifacts/s279-process-receipt.json','artifacts/s279-preregistration.md','artifacts/s279-exact-check.json','artifacts/s279-check.stdout.txt','artifacts/s279-check.stderr.txt']
rows=[]
for original in PATHS:
 data=subprocess.check_output(['git','-C',str(SOURCE),'show',COMMIT+':'+original])
 dest=ROOT/'evidence/s279'/original;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
 rows.append({'original_path':original,'file':dest.relative_to(ROOT).as_posix(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
pdf='artifacts/s279-sources/ray-beretta-2301.11548v5.pdf'
data=subprocess.check_output(['git','-C',str(SOURCE),'show',COMMIT+':'+pdf]);(ROOT/'sources/ray-beretta-v5.pdf').write_bytes(data)
rows.append({'original_path':pdf,'file':'sources/ray-beretta-v5.pdf','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'tracked':False})
(ROOT/'evidence/provenance.json').write_text(json.dumps({'source_repository':'https://github.com/Quantyra/quantyra-quantum-complexity','source_commit':COMMIT,'files':rows},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'imported':len(rows),'source_commit':COMMIT}))
