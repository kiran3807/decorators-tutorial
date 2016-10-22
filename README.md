# decorators-tutorial
Yet another decorators tutorial

## The Basics :

### Closures : 

In Python, functions are first class objects, Therefore they can be passed around as arguments and be returned from other functions. functions which do that are called higher-order functions.

Whenever a function is created, a local scope/name-space is created for that function. In that you can access the local variable of that functions. The arguments passed to the function are also avalaible in the local scope. Standard scope lookup rules apply ( LEGB )

that scope is destroyed as soon as the function finishes it's execution.

#### Inner functions :

We can also **define** a function inside another function. such functions are known as inner functions

#### Static/Lexical scoping

The scope in python is lexical not dynamic. That is the variables resolution, when done using LEGB rules will be done on the basis of how the function was written . That is if foo is defined in bar and foo is called in fizz, then bar will be the enclosing scope for foo. fizz will not be the enclosing scope.

#### Closures continued

If we return a inner function, that function has access to the variables defined in it's enclosing scope. This has an important implication. This means that the scope of the enclosing function does not die immeadetly if returns an inner function. This is nothing but a closure. This is one of the reasons as to why we can call python a functional language

### The  `__call__` magic method :

In python if we have an object foo and we call it using this syntax :
`foo()`

It is usefull to think of it as a short hand for `foo.__call__()`. In other words any object that has implemented this method is callable like a function. For example class-objects in python implement this method. That is how we are able to get a new
instance of a class when we simply do this :

`instance = MyClass()`

### `*args` and `**kargs` :





