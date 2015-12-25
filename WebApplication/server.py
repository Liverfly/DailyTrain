
from wsgiref.simple_server import make_server

from hello import application

http = make_server('',8000,application)
print "Serving HTTP on port 8000..."

http.serve_forever()