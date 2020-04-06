"""
Recursion: programming technique where the program calls itself

Recursion:
    must have 1 or more base cases (that are easy to solve)
    must solve the same problem on some other input with the goal of simplifying the larger program input

Iteration should be your default in most problems as it will be faster, easier and more readable.

Each recursive call of the function creates its own scope/environment
We are using the same variable names, but they are different objects is separate scopes
Bindings of variables in that scope is not changed by the recursive call (we go deeper)
Flow of control passes back to previous scope once function call returns value

Mathematical induction (in our recursive example): if the base case is true, that means it returns the right answer for
the problem of size b, and by mathematical induction, my code will always do the right thing for appropriate values of
a and b. (see the equation solution on the forum)

"""


# simple example of recursion
# base case = a, case + 1 = a + base case of a, etc
def mult(a,b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)

# factorial example
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
            return n * factorial(n-1)


# towers of hanoi example
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr,to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)


# Recursion vs Iteration examples
# iteration
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1

    while exp > 0:
        result *= base
        exp -= 1
    return result
# recursion
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

# great common divisor iteration
def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    testValue = min(a, b)

    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue

# great common divisor recursion
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

