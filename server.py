import http.server
import socketserver
import json
import config
from newsapi import NewsApiClient

PORT = 1337

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        data = {'message': 'Hello from Python!'}
        self.wfile.write(json.dumps(data).encode())

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

# Im not sure if I like this implamentation, copyed from google ai websearch thing...