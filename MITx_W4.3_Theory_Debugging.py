'''
Being able to debug is a steep learning curve

tools for debugging:
    - build into IDLE or Anaconda
    - python Tutor
    - print statement
    - your brain, be systematic in your hunt


Print statements:
    good way to test hypothesis
    when to print:
        enter the function
        parameters
        function results

    use bisection method:
        put print halfway in code
        decide where bag may be depending on values


Error messages:
    IndexError - trying to access beyond the limits, boundaries (of a list for example)

    TypeError - converting something to a type that i can't

    NameError - referencing a non-existent variable

    TypeError - mixing data types without appropriate coercion (принуждение)

    SyntaxError - forgetting to close parenthesis, quotation, etc.


Logic Errors - HARD:
    think before writing a code
    draw pictures, take a break
    explain the code to somebody/something

Debugging steps:
    Study program code:
        ask how did i get an unexpected result?
        don't ask what is wrong
        is it part of the family?

    Scientific method:
        - study available data
        - form hypothesis
        - repeatable experiments
        - pick simplest input to test with


DON'T:
    - write an entire program
    - run an entire program
    - debug entire program

    also don't
    - change the code
    - remember where bug was
    - test code
    - forget where bug was, or where change was made
    ---> Panic

DO's:
    - write a function
    - test the function
    - write a function
    - test the function, debug the function
    - do integration testing

    also do's
    - backup code
    - change code
    - write down potential bug in a comment
    - test code
    - compare new version with an old version



Practical hints:
    - look for the usual suspects
    - ask why the code is doing what it does, not why it is not doing what you want
    - the bug is probably not where you think it s - eliminate locations
    - explain the problem to someone else
    - don't believe the documentation
    - take a break and come back to the bug later
'''

# assert --> exception handling operator, that executes code and terminates the function if some specified assuptions
# are not met

# assertion - утверждение/предположение
# assert - утверждать/предполагать

# Bisection search and Binary search mean the same thing
# hash table == dictionary in python