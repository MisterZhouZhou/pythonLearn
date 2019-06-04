from http.server import HTTPServer
import os
from sys import version as python_version

if python_version.startswith('3'):
    from urllib.parse import parse_qs
    from http.server import BaseHTTPRequestHandler
else:
    from urlparse import parse_qs
    from BaseHTTPServer import BaseHTTPRequestHandler


class NoticeHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = self.path.split('?', 1)
        if len(query) < 2:
            str = b'err'
        else:
            str = b'ok'
            params = parse_qs(query[1])
            title = params.get('title', '')[0]
            msg = params.get('msg', '')[0]
            os.system('osascript -e \'display notification "%s" with title "%s"\'' % (msg, title))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(str)

    def do_POST(self):
        self.wfile.write('method error.')


server = HTTPServer(('', 8001), NoticeHandler)
print('started http server on 127.0.0.1:8001...')
server.serve_forever()