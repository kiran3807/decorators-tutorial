
def static_decorator(func):
    
    def wrapper():
        print "called the static_decorator code"
        func()
        
    return wrapper
    
    
def flexible_decorator(func):

    def wrapper(*args):
        print "called the flexible_decorator code"
        func(*args)
        
    return wrapper
