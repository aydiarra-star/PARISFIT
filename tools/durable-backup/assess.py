"""Read-only service metadata; save no credentials, private URLs or unrelated repository names."""
import subprocess,json,shutil
from pathlib import Path
D=Path('docs/coach/phase26');D.mkdir(exist_ok=True)
def pages(endpoint):
 s=subprocess.check_output(['gh','api','--paginate',endpoint]).decode();dec=json.JSONDecoder();out=[]
 while s.strip():
  value,n=dec.raw_decode(s.lstrip());out.append(value);s=s.lstrip()[n:]
 return out
def gh(endpoint):return pages(endpoint)[0]
u=gh('user');flat=[r for page in pages('user/repos?per_page=100&affiliation=owner,collaborator,organization_member') for r in page]
d={'account':u['login'],'plan':u.get('plan',{}).get('name','not exposed'),'visibleRepositoryCount':len(flat),'visiblePrivateRepositoryCount':sum(r['private'] for r in flat),'parisfit':[{k:r.get(k) for k in ['full_name','private','permissions','has_pages']} for r in flat if r['full_name']=='aydiarra-star/PARISFIT'],'scopeLimit':'Only repositories visible to this integration; no proof that other private repositories do not exist. No unrelated repository content inspected.','connectedApps':'none per session; GitHub connector unsupported; gh CLI read access works','diskBytesFree':shutil.disk_usage('.').free,'durableDestinationVerified':False}
(D/'destination-evidence.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d,indent=2))
a=pages('repos/aydiarra-star/PARISFIT/actions/artifacts?per_page=100');arts=[x for p in a for x in p['artifacts']]
(D/'actions-metadata.json').write_text(json.dumps({'total_count':a[0]['total_count'],'artifacts':[{k:x[k] for k in ['id','name','size_in_bytes','expired','created_at','expires_at']} for x in arts]},indent=2)+'\n');print('artifacts',len(arts))
