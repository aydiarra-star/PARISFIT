import subprocess,json,base64,zlib,hashlib,sys
from pathlib import Path
run,check,commit=sys.argv[1:];out=Path('docs/coach/phase11');groups={}
annotations=json.loads(subprocess.check_output(['gh','api',f'repos/aydiarra-star/PARISFIT/check-runs/{check}/annotations?per_page=100']))
for a in annotations:
 t=a.get('title','')
 if not t.startswith('phase11-') or t.startswith('phase11-log-'):continue
 name,i=t[len('phase11-'):].rsplit('-',1)
 if not i.isdigit():continue
 groups.setdefault(name,{})[int(i)]=a['message'].strip()
evidence={'run':run,'check':check,'commit':commit,'method':'zlib/base64 JSON annotations, SHA256 preserved; binary videos not retrieved','reports':{}}
for name,parts in groups.items():
 assert sorted(parts)==list(range(len(parts)))
 raw=zlib.decompress(base64.b64decode(''.join(parts[i] for i in sorted(parts)),validate=True));json.loads(raw);(out/name).write_bytes(raw);evidence['reports'][name]=hashlib.sha256(raw).hexdigest()
assert set(groups)=={'A_report.json','B_report.json','C_report.json','anatomy-summary.json','three-report.json','video-report.json'},groups.keys()
(out/'evidence.json').write_text(json.dumps(evidence,indent=2)+'\n')
