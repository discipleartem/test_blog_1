import os, sys

from http.server import HTTPServer, CGIHTTPRequestHandler
# Путь до корня, где лежит cgi-bin
webdir = r'D:\python_win\work\Blogs\test_blog_1'
port = 8000
# Переходим в корневую директорию
os.chdir(webdir)
srvaddr = ('127.0.0.1', port)
srvrobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()
