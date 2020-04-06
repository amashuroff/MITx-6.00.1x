"""
Approximate solutions - using something that will tell me if i am close enough


Bisection search - see notepad, works well with problems having an ordering property.
Ordering property - value of the function varies monotonically with the input value

Bisection algorithm:
If our answer squared is too small, the algorithm will discard the half of the search space that contains numbers smaller than our answer,
and our new search space will be the other half that contains numbers larger than our previous answer.
Our new Low will be the previous answer (the middle point of the previous search space) and our High point will remain the same.

On the contrary, if our answer squared is too large to be the right answer,
the algorithm will discard the HALF of the search space that contains numbers Larger than our previous answer.
Our new High point will be the previous answer (the middle point of the previous search space) and our Low point will remain the same.


Newton_Raphson method:
simple case: cx**2 + k
first derivative: 2cx

NR says: given a guess g for root, a better guess is g - g(**2 - k)/2g (k in our example is cube of a number)

"""


#cheers exercise
an_letters = "abcdefghigklmnopqrstuvxyz"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level(1-10): "))
i = 0

while i < len(word):
    char = word[i].upper()
    print('Give me ' + char + '! ' + char)
    i += 1
print('What does it spell?')

for i in range(times):
    print(word.upper() + '!!!')


# approximation of the cube root exercise, num of guesses is very large: thousands
cube = int(input("What is the number you want to find a cube root of? "))
epsilon = 0.01 # difference between the answer and the cube of the number (how close we are?)
guess = 0.0
increment = 0.1
num_of_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_of_guesses += 1
if abs(guess**3 - cube) >= epsilon:
    print("Failed to find the cube root of ",  cube)
else:
    print("{} is close enough to cube root of {}".format(guess,cube))


# bisection search, finding the cube root example,
# faster algorithm, in our example was not greater than 100 num of guesses
cube = 10
epsilon = 0.01
num_of_guesses_1 = 0
low = 0
high = cube
guess = (low+high)/2.0

while abs(guess**3 - cube) >= epsilon:
    # if the guess is low, but is greater than or equal to epsilon
    if guess**3 < cube:
        # too low, set guess(in the middle) to be the lower bound
        low = guess
    # if the guess is too high, and is greater than or equal to epsilon
    else:
        # too high, set our guess to be the upper bound
        high = guess
    # re-set our guess to be in the middle between low and high bound
    guess = (high+low)/2.0
    num_of_guesses_1 += 1
print("num_guesses =", num_of_guesses_1)
print(guess, 'is close to the cube root of', cube)


# another example of the bisection search, guess my number
# print('Please think of a number between 0 and 100')
high_1 = 100
low_1 = 0
guessed = False

while not guessed:
    guess_1 = (high_1+low_1)//2
    print('Is your secret number is ' + str(guess) + '?')
    user_inp = input(
        "Enter 'h' to indicate the guess is too high. "
        "Enter 'l' to indicate the guess is too low. "
        "Enter 'c' to indicate I guessed correctly: ")

    if user_inp == 'c':
        guessed = True

    elif user_inp == 'h':
        high_1 = guess_1
    elif user_inp == 'l':
        low_1 = guess_1

    else:
        print("Sorry, i don't understand your input...")
print("Game over. Your secret number was: " + str(guess))


# example of the Newton-Raphson method of finding solution to any equation, in our example took no more than 5-7 guesses
epsilon = 0.01
y = 'num we want to find the cube root of '
num_of_guesses_2 = 0

while abs(guess*guess - y) >= epsilon:
    num_of_guesses_2 += 1
    guess = guess - (((guess**2)-y)/(2*guess))
print("The number of guesses is: " + str(num_of_guesses_2))
print("Square root of " + str(y) + 'is about' + str(guess))


# bisection search, is character in a string
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 1:
        return char == aStr
    if aStr == '':
        return False
    m = aStr[len(aStr) // 2]
    if char == m:
        return True
    else:
        if char < m:
            return isIn(char, aStr[:len(aStr) // 2])
        if char > m:
            return isIn(char, aStr[len(aStr) // 2:])
    return isIn(char, aStr)

# fibonacci numbers
def fib(x):
    """
    :param x: assumes x >= 0
    :return: Fibonacci of x
    """
    if  x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

# is palibdrome recursive
def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in "abcdefhigklmnopqrstuvwxyz":
                ans += c
        return ans

    def isPal(s):
        # it is a palindrome if len is 1
        if len(s) <= 1:
            return True
        else:
            # check the first and last char and then slice and do the same check again
            return s[0] == s[-1] and isPal(s[1:-1])