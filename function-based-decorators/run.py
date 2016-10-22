from decorators import static_decorator, flexible_decorator

@static_decorator
def foo():
    print "foo called"
    
foo()
# this will throw error, as we havent coded the generator to accomodate it. to continue comment it
foo(4)

@flexible_decorator
def bar(a):
    print "called with arg : {0}".format(a)
    
bar('barbar')

