# Ryan Pineyro
# Simple Python
import http.server
import socketserver
import os
Port = int(os.environ('PORT', 8080))
Handler = http.server.SimpleHTTPRequestHandler
Webdir = os.path.dirname(os.path.realpath(__file__))
os.chdir(Webdir)
with socketserver.TCPServer(("", Port), Handler) as httpd:
    httpd.serve_forever()