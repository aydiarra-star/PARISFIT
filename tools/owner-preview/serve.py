"""Development-only authenticated, allowlisted preview. Never serve repository root."""
import base64, hashlib, hmac, http.server, secrets
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
KEY=ROOT/'.cache/owner-preview-access.txt'
KEY.parent.mkdir(exist_ok=True)
if not KEY.exists():
    KEY.write_text(secrets.token_urlsafe(24));KEY.chmod(0o600)
PASSWORD=KEY.read_text().strip()
FILES={'/':'tools/owner-preview/index.html','/preview.js':'tools/owner-preview/preview.js','/model.glb':'assets/coach/coach.glb'}
for p in ['three.module.js','loaders/GLTFLoader.js','utils/BufferGeometryUtils.js','controls/OrbitControls.js']:
    FILES['/vendor/'+p]='vendor/three/'+p
class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def do_GET(self):
        expected='Basic '+base64.b64encode(('owner:'+PASSWORD).encode()).decode()
        if not hmac.compare_digest(self.headers.get('Authorization',''),expected):
            self.send_response(401);self.send_header('WWW-Authenticate','Basic realm="PARISFIT internal review"');self.end_headers();return
        path=self.path.split('?',1)[0]
        if path not in FILES:self.send_error(404);return
        data=(ROOT/FILES[path]).read_bytes()
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8' if path=='/' else 'text/javascript' if path.endswith('.js') else 'model/gltf-binary')
        self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.send_header('Referrer-Policy','no-referrer');self.end_headers();self.wfile.write(data)
print('Internal preview on port 3012. User: owner. Access code: .cache/owner-preview-access.txt (not logged).',flush=True)
http.server.ThreadingHTTPServer(('0.0.0.0',3012),Handler).serve_forever()
