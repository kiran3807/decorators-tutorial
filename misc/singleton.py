# example of a class decorator , That is a decorator which decorates a class

def singleton(cls):
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance
    
@singleton
class Foo(object):
    pass
    
x = Foo()

y = Foo()

print id(x)
print id(y)
