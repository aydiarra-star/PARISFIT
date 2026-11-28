"""Local document audit only. Never executes source processing or accesses a recipient."""
from pathlib import Path
import json,hashlib,re,csv,subprocess
D=Path('docs/coach/phase21');E=Path('docs/coach/phase20/external');P=E.parent
REF='5eeb144aaa1c1f47f956776fa5a6dc1c1425fd9a'
def main():
 report={'reference':REF,'scope':'all seven files of phase20/external, internal source comparisons and reference Git blobs; no binary source processing','manifest':{},'equivalence':{},'findings':[]}
 manifest=json.loads((E/'manifest.json').read_text())
 for n,h in manifest.items():
  actual=hashlib.sha256((E/n).read_bytes()).hexdigest();assert actual==h;report['manifest'][n]=actual
 base='https://github.com/aydiarra-star/PARISFIT/blob/25ebee0ec3161ca5415d4961bd8d04ea4404af84/docs/coach/'
 for n in ['expert-preliminary-dossier.md','expert-questionnaire-final.md','evidence-and-claims-matrix.csv','expert-response-template.json']:
  s=(P/n).read_text();s=re.sub(r'\.\./(phase\d+/[^\s;)]+)',lambda m:base+m[1],s);s=s.replace('(external-sharing-checklist.md)','(README.md)').replace('(experimental-readiness-gates.md)','(README.md)')
  assert s==(E/n).read_text();report['equivalence'][n]='exact after documented URL/navigation substitutions'
 alltext='\n'.join(p.read_text() for p in E.iterdir())
 patterns={'token':r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_|Bearer\s+[A-Za-z0-9]+','signed_url':r'[?&](?:signature|token|access_token)=','private_key':r'-----BEGIN .*PRIVATE KEY-----','windows_profile':r'[A-Z]:\\Users\\','email':r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}'}
 report['sensitivePatternCounts']={k:len(re.findall(v,alltext)) for k,v in patterns.items()};assert not any(report['sensitivePatternCounts'].values())
 report['extensions']=sorted({p.suffix for p in E.iterdir()});assert set(report['extensions'])=={'.md','.csv','.json'}
 pinned=set(re.findall(re.escape(base)+r'([^\s;),"]+)',alltext));report['pinnedReferences']=sorted(pinned)
 for p in pinned:subprocess.check_output(['git','cat-file','-e','25ebee0:docs/coach/'+p])
 j=json.loads(Path('docs/coach/phase19/archive-probe.json').read_text());logs=[x for f in j['files'] for x in f.get('acquired',[]) if x['path'].endswith('opensim.log')];m=json.loads((E/'minimal-evidence.json').read_text());assert logs[0]['sha256']==m['originalLogSHA256'];t={x['line']:x['text'] for x in logs[0]['targetMentions']};assert 'AB01\\Squat\\1\\' in t[13369] and 'nr=2948 nc=43' in t[13555]
 report['minimalEvidence']='log hash and selected line contents agree; external text explicitly summarized, not verbatim'
 rows=list(csv.DictReader(Path('docs/coach/phase17/marker-anatomical-mapping.csv').read_text().splitlines()));assert len(rows)==57 and sum(x['anatomical_status']=='Confirmé' for x in rows)==44
 report['markerDefinitions']={'total':57,'confirmed':44,'plausible':13,'scope':'documentary definitions, not physical placement or centres'}
 for x in json.loads((E/'expert-response-template.json').read_text()):assert x['answer'] is None and x['justification'] is None
 paths=subprocess.check_output(['git','ls-tree','-r','--name-only',REF]).decode().splitlines();changed=[]
 for p in paths:
  if not Path(p).exists() or Path(p).read_bytes()!=subprocess.check_output(['git','show',REF+':'+p]):changed.append(p)
 assert not changed,changed
 report['preservation']={'referenceTrackedFiles':len(paths),'changed':changed,'rocketboxSHA256':hashlib.sha256(Path('assets/coach/coach.glb').read_bytes()).hexdigest()}
 report['limitations']=['Pattern scan not a comprehensive security certification','Linked internal evidence not bundled: access and minimization must be approved before sharing','Article license distinct from dataset: see submission-addendum.md','No recipient identity or access verified; none selected']
 (D/'audit-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print('PASS: external integrity, equivalence, references, log summaries, blank responses, pattern scan, preservation')
if __name__=='__main__':main()
