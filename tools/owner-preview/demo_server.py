"""Separate demo service. Requires a freshly built .cache/owner-demo directory.
Set PARISFIT_DEMO_PASSWORD and COOKIE_SECURE=1 behind an HTTPS reverse proxy.
Never use this service as the public PARISFIT deployment.
"""
import hashlib, hmac, http.server, mimetypes, os, secrets, time
from http.cookies import SimpleCookie
from pathlib import Path
from urllib.parse import parse_qs, urlsplit
ROOT=Path(__file__).resolve().parents[2]
PUBLIC=ROOT/'.cache/owner-demo'
if not (PUBLIC/'review-feedback.js').exists(): raise SystemExit('Run build_demo.py first')
PASSWORD=os.environ.get('PARISFIT_DEMO_PASSWORD')
if not PASSWORD:
    if os.environ.get('RENDER') or os.environ.get('RENDER_SERVICE_ID'):
        raise SystemExit('PARISFIT_DEMO_PASSWORD must be configured in Render environment settings')
    key=ROOT/'.cache/owner-preview-access.txt'
    if not key.exists():
        key.parent.mkdir(exist_ok=True);key.write_text(secrets.token_urlsafe(24));key.chmod(0o600)
    PASSWORD=key.read_text().strip()
if len(PASSWORD)<16: raise SystemExit('Demo password must contain at least 16 characters')
SESSION=secrets.token_urlsafe(32)
SECURE=os.environ.get('COOKIE_SECURE','1')=='1'
FILES={'/'+p.relative_to(PUBLIC).as_posix():p for p in PUBLIC.rglob('*') if p.is_file()}
FILES['/']=PUBLIC/'index.html'
attempts={}
LOGIN='''<!doctype html><html lang="fr"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PARISFIT — Démonstration privée</title><style>body{font:18px system-ui;background:#edf5ef;color:#153f32;max-width:480px;margin:10vh auto;padding:24px}input,button{box-sizing:border-box;width:100%;padding:14px;font:inherit;margin:12px 0}</style><h1>PARISFIT</h1><p>Démonstration privée du Coach humain. Animations non validées professionnellement.</p><form method="post" action="/login"><label>Code d’accès<input name="password" type="password" required autocomplete="current-password"></label><button>Entrer dans PARISFIT</button></form></html>'''
class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self,*args): pass
    def reply(self,status,data=b'',kind='text/html; charset=utf-8',headers=()):
        self.send_response(status)
        for k,v in [('Content-Type',kind),('Cache-Control','no-store'),('X-Content-Type-Options','nosniff'),('Referrer-Policy','same-origin'),('Content-Length',str(len(data))),*headers]:self.send_header(k,v)
        self.end_headers();self.wfile.write(data)
    def authenticated(self):
        try:
            c=SimpleCookie(self.headers.get('Cookie',''));return hmac.compare_digest(c['pf_demo'].value,SESSION)
        except (KeyError,ValueError):return False
    def do_GET(self):
        path=urlsplit(self.path).path
        if not self.authenticated():
            self.reply(200 if path=='/' else 401,LOGIN.encode() if path=='/' else b'Authentication required');return
        if path not in FILES:self.reply(404,b'Not found');return
        p=FILES[path];kind=mimetypes.guess_type(str(p))[0] or 'application/octet-stream'
        self.reply(200,p.read_bytes(),kind)
    def do_POST(self):
        if self.path!='/login':self.reply(404);return
        # Reject cross-origin form submissions; no credential in URL or client bundle.
        origin=self.headers.get('Origin')
        if origin and urlsplit(origin).netloc!=self.headers.get('Host'):self.reply(403);return
        try:n=int(self.headers.get('Content-Length','0'))
        except ValueError:self.reply(400);return
        if not 0<n<=4096:self.reply(413);return
        ip=self.client_address[0];now=time.monotonic()
        recent=[x for x in attempts.get(ip,[]) if now-x<60];attempts[ip]=recent
        if len(recent)>=10:self.reply(429,b'Too many attempts. Retry in one minute.');return
        recent.append(now)
        value=parse_qs(self.rfile.read(n).decode('utf8',errors='replace')).get('password',[''])[0]
        if not hmac.compare_digest(hashlib.sha256(value.encode()).digest(),hashlib.sha256(PASSWORD.encode()).digest()):self.reply(401,LOGIN.encode());return
        cookie=f'pf_demo={SESSION}; HttpOnly; SameSite=Strict; Path=/'+('; Secure' if SECURE else '')
        self.reply(303,headers=[('Set-Cookie',cookie),('Location','/')])
print('PARISFIT private integrated demo started; no credentials logged.',flush=True)
http.server.ThreadingHTTPServer(('0.0.0.0',int(os.environ.get('PORT','3013'))),Handler).serve_forever()
