
"""
Tuple is an ordered sequence of elements;
can mix element types;
immutable;
represented with parentheses;
t[0] --> element;
t[0:1] --> ('element',) extra comma tells that it is a tuple, if no comma, treats parentheses as scope, returns element;
t[0] = 4 --> error, can't modify tuples;
can add tuples;
used to swap variable values --> (x,y) = (y,x) take the opposite versions of tuple

"""


# used to return more then 1 value from a function
def quotient_and_remainder(x, y):
    q = x // y
    r = x % y
    return (q, r)

# (quot,remain) = quotient_and_remainder(4,5)


# can iterate over tuples
#aTuple is going to be a collection of tuples ((int,string),...,)
def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums += (t[0],)
        if t[1] not in words:
            words += (t[1],)

    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return min_nums, max_nums, unique_words

# small, large, u_words = get_data(((1,'mine'),
    #                                (3,'yours'),
    #                                (4,'mine'),
    #                                (8,'hi')))






# Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output,
# where every other element of the input tuple is copied, starting with the first one.
# So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'),
# then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

    i = 0
    t = ()

    while i < len(aTup):
        # we are adding tuples! use (,)
        t += (aTup[i],)
        i += 2

    return t

# print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))

# another solution, more clean and easy
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

    # return the same tuple sliced with the step of 2
    return aTup[::2]

# print(oddTuples(('I', 'am', 'a', 'test', 'tuple'))
