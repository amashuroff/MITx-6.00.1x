'''

We refer to functions as first-class objects, meaning:
    it has a type;
    can be used as elements of data structures like lists;
    can appear in expressions:
        as part of an assignment statement;
        as an argument of a function.

Usefull to use functions as arguments, when coupled with lists:
    aka(also known as) higher order programming.

HOP - higher order procedure, map
map() - takes a function and applies itself to all elements in the list:
    produces an iterable


'''

# apply the function to each element on the list
def apply_to_each(L,f):
    '''
    :param L: list
    :param f: function
    :return: replaces every element of the L by f(L)
    '''
    for i in range(len(L)):
        L[i] = f(L[i])

# apply list of functions to the argument x
def apply_to_each_2(L,x):
    for f in L:
        print(f(x))

# map produces structure that looks like a list,
# but need to walk down, iterate over, to get back out
for element in map(abs, [1,-2,3,-4]):
    print(element)

# only tells that it is an object and it is located in memory
map(abs, [1,2,3,-4])

# n-ary function, expects n arguments
L1 = [1,23,4]
L2 = [1,2,3,45,6]
# takes first elements of the 2 lists
# applies function
# here it gives the minimum between two functions
for element in map(min, L1, L2):
    print(element)

