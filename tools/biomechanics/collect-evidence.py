"""Collect public JSON evidence via GitHub API annotations when artifact download is unavailable."""
import subprocess,json,base64,hashlib,sys
from pathlib import Path
run,check,commit=sys.argv[1:];out=Path('docs/coach/phase10');groups={}
annotations=json.loads(subprocess.check_output(['gh','api',f'repos/aydiarra-star/PARISFIT/check-runs/{check}/annotations?per_page=100']))
for a in annotations:
 t=a.get('title','')
 if not t.startswith('phase10-b64-'):continue
 name,i=t[len('phase10-b64-'):].rsplit('-',1);groups.setdefault(name,{})[int(i)]=a['message'].strip()
evidence={'run':run,'check':check,'commit':commit,'method':'base64 JSON chunks from check annotations; no binary artifacts claimed local','reports':{}}
for name,parts in groups.items():
 assert sorted(parts)==list(range(len(parts)))
 raw=base64.b64decode(''.join(parts[i] for i in sorted(parts)),validate=True);json.loads(raw);(out/name).write_bytes(raw);evidence['reports'][name]=hashlib.sha256(raw).hexdigest()
assert len(groups)==6,groups.keys()
(out/'evidence.json').write_text(json.dumps(evidence,indent=2)+'\n')
