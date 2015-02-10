from ps4a import *
import time
import sys

#
#
# Problem #6: Computer chooses a word
#
#


def isValidWord_new(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # just made copied since they should not be mutated
    xhand = hand.copy()
    xwordlist = wordList[:]
    
    # loop through the index of the word
    for i in range(len(word)):
        if word[i] in xhand.keys(): # this xhand.key() will update by del 
            xhand[word[i]] -= 1
            if xhand[word[i]] == 0:
                del xhand[word[i]]
        else:
            return False
    return True
    
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0
    current_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord_new(word, hand, wordList):
            # Find out how much making that word is worth
            current_score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if current_score > max_score:
                # Update your best score, and best word accordingly
                max_score = current_score
                best_word = word
    # return the best word you found.
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    total = 0
    compWordScore = 0
    while calculateHandlen(hand) > 1:
        # Display the hand
        print('Current hand: ', end=' ') 
        displayHand(hand)
        compWord = compChooseWord(hand, wordList, n)
        
        # If computer does not find a word:
        if compWord == None:
            break
            # End the game (break out of the loop)    
        # Otherwise (there is a word found):
        else:
            compWordScore = getWordScore(compWord, n)
            total += compWordScore
            print('"{0}" earned {1} points'.format(compWord, compWordScore), end=' ')
            print('Total: {0:d}'.format(total))
            print('')
            hand = updateHand(hand, compWord)
            # I dont know why but needed this for edX Grader.
            #for k, v in hand.items():
                #if v == 0:
                   # del hand[k]
                
            # Update the hand
    
    # different outcomes if the hand is now empty or not            
    if calculateHandlen(hand) == 0:
        print('Total score: {0:d} points'.format(total))
    # Game is over (Computer did not find word!), so tell user the total score
    else:
        print("Total score: {0:d} points".format(total))
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    playedHand = False
    trigger = True
    choice = ''
    while trigger:
        
        try:
            if choice == '' or choice not in 'ern': 
                choice = input('Enter n to deal a new hand, r to replay the '
                                   'last hand, or e to end game: ')
                print('')
                if choice not in 'ern':
                    raise ValueError('Invalid input, please try again!')
                if choice == 'e':
                    #sys.exit(0)
                    trigger = False
                    break
                if choice == 'r' and playedHand == False:
                    choice = ''
                    raise Exception('You have not played a hand yet.')                    
            whoplays = input('Enter u to have yourself play, '
                                 'or c to have the computer play: ')
            print('')
            if whoplays not in 'uc':
                    raise ValueError('Invalid input. Please try again!')                     
        except (ValueError, Exception) as e:
            print(e)        
        else:
            if choice == 'r' and whoplays == 'u':
                playHand(hand, wordList, HAND_SIZE)
                choice = ''
                playedHand = True
            elif choice == 'r' and whoplays == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
                choice = ''
                playedHand = True
            elif choice == 'n' and whoplays == 'u':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
                choice = ''
                playedHand = True
            elif choice == 'n' and whoplays == 'c':
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
                choice = ''
                playedHand = True
            else:
                print('Invalid command.')
            
            

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


