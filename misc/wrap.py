from functools import wraps

def foo(func):
    def wrapper(*args):
        #print "decorated function"
        func(*args)
        
    return wrapper

@foo    
def bar():
    print "bar"
    
bar()

print bar.__name__
# will print "wrapper"

"""
def fizz(func):
    def wrapper(*args):
        print "decorated function"
        func()
        
    wrapper.__name__ = func.__name__
    return wrapper
    
@fizz    
def buzz():
    print "buzz"
    
print buzz.__name__
# will print buzz
"""

def fizz(func):
    
    @wraps(func)
    def wrapper(*args):
        #print "decorated function"
        func(*args)
        
    return wrapper
    
@fizz    
def buzz():
    print "buzz"
    
buzz()
    
print buzz.__name__

#print buzz.__doc__
#print buzz.__module__


