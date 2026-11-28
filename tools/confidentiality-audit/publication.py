"""Audit existing public artifact without rebuilding or deleting any resource."""
from pathlib import Path
import json,hashlib,struct,http.server,threading,urllib.request,urllib.error,functools,sys
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase25';P=R/'.cache/public';sys.path.insert(0,str(R/'tools/animation-lock'));from build_public import static_model
expected=json.loads((R/'docs/coach/phase24/public-build.json').read_text())['publicFiles'];files=sorted(str(p.relative_to(P)) for p in P.rglob('*') if p.is_file());assert files==expected
rows=[]
for name in files:
 b=(P/name).read_bytes();rows.append({'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 if name!='assets/coach/coach-static.glb':assert b==(R/name).read_bytes(),name
b=(P/'assets/coach/coach-static.glb').read_bytes();assert b==static_model((R/'assets/coach/coach.glb').read_bytes());n=struct.unpack_from('<I',b,12)[0];g=json.loads(b[20:20+n]);assert not g.get('animations');used={a['bufferView'] for a in g['accessors']}|{i['bufferView'] for i in g['images']};assert used==set(range(len(g['bufferViews'])))
class Handler(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Handler,directory=str(P)));thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base=f'http://127.0.0.1:{server.server_port}'
def status(path):
 try:
  with urllib.request.urlopen(base+'/'+urllib.parse.quote(path,safe='/'),timeout=5) as r:r.read();return r.status
 except urllib.error.HTTPError as e:return e.code
history=json.loads((D/'history-inventory.json').read_text());denied=sorted({r['path'] for r in history if (r['path'].startswith(('docs/','tools/','tests/')) or r['category'] in ['video','capture-or-biomechanical-model','3d-model']) and r['path'] not in files})
tests=[{'path':name,'expected':404,'status':status(name)} for name in denied];tests += [{'path':name,'expected':200,'status':status(name)} for name in files];server.shutdown();server.server_close();assert all(t['status']==t['expected'] for t in tests)
report={'status':'PASS','scope':'existing .cache/public served locally; not deployed production','files':rows,'bytes':sum(x['bytes'] for x in rows),'staticGLB':{'animations':len(g.get('animations',[])),'accessors':len(g['accessors']),'bufferViews':len(g['bufferViews']),'allViewsReferenced':True,'exactReproducibleDerivative':True},'httpTests':tests,'deniedCount':len(denied),'allowedCount':len(files)}
(D/'publication-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['files','httpTests']},indent=2))
