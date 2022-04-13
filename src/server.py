from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
pwd = os.getcwd()

from config import getconfig 
config = getconfig()
hostName = "localhost"
port = config['port']

class HelloServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
    def do_GET(self):
        filepath = os.path.join(os.path.join(os.path.dirname(__file__), "public"), 'index.html' if self.path == '/' else self.path[1: len(self.path)])
        filesize = os.path.getsize(filepath)
        print(filepath + " " + str(filesize))
        try:
            if self.path == '/style.css':
                f = open(filepath, 'r')
                self.send_response(200)
                self.send_header("Content-type", "text/css")
                self.send_header("Content-length", filesize)
                self.end_headers()
                while True:
                    file_data = f.read(32768)
                    if file_data is None or len(file_data) == 0:
                        break
                    self.wfile.write(bytes(file_data, 'UTF-8')) 
                f.close()
            elif self.path == '/favicon.ico':
                f = open(filepath, 'rb')
                self.send_response(200)
                self.send_header("Content-type", "image/x-icon")
                self.send_header("Content-length", filesize)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
            else:
                f = open(filepath, 'r')
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.send_header("Content-length", filesize)
                self.end_headers()
                while True:
                    file_data = f.read(32768)
                    if file_data is None or len(file_data) == 0:
                        break
                    self.wfile.write(bytes(file_data, 'UTF-8')) 
                f.close()
        except FileNotFoundError:
            print(self.path)
            self.send_response(404)
    def do_POST(self):
        print(self.path)
        # TODO: AJAX requests
        self.send_response(404)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, port), HelloServer)
    print("Server started http://%s:%s" % (hostName, port))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")