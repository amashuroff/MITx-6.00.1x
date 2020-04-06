'''
Assertions - утверждения

    Want to be sure that assumptions
    on the state of computation are as expected

    Use assert statement to raise an
    AssertionError exception if assumptions not met

    Use of assertions is an example of
    good defensive programming

Assertions as defensive programming:
    - don't allow a programmer to control response to unexpected conditions
    - ensure that execution halts whenever an expected condition is not met
    - typically used to check inputs to function procedures, but can be used anywhere
    - can be used to check outputs of the function to avoid propagating (распространение) bad values
    - can make it easier to locate a source of the bug

Where to use assertions?
    goal is to spot bugs as soon as they introduced and make clear where they happened

    - use as supplement to testing
    - raise exceptions if user supplies bad data inputs

Use assertions to:
    - check types of arguments or values
    - check that invariants (что-то неизменяемое) on data structures are met
    - check constrains on return values
    - check for violations of constrains on procedure (e.g. no duplicates in a list)

Precondition:
"A precondition is a predicate that should hold upon entry into a function.
It expresses a function's expectation on its arguments and/or the state of objects that may be used by the function."

Postcondition:
"A postcondition is a predicate that should hold upon exit from a function."

'''

# example
def avg_grades(grades):
    assert not len(grades) == 0, 'no data is given'
    return sum(grades)/len(grades)

# example
def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    # we assert that max number is not equal to 0, if this condition is False, print 'Cannot divide by 0'
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers