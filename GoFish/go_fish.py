# Project: Go Fish game vs computer.
# By: Natac

import random
import sys

suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = list(map(str, range(2, 11))) + ['A', 'J', 'Q', 'K'] 

def make_deck():
    '''Generate list of tuples, which are the card of a deck'''
    return [(rank, suit) for rank in values for suit in suits]
    
def draw_card(n, deck):
    ''' 
    n: an integer which is how many card to draw from the deck, usually 1
    deck: is a non-empty list of tuples when n is 9
    
    return: a list of tuples which are the cards, this coud be one card,
    will return none is the deck is empty
    '''
    new_cards = []
    if n == 1:
        try:
            card = random.choice(deck)
        except IndexError:
            print("No cards, left in deck")
            return None
        else:
            deck.remove(card)
            new_cards.append(card)
    if n == 9:
        for i in range(n):
            card = random.choice(deck)
            new_cards.append(card)
            deck.remove(card)
    return new_cards
    
def card_in_hand(v, hand):
    '''
    v is a rank value of a card from the deck, ie 3, or 'A'
    Hand is a list of tuples
    
    returns: true if that card is currently in the given hand
    '''
    if v in 'ajqk':
        v = v.upper()
    for card in hand:
        if card[0] == v:
            return True
    return False
        
    
    
    