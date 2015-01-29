# 6.00 Problem Set 3
# 
# Hangman game
# Jan 27 2015
# -----------------------------------
from sys import exit
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string #### Could also be read() however all word on same line
    line = inFile.readline()
    # wordlist: list of strings the string part is what to split on
    # if blank or as it is written then .split on spaces
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

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
    # Create a list version of secretWord so I can removed 'found' letters
    x = [x for x in secretWord]
    for i in x[:]:
        if i in lettersGuessed:
            x.remove(i)
    return len(x) == 0


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    # Check if the letter in the secretWord is in lettersGuessed
    # Build a list of either the letter guessed or a "_ "
    output = []
    
    for i in secretWord:
        if i in lettersGuessed:
            output.append('{}'.format(i))
        else:
            output.append('_')
    return ' '.join(map(str, output))


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    
    import string
    x = list(string.ascii_lowercase)
    
    for i in lettersGuessed:
        if i in x:    ## this was added since I got an error when updating var.
            x.remove(i)
    return '-'.join(map(str, x)) 

def bonusSocre(lettersGuessed):
    '''
    lettersGuessed: will be a list of letter and '_',
    check how many '_' are in the list and then apply,
    '_' times 13 to give 13 extra percent to score
    This is done by calling the getGuessedWord() function
    to generate a list of '_' for unguessed letters,
    which are used to calculate the bonus  
        
    returns: integer of bonus amount
    '''
    bonus = sum(1 for x in lettersGuessed if x == '_')
    bonus *= 13.0
    return bonus
    
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.
    * Or the user may try and just guess the word.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    
    print "Welcome to the game hangman!"
    print "I am thinking of a word that",
    print "is {0:d} letters long.".format(len(secretWord))
    
    guesses = []
    attempt = 8
    main_word = secretWord
    
    
    while not isWordGuessed(main_word, guesses) and attempt > 0:
        # able to update the string of available letter 
        choose_from = getAvailableLetters(guesses)
                 
        print '-' * 11
        print "You have {0:d} guesses left.".format(attempt)
        print "Available letters: {0}".format(choose_from)
        
        current_guess = raw_input("Please guess a letter, or even a guess: ").lower()
        
        if len(current_guess) == 1:
            guesses.append(current_guess)
            output_update = getGuessedWord(main_word, guesses)
            ## check to see if guess in main_word and the available letter
            if guesses[-1] in main_word and guesses[-1] in choose_from:
                print "Good guess: {0}".format(output_update)
            elif not guesses[-1] in choose_from and guesses[-1] in main_word:
                print "Oops! You've already guessed",
                print "that letter: {0}".format(output_update)
            elif not guesses[-1] in choose_from:
                print "Oops! You've already guessed",
                print "that letter: {0}".format(output_update)
            else:
                print "Oops! That letter is not",
                print "in my word: {0}".format(output_update)
                attempt -= 1
        elif len(current_guess) == len(main_word):
            output_update = getGuessedWord(main_word, guesses)
            if current_guess == main_word:
                bonus = bonusSocre(output_update)
                print "Congratulations, You WON!"
                print "Main score is: {0:.2f}%".format((attempt/8.0)*100)
                print "{0} ===>>  {1}".format(output_update, main_word.upper())
                print "For a added bonus of {0:.2f}%".format(bonus)
                print "TOTAL: {0:.2f}%".format(((attempt/8.0)*100) + bonus)
                exit(0)               
            else:
                print "That is not the correct word.",
                print "Try again! {0}".format(output_update)
                attempt -= 1
        else:
            print "Your guess was not the correct amount of characters"
            attempt -= 1
    print '-' * 11
    
    if isWordGuessed(main_word, guesses):
        print "Congratulations, YOU WON! Word = {0}".format(main_word.upper())
        score = (attempt / 8.0) * 100
        print "Total score is: {0:.2f}%".format(score)
        print "Next time try to guess the word to get the added bonus!"
    else:
        print "Sorry you ran out of guesses.",
        print "The word was {0}".format(main_word.upper())
        print "Score of ZERO!"
    
            


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
#secretWord = "test"
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
