import http.server
import socketserver
import json
import config
from newsapi import NewsApiClient

PORT = 1337

newsapi = NewsApiClient(api_key=config.API_KEY)

data = newsapi.get_top_headlines(category='technology',language='en')

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json','Access-Control-Allow-Origin: *')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

# Im not sure if I like this implamentation, copyed from google ai websearch thing...