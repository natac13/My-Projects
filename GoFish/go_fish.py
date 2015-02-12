# Project: Go Fish game vs computer.
# By: Natac

import random
import sys
import time

suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = list(map(str, range(2, 11))) + ['A', 'J', 'Q', 'K'] 

def make_deck():
    '''Generate list of tuples, which are the card of a deck'''
    deck = [(rank, suit) for rank in values for suit in suits]
    random.shuffle(deck)
    return deck
    
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
            return []
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
        
def transfer_cards(cardvalue, hand):
    ''' 
    cardvalue is a str representation of the value of the card in question
    hand will contain at least one card matching the value
    
    return: list of card(s)(tuples) which are removed from the hand
    '''
    if cardvalue in 'ajqk':
        cardvalue = cardvalue.upper()
    return [card for card in hand if card[0] == cardvalue]
    
def update_hand(cardvalue, hand):
    '''
    cardvalue is a str representation of the value of the card in question
    hand will contain at least one card matching the value
    
    return: list of card(s)(tuples) where transffered card are removed
    '''
    if cardvalue in 'ajqk':
        cardvalue = cardvalue.upper()
    return [card for card in hand if card[0] != cardvalue]
    
    
def computer_ask(comp_hand, user_hand, deck):
    '''
    Take the comp hand and will ask user if they have one of the card value
    Random for some strategy
    
    return: tuple of a new comp hand and new user hand to unpack outside 
    function
    '''
    
    do_you_have = random.choice(comp_hand)
    print("COMPUTER TURN...")
    time.sleep(1)
    print("Do you have any {0}'s?".format(do_you_have[0]))
    user_answer = input('Y or N? ')
    print("Checking.....")
    time.sleep(2)
    if card_in_hand(do_you_have[0], user_hand):
        print("Yep, you do have some {0}'s, so I will transfer those"
                " for you.".format(do_you_have[0]))
        xfer_cards = transfer_cards(do_you_have[0], user_hand)
        user_hand = update_hand(do_you_have[0], user_hand)
        comp_hand += xfer_cards
        return(comp_hand, user_hand)
    else:
        print('Bad guess by the computer, computer draws a card.')
        time.sleep(1)
        comp_hand += draw_card(1, deck)
        return(comp_hand, user_hand)
        
def book_keeping(comp_hand, user_hand, comp_bookT, user_bookT):
    '''
    comp_hand, user_hand: are list of tuples. These represent cards.
    comp_books, user_books: are integers that are a total of how many books
    each player has
    
    returns: a tuple of 4 elements that will be unpacked,(comp_hand, user_hand,
    comp_books, user_books) then reassign outside function
    '''
    
    
    for card in comp_hand:
        if len(transfer_cards(card[0], comp_hand)) == 4:
            # by not calling transfer_cards they will simple not appear in the 
            # updated comp_hand
            print("Computer making a book of {0}'s".format(card[0]))
            comp_hand = update_hand(card[0], comp_hand)
            comp_bookT += 1
    for card in user_hand:
        if len(transfer_cards(card[0], user_hand)) == 4:
            print("You can make a book of {0}'s".format(card[0]))
            user_hand = update_hand(card[0], user_hand)
            user_bookT += 1
    print("Totals: Comp: {0}, User: {1}.".format(comp_bookT, user_bookT))
    return (comp_hand, user_hand, comp_bookT, user_bookT)
    
    
def playGame():
    '''
    Control flow of game and set up the compHand and userHand variables,
    as well as compBookTotal and userBookTotal 

    will end when there are no cards left in the deck or in either hand and all 
    books have been made. Player with more books wins
    '''
    
    print("Welcome to Natac's Go Fish game!\n To win you need to collect more " 
        "books, full sets then the computer.")
    print("When prompted, input a card value, that appears in your hand to see "
        "if you can snatch some from the computer, if not you will draw a card")
    time.sleep(3)
    
    prompt = "TO ASK>>>>>  "
    main_deck = make_deck()
    compHand, userHand = [], []
    for i in range(9):
        compHand += draw_card(1, main_deck)
        userHand += draw_card(1, main_deck)
    user_turn = True
    compBookTotal, userBookTotal = 0, 0

    
    
    while (compBookTotal+userBookTotal) != 13:
        
        while user_turn:
            if len(userHand) == 0:
                userHand += draw_card(1, main_deck)
            if len(compHand) == 0:
                compHand += draw_card(1, main_deck)
            print("\nUSER HAND: {0}\n".format(userHand))
            #print("COMP HAND", compHand) #test######################
            to_ask_comp = input(prompt)
            print("Checking...")
            time.sleep(2)
            if not card_in_hand(to_ask_comp, userHand):
                print("Nice try that card is not even in your hand")
                user_turn = False
                print("Drawing a card for user hand.")
                time.sleep(1)
                userHand += draw_card(1, main_deck)
                break
            elif card_in_hand(to_ask_comp, compHand) and card_in_hand(
                                                        to_ask_comp, userHand):
                print("Looks like the computer has some {0}'s.".format(
                                                                   to_ask_comp))
                print("Transferring cards to your hand now")
                time.sleep(1)
                userHand += transfer_cards(to_ask_comp, compHand)
                compHand = update_hand(to_ask_comp, compHand)
                break
            else:
                print("Computer didn't have any {0}'s.".format(to_ask_comp))
                print("Drawing a card for user hand.")
                time.sleep(1)
                userHand += draw_card(1, main_deck)
                print("\nUSER HAND: {0}\n".format(userHand))
                user_turn = False
            
        while not user_turn:
            if len(compHand) == 0:
                compHand += draw_card(1, main_deck)
            if len(userHand) == 0:
                userHand += draw_card(1, main_deck)
            temp_hand = userHand[:]
            #print("COMP HAND", compHand) #test######################
            print("\nUSER HAND: {0}\n".format(userHand))
            compHand, userHand = computer_ask(compHand, userHand, main_deck)
            #print("COMP HAND", compHand) #test######################
            # If the computer fails to find userHand won't change
            if len(temp_hand) == len(userHand):
                user_turn = True
                break
            else:
                print("\nUSER HAND: {0}\n".format(userHand))
                break
            
        compHand, userHand, compBookTotal, userBookTotal = book_keeping(
                            compHand, userHand, compBookTotal, userBookTotal)
                            
    print("All books have been completed, let's see who won.")
    time.sleep(1)
    if userBookTotal > compBookTotal:
        print("Congratulation you have won Natac's Go Fish game")
    else:
        print("Looks like the computer beat you this time.... wamp wamp")
                
            
                
                
                
                
if __name__ == '__main__':
    playGame()
            
    
    
    
        
    
    