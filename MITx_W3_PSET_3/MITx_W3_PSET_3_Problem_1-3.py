"""
.join method - returns a string concatenated with the elements of an iterable.
all() - all True for some iterable
any() - any True for some iterable

"""
import string



secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

# function that checks if the user guessed the word and returns True/False
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    # for every character in the secret word
    for char in secretWord:
        # check if character is in guessed list of letters
        if char not in lettersGuessed:
            # if at least one of the char not in secret word, stop and return False
            return False
    # if the for loop end without False statement, it means that all characters are guessed
    return True


# one line version of the function
def isWordGuessed2(secretWord, lettersGuessed):

    return all([True if char in lettersGuessed else False for char in secretWord])


# print(isWordGuessed(secretWord, lettersGuessed))
# print(isWordGuessed2(secretWord, lettersGuessed))

# function that prints out the guessed charachters of the secret word
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    # store characters in a string
    result = ""
    for char in secretWord:
        if char not in lettersGuessed:
            result += " _ "
        else:
            result += " {} ".format(char)
    return result


# print(isWordGuessed3(secretWord, lettersGuessed))
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''

    result = ''

    for char in string.ascii_lowercase:
        if char not in lettersGuessed:
            result += char

    return result

# print(getAvailableLetters(lettersGuessed))