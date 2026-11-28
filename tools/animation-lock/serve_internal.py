"""Explicit local-only diagnostic server; never included in public artifact."""
import argparse,http.server
from pathlib import Path
from functools import partial
p=argparse.ArgumentParser();p.add_argument('--acknowledge-unvalidated',action='store_true');a=p.parse_args()
if not a.acknowledge_unvalidated:p.error('Explicit acknowledgement required for internal diagnostics')
http.server.ThreadingHTTPServer(('127.0.0.1',3012),partial(http.server.SimpleHTTPRequestHandler,directory=str(Path(__file__).resolve().parents[2]))).serve_forever()
