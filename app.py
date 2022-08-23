import http.server
from prometheus_client import Counter,start_http_server

no_of_requests = Counter('app_requests_so_far','no of requests made so far',['app_name','endpoint'])


PORT = 8000
METRICS_PORT=8001

class HandleRequests(http.server.http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        no_of_requests.labels('myapi',self.path).inc()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes('{"message":"Python API is running"}','utf-8'))
        self.wfile.close()

if __name__ == '__main__':
    start_http_server(METRICS_PORT)
    server=http.server.HTTPServer(('localhost',PORT),HandleRequests)
    server.serve_forever()