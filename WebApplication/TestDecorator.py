import functools

def log(text):
	if callable(text):
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print 'function:%s'%text.__name__
			print 'begin call'
			text(*args,**kw)
			print 'end call'
		return wrapper
	else :
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print 'param:%s function:%s'%(text,func.__name__)
				print 'begin call'
				func(*args,**kw)
				print 'end call'
			return wrapper
		return decorator
		
@log 
def f1():
	print 'I\'m function1'
	
@log('execute')
def f2():
	print 'I\'m function2'
		
if __name__ == '__main__':
	f1()
	f2()