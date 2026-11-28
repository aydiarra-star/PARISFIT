from pathlib import Path
import subprocess,json,base64,zlib,hashlib,sys
run,check,commit=sys.argv[1:];parts={}
for a in json.loads(subprocess.check_output(['gh','api',f'repos/aydiarra-star/PARISFIT/check-runs/{check}/annotations?per_page=100'])):
 if a.get('title','').startswith('phase14-original-'):parts[int(a['title'].rsplit('-',1)[1])]=a['message'].strip()
assert parts and sorted(parts)==list(range(len(parts)))
b=zlib.decompress(base64.b64decode(''.join(parts[i] for i in sorted(parts)),validate=True));d=json.loads(b);assert d['archiveSHA256']=='901112330ed234ad97ce24cb866bd5e7e33bef766861d21264953b3ac1875782'
p=Path('docs/coach/phase14');(p/'original-audit.json').write_bytes(b);(p/'evidence.json').write_text(json.dumps({'status':'VALIDÉ','scope':'transport/integrity not anatomical qualification','run':run,'check':check,'commit':commit,'originalAuditSHA256':hashlib.sha256(b).hexdigest()},indent=2)+'\n')
