"""
Complexity classes:
    1. O(1) - constant
    2. O(log n) - logarithmic
    3. O(n) - linear
    4. O(n log n) - loglinear
    5. O(n^c) - polynomial
    6. O(c^n) - exponential

Constant complexity:
    - complexity independent of inputs
    - very few interesting algorithms in a class, but can often have pieces that fit this class
    - can have loops or recursive calls, but number of iteration calls independent of size of input

Logarithmic complexity:
    - complexity grows as log of size of one of its inputs
    - example:
        bisection search
        binary search of a list

linear complexity:
    - searching a list in sequence to see if the element is present
    - add characters of a string, assumed to be composed of decimal digits

Log-linear complexity:
    - many practical algorithms are log-linear
    - very common is merge sort algorithm
    -...

Polynomial complexity:
    - most common algorithms are quadratic (complexity grows with square of size of an input)
    - commonly occurs when we have nested loops or recursive function calls

Exponential complexity:
    - recursive functions where more than one recursive call for each size of a problem (Towers of Hanoi)
    - i.e. function that calls itself, but in each call calls up more than once
    - many important problems are inherently exponential:
        will lead to consider approximate solutions more quickly
    - c is a constant being raised to a power based on size of the input


"""

# logarithmic complexity example
def intTostr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i//10
    return result
# how many times we go through a loop?
# how many times we divide i by 10? ---> O(log(i))
# it is linear in the number of digits in i
# but log in the size of i


# linear complexity example
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val
# linear of the length of the string, O(len(s))


# complexity can depend on number of recursive calls
# linear fact_iter
def fact_iter(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod
# number of times around the loop is n
# number of operations inside the loop is constant
# overall just O(n)

# recursive fact_iter

def fact_iter_recur(n):
    """ Assumes n >= 0"""
    if n <= 1:
        return 1
    else:
        return n * fact_iter_recur(n-1)
# still O(n) becouse the number of function calls is linear

# both iterative and recursive versions of fact_iter have the same order of growth, even if recursive version is slower

# polynomial complexity example
def isSubset(L1, L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
# O(len(L1)^2) 2 lists are the same length and have equal elements

# exponential complexity example
def genSubsets(L):
    if len(L) == 0:
        return [[]]     # list of empty list
    smaller = genSubsets(L[:-1])    # all subsets without the last element
    extra = L[-1:]      # create a list with just last element
    new = []
    for small in smaller:
        new.append(small + extra)   # for all smaller solutions, add one with last element
    return smaller + new            # combine those with last element and those without

# for the set of size k, we have 2^k cases
# so to solve need 2^n-1 + 2^n-2 +...+ 2^0

# tricky complexity
def h(n):
    """Assume n an int >= 0"""
    answer = 0
    s = str(n)
    for c in s:
        answer += int(c)
    return answer
# adds digits of a number together
# tricky part:
    # convert integer to a string
    # iterate over length of a string, not magnitude of input n
    # think of it like dividing n by 10 each iteration
# answer is O(log(n)) - reducing the size of the problem by a constant factor each stage


