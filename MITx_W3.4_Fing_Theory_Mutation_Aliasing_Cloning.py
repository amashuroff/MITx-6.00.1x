'''

Alias: псевдоним - if I change the variable under 1 name, it also changes under the other name (assignment)
    it points to the same place.

Mutation: aliasing can be useful, but if we mutate for example one list, to which the other list is pointing,
    we will also change the values in the last one;
    Avoid mutation while iterating over a list. See example
    To solve this problem, make a new list, or make a copy

Even if 2 lists print the same thing, id doesn't mean that they represent the same structure

Cloning: copy every element from a list using chill = cool[:]
    both lists print the same thing, but they refer to different structures

1. Assignment never copies data.
2. Python is neither "Call By value" nor "Call By Reference", it's "Call by Assignment"!
3. There is no way in python where a name can refer to another name. A name can only refer to values.

Difference between == and is operators:
== checks if values of the operands are the same
is checks if operands refer to the same object or not
'''


warm = ['good', 'freaking', 'weather']
# cold is an alias for warm, it points to the same place
# append() will have effect on both
cold = warm

# one more sorting comment
warm = ['red', 'yellow', 'green']
# this will print None, since the sorted_warm has no value, it has been already changed (warm was sorted)
# and now pointing to the different value, while the old value has been vanished
sorted_warm = warm.sort()

cool = ['grey', 'white', 'black']
# cool list will not be changed
sorted_cool = sorted(cool)

# example of the mutation in the for loop
# remove() mutates the list, changes its size
# which causes python to never see the next element of the list
# after first iteration the list size has changed
# and the second element is no longer 2 its 3 (L1 = [2,3,4])
L1 = [1,2,3,4]
L2 = [1,2,5,6]
def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)

def remove_dups1(L1,L2):
    # L1 is now pointing to the different structure
    L1_copy = L1[:]
    for e in L1:
        if e in L2:
            L1.remove(e)
    return L1_copy