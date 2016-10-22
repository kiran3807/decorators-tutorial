class NotFlask(object):
    def __init__(self):
        self.map = {}
        
    def route(self,r):
        
        def decorator(fn):
            self.map[r] = fn
            print "added the function to the routes"
            print self.map
            return fn 
            
        return decorator
        
        
app = NotFlask()

@app.route('/route')
def foo():
    print "just another routing function"
    
foo()
