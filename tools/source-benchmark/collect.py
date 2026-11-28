"""Lossless public-report/thumbnail transport; binary videos remain artifacts."""
import subprocess,json,zlib,base64,hashlib,sys
from pathlib import Path
run,check,commit=sys.argv[1:];root=Path('docs/coach/phase12');groups={}
for a in json.loads(subprocess.check_output(['gh','api',f'repos/aydiarra-star/PARISFIT/check-runs/{check}/annotations?per_page=100'])):
 t=a.get('title','')
 if not t.startswith('phase12-'):continue
 name,i=t[8:].rsplit('-',1)
 if i.isdigit():groups.setdefault(name,{})[int(i)]=a['message'].strip()
e={'run':run,'check':check,'commit':commit,'reports':{},'scope':'CI source qualification; source and motion approval are separate'}
for name,parts in groups.items():
 assert sorted(parts)==list(range(len(parts)))
 raw=zlib.decompress(base64.b64decode(''.join(parts[i] for i in sorted(parts)),validate=True))
 if name.endswith('.json'):json.loads(raw)
 elif name.endswith('.png'):assert raw.startswith(b'\x89PNG\r\n\x1a\n')
 else:raise ValueError('UNEXPECTED_FILE')
 (root/name).write_bytes(raw);e['reports'][name]=hashlib.sha256(raw).hexdigest()
assert {'14_06-report.json','original-retrieval.json','original-analysis.json','visual-report.json','marker-benchmark.json'}<=set(groups),groups.keys()
(root/'ci-evidence.json').write_text(json.dumps(e,indent=2)+'\n')
