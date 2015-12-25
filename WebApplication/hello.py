
def application(environ,start_response):
	start_response('200 K',[('Content-Type','text/html')])
	return b'<h1/>Hello, %s!' % (environ['PATH_INFO'][1:] or 'web')