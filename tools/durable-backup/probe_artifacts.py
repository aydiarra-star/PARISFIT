"""Inbound read-only probe of three artifacts, no upload. Never log signed redirect URLs."""
import json,subprocess,hashlib,zipfile
from pathlib import Path
D=Path('docs/coach/phase26');B=Path('.cache/phase26-work/artifacts');B.mkdir(parents=True,exist_ok=True)
arts=json.loads((D/'actions-metadata.json').read_text())['artifacts'];chosen=[]
for name in ['phase19-passive-archive-metadata','phase14-model-qualification','coach-browser-review']:
 chosen.append(next(a for a in arts if a['name']==name and not a['expired']))
results=[]
for a in chosen:
 p=B/(str(a['id'])+'.zip');assert not p.exists();r={'id':a['id'],'name':a['name'],'status':'unrecovered'}
 try:
  with p.open('xb') as f:proc=subprocess.run(['gh','api',f"repos/aydiarra-star/PARISFIT/actions/artifacts/{a['id']}/zip"],stdout=f,stderr=subprocess.PIPE,timeout=25)
  r['exitCode']=proc.returncode
  if proc.returncode==0 and zipfile.is_zipfile(p):
   with zipfile.ZipFile(p) as z:
    assert z.testzip() is None
    r.update(status='recovered-CRC-verified',files=len(z.infolist()),members=z.namelist(),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,path=str(p))
  else:r['failure']='Download did not return a valid ZIP; signed URL/error details withheld.'
 except subprocess.TimeoutExpired:r['failure']='Timeout 25s; partial file retained, not a backup.'
 r['localBytes']=p.stat().st_size;results.append(r)
(D/'artifact-retrieval.json').write_text(json.dumps({'scope':'three representative downloads; no claims for untested artifacts','results':results,'metadataOnlyIds':[a['id'] for a in arts if a['id'] not in {r['id'] for r in results if r['status']=='recovered-CRC-verified'}]},indent=2)+'\n');print(json.dumps(results,indent=2))
