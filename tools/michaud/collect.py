import json,zlib,base64,hashlib,subprocess,sys
from pathlib import Path
run,check,commit=sys.argv[1:];root=Path('docs/coach/phase13');root.mkdir(parents=True,exist_ok=True);groups={}
for a in json.loads(subprocess.check_output(['gh','api',f'repos/aydiarra-star/PARISFIT/check-runs/{check}/annotations?per_page=100'])):
 t=a.get('title','')
 if not t.startswith('phase13-'):continue
 name,i=t[len('phase13-'):].rsplit('-',1)
 if i.isdigit():groups.setdefault(name,{})[int(i)]=a['message'].strip()
e={'run':run,'check':check,'commit':commit,'scope':'lossless public diagnostic reports and review samples, not human approval','files':{}}
for name,parts in groups.items():
 assert sorted(parts)==list(range(len(parts)))
 raw=zlib.decompress(base64.b64decode(''.join(parts[i] for i in sorted(parts)),validate=True));json.loads(raw);(root/name).write_bytes(raw);e['files'][name]=hashlib.sha256(raw).hexdigest()
assert {'markers-report.json','forces-report.json','reconstruction-report.json','phases-report.json','review-data.json','provenance.json','model-inspection.json'}<=set(groups),groups.keys()
(root/'evidence.json').write_text(json.dumps(e,indent=2)+'\n')
