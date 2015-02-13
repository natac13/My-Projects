# BlackJack Game
# By: Natac
# Rules of choice are in README_blackjack.md
# Feb 13, 2015

import random

suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = list(range(2, 11)) + ['A', 'J', 'Q', 'K'] 

def make_shoe():
    '''
    Generate list of tuples, which are the cards of a deck, 8 times
    shuffle the full shoe    
    
    returns: full shoe with yellow_card inserted around 83-95% of total size
    '''
    shoe = [(rank, suit) for rank in values for suit in suits] * 8
    random.shuffle(shoe) # does not return anything....
    yellow_card = random.randrange(20, 71)
    return shoe[:-yellow_card]
    
def draw_card(deck):
    ''' 
    deck: is a list of tuples 
    
    return: a list of one tuple, then add onto players hand outside function
    '''
    new_cards = []
    try:
        card = deck.pop(0) # no need to del since pop() removes element as well
    except IndexError:
        print("No cards, left in deck")
        return new_cards # empty list 
    else:
        new_cards.append(card)
    
    return new_cards


def handCal(Hand):
    '''
    Hand is a list of tuples, which have mostly (int, str) groupings, however, 
    for (str, str) the try block handles this caes.
    aces start as a value of 1, (only ever use 1 ace as 11 in a hand)
    
    return: an integer that is the total value of the hand.    
    '''
    total = 0
    ace = False
    for card in Hand:
        try:
            total += card[0]
        except TypeError:
            if card[0] in 'JQK':
                total += 10
            else: # the card is an ace
                total += 1
                ace = True
    if ace:
        total += 10
        if total <= 21:
            return total
        else:
            return total - 10
    return total ### this is if no ace
    
