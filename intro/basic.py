"""def outer():
	print "out"
	
def deco(func):
	return outer

@deco	
def foo():
	print "foo"
	
foo() """

""" The above code is equivivalent to """

"""def foo():
    print "foo"
    
def outer():
    print "out"
    
def deco(func):
    return outer
    
foo = deco(foo)

foo()"""
######################################################
"""class fizz(object):
    def __init__(self,fn):
        self.fn = fn
        
    def __call__(self,*args):
        print "decorated"
        self.fn(*args)    
        
@fizz
def buzz(a,b):
    print "{0}, {1}" .format(a,b)   
buzz(1,2)"""

""" above code equivalent to """

class fizz(object):
    def __init__(self,fn):
        self.fn = fn
        
    def __call__(self,*args):
        print "decorated"
        self.fn(*args)   

def buzz(a,b):
    print "{0}, {1}" .format(a,b)        


buzz = fizz(buzz)
buzz(4,5)



