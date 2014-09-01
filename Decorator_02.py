import functools

def log(arg):
	if hasattr(arg, '__call__'):
		@functools.wraps(arg)
		def wrapper(*args, **kw):
			print '%s():' %arg.__name__
			return arg(*args, **kw)
		return wrapper

	def decorate(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print '%s %s()' %(arg, func.__name__)
			return func(*args, **kw)
		return wrapper
	return decorate


@log('excute')
def now():
	print '2014-09-01'

now()

@log
def now():
	print '2014-09-02'

now()