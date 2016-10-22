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

Python provides us a way to pass multiple arguments to a function. it uses two operators `*` and `**`. The former is used to pass the arguments by position and the latter by key-word arguments. By convention we use `*args` for postion parameters and `**kwargs` for key-word arguments.

We can also use `*` and `**` as a sort of "spread" operators, that is if we have a tuple `t` we can expand it as positional params on foo : `foo(*t)`. The same goes for a dict d, whose name and key-value pairs can be expanded as key word arguments

`foo(**d)`

### Decorators :

Decorators in python, in its most simple case are a syntax sugar for this :

`@foo
def bar():
  bar`
is equivalent to 

`bar = foo(bar)`

essentially a higher-order function returning another function. To be more precise one callable object returning another callable object

To go in depth `@` desugars the decorator in 2 flavours depending on wether arguments are passed or not. 
1. The decorator function
2. The decorator factory.

## Note :

In the wild  we generally find that functions and classes are used to decorate other functions and classes. the semantics for the combinations there in are slightly different.






