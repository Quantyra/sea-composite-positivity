"""Build/render the manuscript; does not run research or publish anything."""
import argparse, datetime, hashlib, json, os, re, shutil, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--tectonic',default='tectonic');p.add_argument('--render',action='store_true')
    args=p.parse_args()
    version=subprocess.check_output([args.tectonic,'--version'],text=True).strip()
    if version!='Tectonic 0.17.0': raise SystemExit(f'Expected Tectonic 0.17.0; got {version}')
    build=ROOT/'.build';build.mkdir(exist_ok=True)
    epoch=int(datetime.datetime(2026,11,16,tzinfo=datetime.timezone.utc).timestamp())
    env=dict(os.environ,SOURCE_DATE_EPOCH=str(epoch),TZ='UTC')
    result=subprocess.run([args.tectonic,'--keep-logs','--outdir',str(build),'main.tex'],cwd=ROOT/'manuscript',env=env,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=300)
    (build/'compiler-output.txt').write_text(result.stdout+result.stderr,encoding='utf-8')
    if result.returncode: raise SystemExit(result.stdout+result.stderr)
    log=(build/'main.log').read_text(encoding='utf-8',errors='replace')
    diagnostics=re.findall(r'^.*(?:Overfull|Underfull|undefined|Missing character|LaTeX Warning|Package .+ Warning).*$',log,flags=re.MULTILINE)
    if diagnostics: raise SystemExit('\n'.join(diagnostics))
    shutil.copyfile(build/'main.pdf',ROOT/'manuscript/main.pdf')
    import pymupdf
    doc=pymupdf.open(ROOT/'manuscript/main.pdf')
    if any(not page.get_text().strip() for page in doc): raise SystemExit('Empty page')
    if args.render:
        renders=build/'renders';renders.mkdir(exist_ok=True)
        for n,page in enumerate(doc,1): page.get_pixmap(dpi=100).save(renders/f'page-{n:02}.png')
    receipt={'scope':'Document build/layout only, not mathematical certification','compiler':version,'pymupdf_version':pymupdf.VersionBind,'source_date_epoch':epoch,'source_sha256':sha(ROOT/'manuscript/main.tex'),'pdf_sha256':sha(ROOT/'manuscript/main.pdf'),'pages':len(doc),'final_log_diagnostics':diagnostics,'environment_messages':[line for line in result.stderr.splitlines() if 'Fontconfig' in line],'page_text_lengths':[len(page.get_text()) for page in doc]}
    (ROOT/'verification/build.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(receipt))
if __name__=='__main__':main()
