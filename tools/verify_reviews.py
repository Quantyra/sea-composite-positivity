"""Check review-source bindings and retained reports; no model or mathematics runs."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check_reviews():
    summary=json.loads((R/'reviews/REVIEW-SUMMARY.json').read_text(encoding='utf-8'))
    assert summary['status']=='COMPLETE_WITH_DISPOSITIONS'
    assert summary['source_sha256']==sha(R/'manuscript/main.tex')
    assert summary['unresolved_essential_findings']==[]
    assert {x['provider'] for x in summary['selected_reviews']}=={'claude','grok','agy'}
    for row in summary['selected_reviews']:
        assert row['completion_verified'] and row['status']=='TERMINAL' and row['exit_code']==0
        assert row['source_sha256']==summary['source_sha256']
        assert sha(R/row['report'])==row['report_sha256']
        packet=R/'reviews/three-lens-2026-11-16'/f"{row['phase']}-{row['provider']}-packet.txt"
        assert sha(packet)==row['input_packet_sha256']
    return {'status':'pass','providers':['claude','grok','agy'],'source_sha256':summary['source_sha256'],'scope':'AI review receipts, not human peer review or formal certification'}
if __name__=='__main__':print(json.dumps(check_reviews()))
