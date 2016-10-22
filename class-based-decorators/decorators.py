class static_class_based_decorator(object):
    
    def __init__(self, func):
        self.func = func
        
    def __call__(self):
        print "static decorated !!"
        self.func()
            
            
            
class flexible_class_based_decorator(object):

    def __init__(self,func):
        self.func = func
        
    def __call__(self, *args):
        print "flexibly decorator"
        self.func(*args)
