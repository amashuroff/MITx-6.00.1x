"""
Search algorithm:
    method for finding an item or group of items with specific properties within a collection of items

Collection could be implicit (неявный):
    example: find square root as a search problem:
        - exhaustive enumeration
        - bisection search
        - Newton - Raphson
Collection could be explicit:
    example: is a student record in a stored collection of data?

Searching algorithms;
    1. linear search:
        - brute force search (british museum search) - looking through all possible versions, until find a solution
        - lists does not have to be sorted
    2. bisection search (binary):
        - lists MUST be sorted to give correct answer



"""

# linear search on an unsorted list
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found
# overal complexity is O(n) where n is len(L)

# linear search on a sorted list
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
# running time is faster, but complexity still O(n)


# Bisection search, (divide and conquer algorithm)
    # 1. pick the index i, which divides list in half
    # 2. ask if L[i] == e
    # 3. if not, ask if L[i] is larger or smaller than e
    # 4. depending on the answer, search lef or right half of L for e
# complexity of bisection search is O(log n) where n is len(L)
# finished looking through a list when 1 = n/2^i (i-th power), so i = log n

# bisection search 1
def bisection_search1(L, e):
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisection_search1(L[:half], e)
        else:
            return bisection_search1(L[half:], e)
# O(log n) bisection search calls
# O(n) for each bisection search to copy the list
# complexity is O(n log n)
# O(n) for a tighter bound, because length of list is halved each recursive call


# bisection search 2
def bisection_search2(L, e):
    def bisection_search_helper(L, e, low, high):
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid:      # nothing left to search
                return False
            else:
                return bisection_search_helper(L, e, low, mid - 1)
        else:
            return bisection_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisection_search_helper(L, e, 0, len(L) - 1)
# pass list and indices as parameters
# list is never copied, just re-passed
# complexity is O(log n)
