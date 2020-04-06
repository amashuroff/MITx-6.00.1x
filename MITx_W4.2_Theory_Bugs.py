'''
Bugs:
    - isolate the bug
    - eradicate the bug
    - re-test until code runs correctly


Types of Bugs:
    Overt (очевидный) bugs:
        has obvious manifestation, code crashes or runs forever
    Covert bugs:
        no obvious manifestation, code returns a value, which may be incorrect, but hard to determine

    Persistent:
        occurs every time code runs
    Intermittent (прерывающийся):
        only occurs some times, even if run on the same input

Overt and intermittent bugs are harder to debug, but if conditions that prompt bug can be reproduced, can be handled

Covert bugs are highly dangerous, as user may not realize the answers are wrong, until code is being run for a long period
'''