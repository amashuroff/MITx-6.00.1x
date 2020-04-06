'''
Computer can do only 2 things:
    1. computations
    2. remembering things

Type of knowledge that is used in computations:
    declarative:
        statements of fact, truths
    imperative:
        1. recipe (algorithm)
        2. sequence of steps
        3. flow of control (process that tells the order of steps exec)
        4. means of determining where and when to stop

An algorithm is a conceptual idea, a program is a concrete instantiation of an algorithm.


Fixed program - calculator, Turings Bombe

Stored program:
    sequence of instructions stored inside computer:
        build from predefined set of primitive instructions:
            1. arithmetic and logic
            2. simple tests
            3. moving data

Special program (interpreter):
    executes each instruction in order:
        use tests to change the flow of control through sentence;
        stop when done.
        it is machine that stores and executes instructions, it emulates fixed program computer for each loaded program.

Basic primitives:
    Alan Turing showed that you can compute anything using 6 primitives:

Print vs Return
    if we print something, it returns NoneType, and it prints something, simple as that.
    returning something will use that something in further computations

Short-Circuit evaluation(or, and, comparison):
    If we already know that the and operator returns False when either one of the expressions is False,
    there is no need to evaluate to second expression if we already know that the first expression is False.
    works also with numbers, but returns value except of Bool.
    ( 4 and 5 - if the first value evaluates to True, the second value is evaluated and returned >>> 5)
    ( 4 and 0 >>> 0)
    ( 0 or 4 >>> 4)

String - sequence of characters

Comparing strings:
    sequence objects can be compared to other objects with the same sequence type
    the comparison uses lexicographical ordering:
        the 2 first items are compared, if one of the differs, this determines the whole outcome
        if the 2 first items are equal, comparison continues

Unicode code point number is used by lexicographical ordering to order individual characters:
    ord('a') returns 97, can also be used to find order of (!@#$%^ etc.)

For vs While loop:
    For:
        know n of iterations
        end early with break
        uses counter
        can re-write for loop with while loop
    While:
        unbounded n of iterations
        end early with break
        can use counter but must initialize before loop, and increment inside loop
        may not be able to re-write while loop with for loop

Truthy and Falsy values:
    Truthy value is is value that is considered True when evaluated in the Boolean context

    Truthy:
        any number that is not 0
        any string that is not empty
        None acts as a falsy value
    test if the value is truthy or falsy by using bool(value_to_be_tested)

Branching structures (if, else, elif):
    let us jump to different pieces of code, based on a test
    programs are constant time (only go through the code once)

Looping structures:
    programs now take time that depends on values of variables, as well as the length of the program

Nested loops:
    use different variables for each loop
    for every iteration of the for/while loop, inner loop will be executed completely

Loop characteristics:
    need a loop variable:
        init outside the loop
        changes within the loop
        test for termination depends on a variable
    think about a decrementing function when designing a loop

Guess and check:
    {guess a value for the solution
    check if the solution is correct
    keep guessing until find the solution or guessed all the values} - process is called exhaustive enumeration


'''

# concatenation of the strings
hw = "hello" + "world"
# successive concatenation
hw3 = "steve" * 3
# slicing: string[start:end:step]
# copy of the string: string[:]

# printing out everything with spaces in between
# print('Hello', 'World', 'I am')
# concatenate the everything in one string
# print('Hello' + "World" + 'I am')


# if <statement of fact> is true, print hi, but 0 itself is False, meaning the else statement is being printed
if 0:
    print('hi')
else:
    print('bye')

num = 5
# evaluates to True
while num:
    if num > 10:
        break
    print('hi')
    num += 1

# evaluates to True
if 'string':
    print('hi')
else:
    print('bye')

# evaluates to False
if '':
    print('a')
else:
    print('b')

# clean guess and check method
cube  = 8

for guess in range(cube+1):
    if guess**3 == cube:
        print("cube root of x is {}".format(guess))
