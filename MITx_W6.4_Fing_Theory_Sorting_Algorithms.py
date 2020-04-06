"""
Sorting algorithms:
    Monkey sort (aka bogo sort, stupid sort, slow sort, permutation sort, shotgun sort):
        randomly assign the elements into the list, then look at them and say: "are they sorted?", if not, repeat.
        complexity of bogo sort:
            1. best case - O(n), where n is len(L)
            2. worst case - O(?) is is unbounded if really unlucky

    Bubble sort:
        1. compare consecutive pairs of elements
        2. swap elements in pair such that smaller is first
        3. when reach end of the list, start over again
        4. stop, when no more swaps have been made

    Selection sort:
        1. extract minimum element, swap it with the element at index 0
        2. in the remaining sublist, extract minimum element, swap it with the element at index 1
        3. keep the left portion of the list sorted:
            at the i'th step, first i elements in the list are sorted
            all other elements are bigger than first i elements

Analysing selection sort:
    loop invariant:
        given prefix of list L[0:i] and suffix L[i+len(L)], then
        prefix is sorted and no element in prefix is larger than the smallest element in suffix
            1. base case: prefix is empty, suffix is a whole list - invariant is True
            2. induction step: move minimum element from suffix to end of prefix.
                Since invariant is True before move, prefix is sorted after append
            3. when exit, prefix is an entire list, suffix is empty, so prefix is sorted

    Merge sort:
        divide and conquer approach:
            1. if list of length 0 or 1 - already sorted
            2. if list has more than 1 element, split into 2 lists, and sort each
            3. merge sorted sub-lists:
                1. look at the first element of each, move smaller, to end of the result
                2. when 1 list is empty, copy rest of other list


"""
# complexity of bubble sort
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp

# inner for loop is doing comparisons
# outer while loop is doing multiple passes until no more swaps
# complexity is O(n^2) where n is len(L), to do len(L)-1 comparisons and len(L)-1 passes

# complexity of selection sort
def selection_sort(L):
    suffixSt = 0
    while suffixSt != len(L):
        for i in range(suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] = L[i], L[suffixSt]
        suffixSt += 1
# complexity is O(n^2) where n is Len(L)

# alternative version of selected sort
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp

# alternative version of selected sort
def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1

# merging example (not merge sort algorithm)
def merge(left, right):
    """
    :param left: sorted sublist
    :param right: sorted sublist
    :return: merged sorted list
    """
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # move indices for sublists depending on which sublist is holding the smallest next element
    while (i < len(left)):      # when right sublist is empty
        result.append(left[i])
        i += 1
    while (j < len(right)):     # when left sublist is empty
        result.append(right[j])
        j += 1
    return result
# complexity is O(len(left) + len(right)) copied elements, but O(len(longer list)) comparisons, so overall O(n)

# merge sort algorithm, putting together
def merge_sort(L):
    if len(L) < 2:
        return L[:]                         # base case
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])       # dividing lists in halves
        right = merge_sort(L[middle:])
        return merge(left, right)           # conquering with merge step
    # depth-first, such that conquer smaller pieces down one branch first, before moving to larger pieces
# complexity of 2 pieces (merge and merge sort):
    # O(n) for different levels or recursion (linear amount of work to do the merge)
    # O(log n) for dividing lists in halves with each recursive call
    # overal complexity is O(n log n) where n is len(L)





