import http.server
from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import socketserver
import json
import config
from newsapi import NewsApiClient

PORT = 1337

newsapi = NewsApiClient(api_key=config.API_KEY)

data = newsapi.get_top_headlines(category='technology',language='en')

with open("data.json", "w") as file:
    file.write(json.dumps(data))


class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')

        SimpleHTTPRequestHandler.end_headers(self)


if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer, port=PORT)
