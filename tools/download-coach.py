"""Fetch pinned MIT-licensed Rocketbox sources with authenticated gh; no paid service.
Usage: .venv/bin/python tools/download-coach.py (requires Pillow and gh)
Raw FBX/TGA stay in ignored .cache, only the derived GLB ships.
"""
from pathlib import Path
import subprocess,json,base64,hashlib,io
from PIL import Image
revision='0943055db6ec570bcef9f2c8b41c9e5467c808f9'
repo='microsoft/Microsoft-Rocketbox'
root='Assets/Avatars/Professions/Sports_Male_04/'
cache=Path('.cache/rocketbox');cache.mkdir(parents=True,exist_ok=True)
tree=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/git/trees/{revision}?recursive=1']))['tree']
files=[x for x in tree if x['path'].startswith(root) and x['type']=='blob' and (x['path'].endswith('/Sports_Male_04.fbx') or x['path'].endswith(('_color.tga','_normal.tga')))]
for item in files:
 reply=json.loads(subprocess.check_output(['gh','api',f'repos/{repo}/git/blobs/'+item['sha']]))
 data=base64.b64decode(reply['content']);assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==item['sha']
 p=cache/Path(item['path']).name;p.write_bytes(data)
 if p.suffix=='.tga':
  image=Image.open(io.BytesIO(data)).convert('RGB');size=2048 if p.name=='m026_head_color.tga' else 1024;image.thumbnail((size,size));image.save(p.with_suffix('.png'))
 print(p)
