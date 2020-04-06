import string

# Problem 3
def count7(N):
    """
    N: a non-negative integer
    """
    if N < 10:  # base case scenario, check the number which is lower than 10
        if N == 7:
            return 1
        else:
            return 0
    elif N % 10 == 7:
        return 1 + count7(N // 10)
    else:
        return 0 + count7(N // 10)


# Problem 4
def getSublists(L, n):
    """
    :param L: list of integers
    :param n: integer, 0<n<len(L)
    :return: list of sub_lists of length n, for every index of the L in range(len(L) - n + 1)
    """
    lst_of_sub = []
    for i in range(len(L) - n + 1):  # we want our sub_lists to be of length n, (0, 1) up to 2
        lst_of_sub.append(L[i: i + n])  # append sub_list of length n, (0, 1) up to 2
    return lst_of_sub


# print(getSublists([1, 2, 3], 2))


# Problem 5
# setdefault - adds keys,values that are not in your dictionary, doesnt changes already existing keys,values

dic = {'a': 1, 'b': 2, 'c': 3, 'g': 1}


def uniqueValues(aDict):
    """
    :param aDict: dictionary
    :return: returns a list of keys that map to integer values that are unique,
            sorted in an increasing order; if no values, returns an empty list
    """

    # create an empty dict
    new_dict = dict()
    # for every value in aDict, create a key in a new_dict, set this value as a key
    for value in aDict.values():
        new_dict.setdefault(value, 0)  # value from aDict acts as a key
        new_dict[value] += 1  # for every value in aDict we will count +1

    lst_of_unique_values = []
    for k, v in aDict.items():
        if new_dict[v] == 1:  # check if aDict value, that acts as a key in a new_dict, has been counted only 1 time
            lst_of_unique_values.append(k)

    return sorted(lst_of_unique_values)


# print(uniqueValues(dic))


# Problem 6
t1 = (1, 2)
t2 = ((1, 2), (1, 2))
t3 = ([1, 2], [1, 2])
l1 = [1, 2]
l2 = [(1, 2), 1, 2]
l3 = [[1, 2], [1, 2]]


def max_val(t):
    """ t: tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    result = 0
    i = 0
    for element in t:
        if type(element) == int:  # check if the element is not nested list or tuple
            if element > result:
                result = element
        else:
            recursive_result = max_val(t[i])
            if recursive_result > result:
                result = recursive_result
        i += 1
    return result
# print(max_val((5, (1,2), [[1],[2]])))


# Problem 7
def f(h,l):
    return h + l

def score(word, f):
    """
       word, a string of length > 1 of alphabetical
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26)
       times its distance from start of word.
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters.
       The first parameter to f is the highest letter score,
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the
           score for 'adD' is 12
    """
    two_highest_scores = []
    for i in range(len(word)):
        score_char = i * (string.ascii_letters.index(word[i].lower())+1)
        print(score_char)
        two_highest_scores.append(score_char)

    two_highest_scores.sort(reverse=True)
    return f(two_highest_scores[0], two_highest_scores[1])

# print(score('adD',f))




