"""Download pinned MIT Rocketbox transitions through authenticated gh; verify git blobs."""
import subprocess,json,base64,hashlib
from pathlib import Path
revision='0943055db6ec570bcef9f2c8b41c9e5467c808f9'
files={'m_crouch_in.max.fbx':'e63c503b61c3890215191b469d2e6bad9ccd8350','m_crouch_out.max.fbx':'da0725eec751a236e13cb40d1ef21b7684a324b4'}
root=Path('.cache/phase3');root.mkdir(parents=True,exist_ok=True)
for name,sha in files.items():
 result=json.loads(subprocess.check_output(['gh','api','repos/microsoft/Microsoft-Rocketbox/git/blobs/'+sha]));data=base64.b64decode(result['content'])
 assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==sha
 (root/name).write_bytes(data)
print('Verified 2 source FBX blobs at '+revision)
