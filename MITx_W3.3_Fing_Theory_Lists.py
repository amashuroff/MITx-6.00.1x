'''
List is an ordered sequence of information, accesible by index;
list elements can be changed, it is mutable;
index can be a variable or an expression;
indexes have an order;
L[1] = 5 - change the second element of the list to be 5, returns the same object;
x[0:1] --> [1], notice how tuple (1,) are different to the list given the same index slicing;
'''

# iterate over list using index
L = [1,2,3]
total = 0
for i in range(len(L)):
    total += L[i]

# print(total)

# iterate over list using list elements
total = 0

for element in L:
    total += element

# add elements to the end of the list, it is actually changes the list itself (mutates the list)
L.append(element)

# concatenate lists
# notice that L1 and L2 itself are not changed, not mutated
L3 = L1 + L2

# extend the list itself, L is changed, mutated
L.extend([list])

# delete elements at the specific index, mutates the list
del(L[index])

# delete element from the end of the list, mutates the list
# can use index to delete the item you want
L.pop()

# remove a specific element in the list, mutates the list
# if multiple elements, removes first occurence
# if element not in list, gives error
L.remove(element)

# convert string to a list
# returns a list with every char in list
list(string)

# split a string on a character parameter
# if called without param. splits on spaces
# returns a list
s = 'abc'
s.split('b')

# turn a list of characters into a string
# give a character in quotes to add char between every element
#returns a string
''.join(L)
'_'.join(L)

#sort a list, method mutates the list, doesnt return anything
L.sort()

#sort a list and return a new version of it
sorted()

#reverse the list, mutate
L.reverse()

#range() returns something that behaves like a tuple
# it does not generate the elements at once, rather it generates the first element,
# and provides an iteration method by which subsequent elements can be generated


# Insert an item at a given position.
# The first argument is the index of the element before which to insert, so a.insert(0, x),
# inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x)
L.insert()


# to see the index of the value in a list
L.index(value,integer,char)

# basic rules syntax for list comprehension
# [<value_to_include> for <elem> in <sequence> if <condition> (if statement is optional)]

# list comprehension(понимание) - compact way to create lists
list1 = [i for i in range(15) if i % 2 == 0]

#example of the list comprehension (read with return)
list1 = [i * 3 for i in range(15) if i % 2 == 0]

