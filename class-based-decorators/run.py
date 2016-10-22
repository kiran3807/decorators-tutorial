from decorators import static_class_based_decorator, flexible_class_based_decorator

@static_class_based_decorator
def foo():
    print "foo called"
    
    
foo()

@flexible_class_based_decorator
def bar(*args):
    print "called with args : {0}".format(args)
    
bar(1,2)
