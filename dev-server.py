#!/usr/bin/env python3
import http.server, os
from urllib.parse import urlparse

ROOT = os.path.dirname(__file__)
PORT = 4011

class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = urlparse(path).path
        return os.path.join(ROOT, path.lstrip('/'))

    def do_GET(self):
        path = urlparse(self.path).path
        if path in ('/', '/index.html'):
            self.path = '/index.html'
        elif path.startswith('/doc/'):
            self.path = '/doc.html'
        elif path.startswith('/worklog/ep-'):
            self.path = '/worklog.html'
        return super().do_GET()

if __name__ == '__main__':
    os.chdir(ROOT)
    print(f'colly-library dev server: http://127.0.0.1:{PORT}')
    http.server.ThreadingHTTPServer(('127.0.0.1', PORT), Handler).serve_forever()
