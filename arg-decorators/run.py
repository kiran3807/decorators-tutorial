from decorators import noarg_function_based_decorator, arg_function_based_decorator, arg_class_based_decorator

@noarg_function_based_decorator
def foo(a):
    print "foo called with arg : {0} ".format(a)
 
"""uncomment to see decorators in action """  
"""foo(2)"""
    
@noarg_decorator
def bar():
    print "bar called

"""uncomment to see decorators in action """  
"""bar('abc')"""

def do():
    print "do called"
    
@arg_function_based_decorator(do)
def fizz(a):
    print 'fizz called with {0}'.format(a)

"""uncomment to see decorators in action   
fizz('buzz')"""

@arg_class_based_decorator('params')
def greet(name):
    print "Hey there {0} ! ".format(name)
    
greet(2)
