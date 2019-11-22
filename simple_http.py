from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    """."""

    def do_POST(self):
        """."""
        print "Recebi um POST"
        content_len = self.headers.getheaders('content-length')
        content_len = content_len and int(content_len[0]) or 0
        print "<----------Inicio POST---------->"
        print(self.rfile.read(content_len))
        print "<----------Fim POST---------->"
        self.send_response(204)
        self.end_headers()


server = HTTPServer(('localhost', 5000), RequestHandler)
server.serve_forever()
