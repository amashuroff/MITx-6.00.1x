"""
Functions - give us a great tool of decomposition and abstraction

Abstraction - i don't need to know what is inside the black box, as long as i know how to use it.
Code: suppress details of method to compute something from the use of that computation, Input/Output,
    achieve abstraction using docstrings and function specifications

Decomposition - different devices work together to achieve an end goal
Code: break problem into different , self-contained pieces, modules, classes, functions

Functions:
    should be "invoked" or "called" in a program
    has: name, body, docstring, parameters(0 or more)

Formal parameter gets bound to the value of actual parameter (or an argument) when function is called
    (Arguments are the actual values passed to functions (for the functions to work with).
    (Parameters are variable definitions inside a function.)

Function scope: is mapping of names to objects;
    new scope,/frame/environment is created when enter the function

Function returns None without return

Functions inside the functions:
    If we want to get the function returned by another function and call the function returned immediately,
    we can use this syntax:
        functionThatReturnsAFunction(arguments_for_this_function)(arguments_for_the_function_returned)

Specifications - docstrings:
    Assumptions: conditions that mst be met by clients, constrains on values of parameters
    Guarantees: conditions that must be met by the function (its been called with right conditions)
"""


# example of the variable scope
# here we are acting in the global scope
def f(x): # x acts as a formal parameter (whatever we make it to be)
    # here we are acting in the local scope
    x = x + 1
    print("in f(x): x = ", x)
    return x

x = 3
# here x acts as an actual parameter that we give to the function
z = f(x)


# unbound local error function
def h(y):
    x += 1
    return x

x = 1
print(h(x))


# if we pass arguments for both g and h we get the outcome
# if we don't pass any arguments for h, we ge the location of h in memory
def g():
    return h
# print(g()(x))


# keyword arguments and variations
# reverse acts as a True or False condition
def printName(firstName, lastName, reverse=False): # specify the initial values, in the case of not having reverse called explicitly
    if reverse:
        print(lastName + ' ' + firstName)
    else:
        print(firstName, lastName)


# variations
printName('Alex', 'Green', True)
printName('Alex', 'Green', reverse=False)
printName('Alex', lastName='Green', reverse=True)
printName(lastName='Green', reverse=True, firstName='Alex')