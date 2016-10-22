
def noarg_function_based_decorator(func):
    print "Inside the no arg decorator"
    funcName = func.__name__
    def wrap_a(*args):
        func(*args)
    def wrap_b(*args):
        func(*args)
        
    if funcName == "foo":
        print "decorating foo with wrap_a"
        return wrap_a
    elif funcName == "bar":
        print "decorating bar with wrap_b"
        return wrap_b
    else:
        print "no decoration performed"
        return func
        
        
def arg_function_based_decorator(callBefore):
    print "inside arg decorator"
    def actual_decorator(func):
    
        def wrapper(*args):
            call_before_name = callBefore.__name__
            func_name = func.__name__
            print "decorating {0} with {1}".format(call_before_name,func_name)
            callBefore()
            func(*args)
        
        return wrapper
    
    return actual_decorator
    
###############################################################

class arg_class_based_decorator(object):

    def __init__(self,*args):
        self.args = args
        
    def __call__(self,func):
        #some processing using self.args
        def wrapper(*args):
            print "inside the decorator"
            func(*args)
            
        return wrapper
        
        
        
        
    
