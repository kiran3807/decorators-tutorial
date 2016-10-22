
def foo(func):
    def wrapper(*args):
        print "decorated using foo"
        func(*args)
        
    return wrapper
    
def bar(func):
    def wrapper(*args):
        print "decorated using bar"
        func(*args)
        
    return wrapper

@foo
@bar    
def fizz():
    print "fizz"
    
fizz()
    
    
    

