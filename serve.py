#!/usr/bin/env python3
# Tiny static server that disables caching, so phone/desktop always get fresh files.
import http.server, socketserver, functools
from pathlib import Path

ROOT = str(Path(__file__).parent)
PORT = 8777

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

socketserver.ThreadingTCPServer.allow_reuse_address = True
with socketserver.ThreadingTCPServer(('0.0.0.0', PORT), functools.partial(Handler, directory=ROOT)) as httpd:
    print(f"Serving {ROOT} on 0.0.0.0:{PORT} (no-cache)")
    httpd.serve_forever()
