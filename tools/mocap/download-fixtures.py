"""Fetch only two public licensed fixtures, pinned by Git blob; never uploads video."""
from pathlib import Path
import json,subprocess,base64,hashlib
items=[('HUSNAIN-MUNAWAR/motionforge-3d','f9f7551ecc00c41ac1779c7d4a2c02272f35a139','docs/coach/phase5/source.webm'),('una-dinosauria/cmu-mocap','fd551a6b3e25d3a801f2de37ebb89aa2c8698083','.cache/phase5/cmu-22_14.bvh')]
for repo,sha,path in items:
 r=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/git/blobs/{sha}']));b=base64.b64decode(r['content']);assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==sha;p=Path(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b);print(path,hashlib.sha256(b).hexdigest())
