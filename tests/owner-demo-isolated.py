"""Exercise only the runtime package, with an environment secret and a random PORT.
Does not require Arena services, the original repository at runtime, or Docker.
"""
import http.client, json, os, secrets, shutil, socket, struct, subprocess, sys, tempfile, time
from pathlib import Path
from urllib.parse import urlencode
ROOT=Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(dir=ROOT/'.cache',prefix='isolated-demo-') as tmp:
    root=Path(tmp)
    server=root/'tools/owner-preview/demo_server.py';server.parent.mkdir(parents=True)
    shutil.copyfile(ROOT/'tools/owner-preview/demo_server.py',server)
    shutil.copytree(ROOT/'.cache/owner-demo',root/'.cache/owner-demo')
    with socket.socket() as sock:sock.bind(('127.0.0.1',0));port=sock.getsockname()[1]
    secret=secrets.token_urlsafe(32)
    env={**os.environ,'RENDER':'true','PARISFIT_DEMO_PASSWORD':secret,'PORT':str(port),'COOKIE_SECURE':'1'}
    def request(method,path,body=None,headers=None):
        conn=http.client.HTTPConnection('127.0.0.1',port,timeout=5)
        conn.request(method,path,body,headers or {});r=conn.getresponse();result=(r.status,dict(r.getheaders()),r.read());conn.close();return result
    proc=subprocess.Popen([sys.executable,str(server)],cwd=root,env=env,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    try:
        for _ in range(100):
            try:
                status,_,html=request('GET','/');break
            except OSError:time.sleep(.05)
        else:raise AssertionError('No listening server')
        assert status==200 and b'PARISFIT' in html
        for path in ['/assets/coach/coach-review.glb','/coach-3d.js','/review-feedback.js']:
            assert request('GET',path)[0]==401
        assert request('POST','/login',urlencode({'password':'wrong'}),{'Content-Type':'application/x-www-form-urlencoded'})[0]==401
        assert request('POST','/login',urlencode({'password':secret}),{'Origin':'https://untrusted.invalid'})[0]==403
        status,headers,_=request('POST','/login',urlencode({'password':secret}),{'Content-Type':'application/x-www-form-urlencoded'})
        assert status==303
        cookie=headers['Set-Cookie'];assert all(x in cookie for x in ['HttpOnly','Secure','SameSite=Strict'])
        auth={'Cookie':cookie.split(';',1)[0]}
        status,_,html=request('GET','/',headers=auth);assert status==200 and b'view-coach' in html
        status,_,glb=request('GET','/assets/coach/coach-review.glb',headers=auth);assert status==200
        size=struct.unpack_from('<I',glb,12)[0];g=json.loads(glb[20:20+size]);assert len(g['animations'])==8
        for path in ['/.git/config','/service-worker.js','/tools/owner-preview/demo_server.py','/../demo_server.py']:
            assert request('GET',path,headers=auth)[0]==404
        assert not (root/'.cache/owner-preview-access.txt').exists()
        for file in (root/'.cache/owner-demo').rglob('*'):
            if file.is_file():assert secret.encode() not in file.read_bytes()
    finally:
        proc.terminate();stdout,stderr=proc.communicate(timeout=10)
        assert secret.encode() not in stdout+stderr
    # Preserve and verify the concurrent owner's explicit open-demo mode.
    opened=subprocess.Popen([sys.executable,str(server)],cwd=root,env={**env,'PARISFIT_DEMO_OPEN':'1'},stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    try:
        for _ in range(100):
            try:
                status,_,html=request('GET','/');break
            except OSError:time.sleep(.05)
        else:raise AssertionError('No open-demo server')
        assert status==200 and b'view-coach' in html
        assert request('GET','/assets/coach/coach-review.glb')[0]==200
        assert request('GET','/motion-candidate.json')[0]==200
        assert request('GET','/.git/config')[0]==404
        assert request('POST','/login')[0]==404
    finally:
        opened.terminate();opened.communicate(timeout=10)
    missing=env.copy();missing.pop('PARISFIT_DEMO_PASSWORD')
    fail=subprocess.run([sys.executable,str(server)],env=missing,capture_output=True,timeout=5)
    assert fail.returncode!=0 and b'must be configured' in fail.stderr
print(json.dumps({'status':'PASS','isolatedRuntime':True,'portFromEnvironment':True,'environmentSecretOnly':True,'clips':8,'explicitOpenDemo':'GET app/model/candidate 200 without cookie; login/internal paths 404','authentication':'unauthenticated 401, login 303, authenticated 200','cookie':'Secure/HttpOnly/SameSite=Strict','missingRenderSecret':'fails closed','limits':['Docker not executed','Render not deployed','No physical iPhone test']},indent=2))
