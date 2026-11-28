"""Only pinned public CMU BVH fixtures. No accounts, private uploads or purchases."""
from pathlib import Path
import hashlib,json,base64,subprocess,urllib.request
ITEMS={'14_14':'15e27a816e0aa7089a86372c04ba402a692a2218','13_30':'921fe6c8e8041ae45281bf232e58cb3299285d05','86_08':'690242fca4f3545caf671f968f37cc6e03bb1762'}
def main():
 root=Path('.cache/phase12');root.mkdir(parents=True,exist_ok=True);manifest=[]
 for name,blob in ITEMS.items():
  path=root/(name+'.bvh')
  if path.exists():raw=path.read_bytes()
  else:
   r=json.loads(subprocess.check_output(['gh','api',f'repos/una-dinosauria/cmu-mocap/git/blobs/{blob}']));raw=base64.b64decode(r['content'])
  assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==blob
  path.write_bytes(raw);manifest.append({'id':name,'blob':blob,'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'provenance':'CMU converted BVH, mirror commit09a07f54f3bbb58797325f009282d0b2048a2871','selection':'screening only, NOT qualified reference'})
 (root/'downloads.json').write_text(json.dumps(manifest,indent=2)+'\n')
if __name__=='__main__':main()
