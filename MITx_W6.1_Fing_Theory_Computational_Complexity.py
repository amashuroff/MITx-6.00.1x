"""
How could we decide which option for program is the most efficient? (solution, algorithm)

Time and space efficiency are separated - trade-off

Challenges in understanding efficiency of a solution to a computational problem:
    - a program can be implemented in many different ways
    - you can solve a problem using only a handful of different algorithms
    - would like to separate choices of implementation from choices of more abstract algorithm

How to evaluate efficiency of programs?
    - measure with a timer
    - count the operations
    - abstract notion of order of growth

Order of growth - the most appropriate way of assessing the impact of choices of algorithm in solving a problem;
    and in measuring inherent(присущую) difficulty in solving a problem.

Timing programs is inconsistent:
start clock
call function
stop clock
    - running time varies between algorithms (okay)
    - running time varies between implementations (bad)
    - running time varies between computers (bad)
    - running time is not predictable based on small inputs (bad) (how it is going to scale?)
Time varies for different inputs but cannot really express a relationship between inputs and time

Counting operations:
assuming steps take constant time:
    - mathematical operations
    - comparisons
    - assignments
    - accessing objects in memory
then count the number of operations executed as function of size of the input
Counting operations is better, but still:
    - count depends on the algorithm (okay)
    - count depends on implementations (bad)
    - count independent of computers (okay)
    - no real definition of which operations to count (bad)
Count varies for different inputs and can come up with a relationship between inputs and the count

Timing and counting evaluate implementations
Timing evaluates machines

We want to express the efficiency in terms of an input, so need to decide what our input is going to be:
    integer
    length of a list
    or your decision given the multiple parameters to a function

Different inputs change how the program runs.
Think of the Best case, Worst case and an Average case.

Orders of growth (or complexity of the algorithm):
Goals:
    1. evaluate programs efficiency when input is very large
    2. express the growth of program's run time as input size grows
    3. want to put an upper bound on growth
    4. do not need to be precise: "order of" not exact "growth" growth
    5. look at the largest factors in runtime (which section of the program will take the longest to run?)

Measuring order of growth, Big Oh notation:
    Big Oh notation measures an upper bound on the asymptotic growth (often called order of growth)

    O() - used to describe the worst case:
        - worst case occurs often and is the bottleneck when program runs
        - express rate of growth relative to the input size
        - evaluate algorithm, not machine or implementation

    Worst case asymptotic behavior:
        - ignores additive constants
        - ignore multiplicative constants

Analyzing programs and complexity:
    Combine complexity statements:
        - analyze statements inside functions
        - apply some rules, focus on dominant term

    Law of Addition for O():
        used with sequential statements
        O(f(n)) + O(g(n)) is O(f(n) + g(n)) ---> O(n) + O(n*n) = O(n+n^2) = O(n^2) because of the dominant term

    Law of Multiplication for O():
        used with nested statements/loops
        O(f(n)) * O(g(n)) is O(f(n) * g(n)) ---> O(n) * O(n) = O(n*n) = O(n^2)

Asymptotic complexity - We describe running time in terms of number of basic steps
"""

# Finger exercises

# 1. What is the number of steps it will take to run Program 1 in the BEST case?
def program1(x):
    total = 0                   # +1
    for i in range(1000):       # +1000
        total += i              # +2000

    while x > 0:                # check if x > 0, in the BEST case x == 0, +1
        x -= 1
        total += x

    return total                # +1

# Answer is 3003 steps

# 2. What is the number of steps it will take to run Program 1 in the WORST case?
def program2(x):
    total = 0                   # +1
    for i in range(1000):       # +1000
        total += i              # +2000

    while x > 0:                # the worst case scenario is some large input x, it will check n times if x > 0
        x -= 1                  # +2*n
        total += x              # +2*n

    return total                # +1

# Answer is 3003 + 5n steps

# 3. What is the number of steps it will take to run Program 2 in the WORST case?
def program3(x):
    total = 0
    for i in range(1000):
        total = i               # +2003

    while x > 0:
        x = x//2                # +log2(n) since dividing by 2 every time
        total += x

    return total

# Answer is (5*log2(n)+1) + 2003

# Because we divide x by 2 every time through the loop, we only execute this loop a logarithmic number of times.
# log2(n) divisions of x by 2 will get us to x = 1; we'll need one more division to get x <= 0 .
#
# This while loop has five steps (one for the conditional check, x > 0, and two each for the //= and += operations).
# When we finally get to the point where x = 0, we execute the conditional check x > 0 one last time - since it is not,
# we do not enter the loop. Adding in one step for the return statement,
# in the worst case we execute 1 + 2*1000 + 5*(log2(n) + 1) + 1 + 1 = 5*log2(n) + 2008 steps.

# 4. What is the number of steps it will take to run Program 2 in the WORST case?
# WORST case is a list, sorted in an increasing order
def program4(L):
    totalSum = 0                # +1
    highestFound = None         # +1
    for x in L:                 # +n
        totalSum += x           # +2*n

    for x in L:                 # +n
        if highestFound == None:        # +n, statement is True only once, thus, highestFound = x only once. But check n times
            highestFound = x            # +1
        elif x > highestFound:          # +n-1, since first time, when if stmt is True, we don't execute elif
            highestFound = x            # +n-1

    return (totalSum, highestFound)     # +1

# Answer is 7 * n + 2


