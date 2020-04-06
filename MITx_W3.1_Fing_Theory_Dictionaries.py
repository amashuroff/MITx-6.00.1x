'''
Quick recap:
Common operators:
    seq[i] - get ith element of the sequence;
    len(seq);
    seq1 + seq2 - not for range;
    seq * n - sequence that repeat sequence n times (not for range);
    seq[start:end];
    e in seq;
    e not in seq;
    for e in seq;
Dictionary:
    index item of interest directly;
    all in one structure;
    Values:
        any type can go into dict (mutable, immutable);
        can be duplicates;
        even other dictionaries;
    Keys:
        must be unique;
        immutable - (int,float,bool, string, tuple), careful with floats.
        need an object that is  hashable
    No Order

List vs Dict:
    List:
        ordered sequence of characters;
        look up elements by an integer index;
        indices have an order;
        index is an integer;
    Dict:
        matches 'keys' to 'values';
        look up one item by another item;
        no order is guaranteed;
        key can be any immutable type.

Global variables:
    it may be dangerous to use:
        breaks the scoping of variables that we get by a function call; (remember recursive example) (we can move value out of scope)
        allows for side effects of changing the variable values in ways that affect other computation;
    but can be really convenient to use:
        when want to keep track of information inside a function





'''

dict = {}
# give me the value associated with the key - dict['key']

# can create new entires, (only works with keys)
dict['key'] = 'Value'

# test if key in dict (in statement only works with keys)
'key' in dict

# delete entry from the dict
# del(dict['key'])

# get all the keys, iterable
dict.keys()

# get all the values, iterable
dict.values()

# list comprehension using dict
namesDict = {"Nora": 56, "Lulu": 15, "Gino": 31}
oddValues_1 = [value for value in namesDict.values() if value % 2 != 0]
# it is equivalent to using
oddValues_2 = []
for value in namesDict.values():
    if value % 2 != 0:
        oddValues_2.append(value)

# dictionary comprehension
# basic syntax (example?) <variable> = { key:new_value for (key, value) in <dictionary>.items() }
# example 1
grades = {"Nora": 90, "Lulu": 15, "Gino": 60}
doubleGrades = {key: value*2 for (key, value) in grades.items()}
# >>> doubleGrades
# >>> {'Nora': 180, 'Lulu': 30, 'Gino': 120}

#example 2 using condition statement
grades_2 = {"Nora": 90, "Lulu": 15, "Gino": 60}
doubleGrades_2 = {key: value*2 for (key, value) in grades.items() if value % 2 == 0}
# >>> doubleGrades
# returns new dictionary with the applied condition (notice value %2 != 0 is not included) (read with return)
# >>> {'Nora': 180, 'Gino': 120}


# example 3. Functions to analyse song lyrics
# IDEA: from song dictionary, find most frequent word. Delete this word, repeat (mutate for fun)

# 1) create a frequency dictionary int:str (word for the number of appearances)

# lyrics_str1 = ['hi', 'hello', 'i', 'b', 'am']

def lyrics_to_frequencies(lyrics):

    my_dict = {}
    for word in lyrics:
        # (in) in dict applies only to keys
        if word in my_dict:
            # updating the value associated with the key
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    return my_dict

# 2) find the word that occurs the most, and how many times:
#   list in case word > 1
#   return a tuple (list, int) for (words_list, highest_freq)

def most_common_word(freqs):
    # extract frequencies from the dictionary, (return a list with values?)
    values = freqs.values()
    # find max occurrence of words (returns an int?)
    max_freq = max(values)
    # set a list to store words with highest occurrence (frequency)
    words_with_max_freq = []

    # find the words that match max occurrence
    for words in freqs:
        if freqs[words] == max_freq:
            words_with_max_freq.append(words)

    return words_with_max_freq, max_freq
# words,frequency = most_common_word(lyrics_to_frequencies})
# we get the tuple, where we see the words and their occurrence

# 3) find the words that occur at least X times:
#   user choose X times (min_times here)
#   return a list of tuples (list of words ordered by frequency)
# LEAVE IT AS IT IS
def words_often(freqs, min_times):
    result = []
    # set switch for the for loop
    done = False
    # set temporary list
    temp = most_common_word(freqs)
    print(temp)
    while not done:
        if temp[1] >= min_times:
           #  print(temp[1])
            result.append(temp)
           # print(result)
            for w in temp[0]:
               # print(temp[0])
               # print(w)
               # print(freqs[w])
               del(freqs[w])
        else:
            done = True
    return result

# Exercise 1, how many animals?
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


# my solution
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    counter = 0
    for key in aDict:
        for word in aDict[key]:
            counter += 1
    return counter


# other solutions of the same exercise
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for value in aDict.values():
        # Since all the values of aDict are lists, aDict.values() will
        #  be a list of lists
        result += len(value)
    return result


def how_many(aDict):
    '''
    Another way to solve the problem.

    aDict: A dictionary, where all the values are lists.

    returns: int, how many individual values are in the dictionary.
    '''
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result


# Exercise 2, biggest number of lists
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = 0
    biggest = 0
    # check every key in the dictionary
    for key in aDict:
        # if the length of the list inside is > than biggest
        if len(aDict[key]) > biggest:
            # set biggest = to this length
            biggest = len(aDict[key])
            # set the result to key
            result = key
    return result


# Fibonacci recursive case vs Memorization technique
# Recursive Fib
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
# it is very slow because it keeps track of all new values, that are already know

# Memorization technique using dictionaries, keeping track of what you already know
d = {0:0, 1:1}
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        # stores all the results in dict, so it is much easier to access them, just check if n is in d
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans


# Memorization technique using dictionaries, keeping track of what you already know
