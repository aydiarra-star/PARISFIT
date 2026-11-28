"""Bounded secret-pattern check on RESTORED bytes and all Git blobs, with redacted outputs.
No credential files read; no keys or suspicious values ever printed.
"""
import json,re,os,subprocess,hashlib,zipfile,tarfile,io
from pathlib import Path
R=Path(__file__).resolve().parents[2];D=R/'docs/coach/phase26';T=R/'.cache/phase26-work/restored'
patterns={
 'private-key-material':rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----[\r\n]+[A-Za-z0-9+/=\r\n]{64,}-----END ',
 'github-token':rb'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b',
 'aws-access-key-id':rb'\bAKIA[0-9A-Z]{16}\b',
 'google-api-key':rb'\bAIza[0-9A-Za-z_-]{35}\b',
 'credential-literal':rb'(?i)(?:password|api_key|access_token|secret)\s*[:=]\s*[\x22\x27][A-Za-z0-9_+/=-]{12,}[\x22\x27]',
 'signed-url':rb'(?i)[?&](?:X-Amz-Signature|X-Goog-Signature|access_token|sig)=[A-Za-z0-9%+/=_-]{20,}'
}
patterns={k:re.compile(v) for k,v in patterns.items()};findings=[];count=0;nested=0;limits=[]
def scan(label,data):
 global count
 count+=1
 for k,p in patterns.items():
  n=len(p.findall(data))
  if n:findings.append({'location':label,'kind':k,'count':n})
rows=json.loads((D/'backup-file-manifest.json').read_text())
for r in rows:
 b=(T/'files'/r['path']).read_bytes();scan(r['path'],b)
 # One archive level: dependencies/old tar caches; no scripts executed.
 if r['path'].endswith(('.zip','.whl','.tar','.tar.gz','.tgz')):
  try:
   if zipfile.is_zipfile(io.BytesIO(b)):
    with zipfile.ZipFile(io.BytesIO(b)) as z:
     for m in z.infolist():
      if m.is_dir():continue
      if m.file_size>100*1024*1024:limits.append({'path':r['path']+'!'+m.filename,'reason':'member over 100MiB'});continue
      scan(r['path']+'!'+m.filename,z.read(m));nested+=1
   else:
    with tarfile.open(fileobj=io.BytesIO(b)) as t:
     for m in t:
      if not m.isfile():continue
      if m.size>100*1024*1024:limits.append({'path':r['path']+'!'+m.name,'reason':'member over 100MiB'});continue
      scan(r['path']+'!'+m.name,t.extractfile(m).read());nested+=1
  except (tarfile.ReadError,zipfile.BadZipFile):limits.append({'path':r['path'],'reason':'empty or unreadable archive'})
objects=json.loads((D/'git-object-manifest.json').read_text());env=dict(os.environ,GIT_OBJECT_DIRECTORY=str(T/'objects'),GIT_ALTERNATE_OBJECT_DIRECTORIES='');proc=subprocess.Popen(['git','cat-file','--batch'],cwd=R,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
for oid,r in objects.items():
 if r['type']!='blob':continue
 proc.stdin.write((oid+'\n').encode());proc.stdin.flush();head=proc.stdout.readline().decode().split();b=proc.stdout.read(int(head[2]));proc.stdout.read(1);scan('git-blob:'+oid,b)
proc.stdin.close();assert proc.wait()==0
out={'status':'NO_PATTERN_MATCH' if not findings else 'REVIEW_REQUIRED','unitsScanned':count,'nestedMembersScanned':nested,'patterns':list(patterns),'findings':findings,'limits':limits,'valuesRedacted':True,'sharingAuthorized':False,'certifiesNoSecret':False,'notes':['Pattern matching is not proof of absence of all secrets.','One nested archive level only; arbitrary encryption and recursively compressed binary content not proven safe.','Personal data, scientific rights, author emails and professional contacts require separate review.']}
(D/'security-scan.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
