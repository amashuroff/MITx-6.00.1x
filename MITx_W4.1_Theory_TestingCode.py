'''
High-Quality programming


Testing

Defensive programming:
    How you structure your code in a way that plans ahead, to make sure you avoid bugs, or detect them.

Debugging:
    Eliminating source of bugs



Defensive programming:
    1. Write specifications for the functions (docstrings)
    2. Modularize programs (braking it up on obvious pieces)
    3. Check the conditions for Inputs/Outputs (assertions)

    Testing validation:
        Comparing Inputs/Outputs (set of example Inputs, and what do I expect)
        How i can break my program? Test all different cases.

    Debugging:
        Study events leading to an error
        "Why is it not working?"
        "How i can fix my program?"


Set yourself up for easy testing and debugging!
    From the start, design code to ease this part.
    Break the program into simple modules (self-contained)
    Write document constrains on modules. "What input/output expect?"
    What are the document assumptions behind the code design?
        (code will be entered in a manner that supports these assumptions)


"Motherhood and apple pie approach":
    Something that cannot be questioned because it appeals to universally-held, wholesome values

When to you are ready to TEST?
    1. ensure code runs
    2. have a set of expected results

Classes of tests:
    1. Unit testing (testing each function in each module)
    2. Regression testing (catch reintroduced errors and bugs, after fixing one)
    3. Integration testing (overall program)


Testing approaches:
    1. Intuition about natural boundaries of a problem
        Can you come up with some natural partitions? (преграды)
        If no natural partitions, might use random testing

    2. black box testing
        Explore all paths through specifications

    3. glass box testing
        explore paths through code


Black box testing:
    designed without looking at the code
    can be done by other people to avoid some implementer biases
    can be reused
    paths through specification:
        testing in natural space partitions
        consider boundary conditions (empty lists, large nums, small nums)

Glass box testing:
    use code directly to guide design of test cases
    path-complete, if every potential path through code is tested at least once
    Drawbacks:
        can go through loops arbitrarily many times
        missing paths

    Guidelines:
        1. branches - exercise all parts of the conditional
        2. for loops - tests where loop not entered, body executed exactly once, more then once
        3. while loops - same as for the for loop, test all cases that catch all ways to exit the loop
'''


