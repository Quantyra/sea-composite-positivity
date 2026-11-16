"""Run the single preregistered diagnostic with a 60-second process cap."""
import datetime,json,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
row={'start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'cap_seconds':60,'command':'python -B tools/check_exact.py'}
try:
 result=subprocess.run([sys.executable,'-B',str(ROOT/'tools/check_exact.py')],cwd=ROOT,capture_output=True,text=True,encoding='utf-8',timeout=60)
 row.update(exit_code=result.returncode,stdout=result.stdout,stderr=result.stderr,within_cap=True)
except subprocess.TimeoutExpired as e: row.update(exit_code=None,within_cap=False,error=str(e))
row['wall_seconds']=time.perf_counter()-start
(ROOT/'verification/exact-process.json').write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8')
print(json.dumps(row));sys.exit(0 if row.get('exit_code')==0 else 1)
