# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/MITx/MITx_W3_PSET_3/words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    for char in secretWord:
        if char not in lettersGuessed:
            result += " _ "
        else:
            result += " {} ".format(char)
    return result


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


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman. play = True, while true

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round. input

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    play = True
    num_of_guesses = 8
    lettersGuessed = []

    while play:

        print("Welcome to the game Hangman!")
        print("I am thinking of a word that is {} letters long.".format(len(secretWord)))
        print("-" * 11)

        # while number of guesses wil not become 0 or the word would not be guessed
        while num_of_guesses != 0 and isWordGuessed(secretWord, lettersGuessed) == False:
            print("You have {} guesses left".format(num_of_guesses))
            print("Available letters: {}".format(getAvailableLetters(lettersGuessed)))
            ask_user_input = input("Please guess a letter: ")
            # check if the user input is already in the list of guessed words
            if ask_user_input in lettersGuessed:
                print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
                print("-" * 11)
                pass
            # if not in the guessed words, append a new word to the list
            else:
                lettersGuessed.append(ask_user_input)
                # check if the guessed word is in secret word, if yes, it's a guess
                if ask_user_input in secretWord:
                    print("Good guess: {}".format(getGuessedWord(secretWord, lettersGuessed)))
                    print("-" * 11)

                else:
                    print("Oops! That letter is not in my word: {}".format(getGuessedWord(secretWord, lettersGuessed)))
                    num_of_guesses -= 1
                    print("-" * 11)
        # if number of guesses == 0, the game is over
        if num_of_guesses == 0:
            print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))
            play = False
        # if the secret word was guessed, the game is over
        elif isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            play = False

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)

