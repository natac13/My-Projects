# BlackJack Game
# By: Natac
# Rules of choice are in rules_blackjack.txt
# Feb 13, 2015

import random
import time

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
        card = deck.pop(0)
    except IndexError:
        print("No cards, left in deck")
        return new_cards # empty list 
    else:
        new_cards.append(card)
    return new_cards


def handCal(Hand):
    '''
    Hand is a list of tuples, which have mostly (int, str) groupings, however, 
    for (str, str) the try block handles this case.
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
    
def have_BJ(hand):
    '''
    hand: list of tuples, first element of tuple is value of card
    
    returns: True if user_hand hand equal 21 with only 2 cards
    '''
    return (handCal(hand) == 21 and len(hand) == 2)

def bust(hand):
    '''returns: True if given hand is over 21'''
    return (handCal(hand) > 21)
    
def dealer_win(dealer_hand, player_hand):
    '''Display info when dealer wins'''
    print("\nSorry you lose...")
    print("Dealer Hand >> {0} : {1}".format(handCal(dealer_hand), dealer_hand))
    print("Player Hand >> {0} : {1}".format(handCal(player_hand), player_hand))
                                                   
def player_win(dealer_hand, player_hand):
    '''Display info when player wins'''
    print("\nYOU WIN!!!")
    print("Dealer Hand >> {0} : {1}".format(handCal(dealer_hand), dealer_hand))
    print("Player Hand >> {0} : {1}".format(handCal(player_hand), player_hand))
    
def push(dealer_hand, player_hand):
    '''Display info for push event'''
    print("\nHAND IS A PUSH...")
    print("Dealer Hand >> {0} : {1}".format(handCal(dealer_hand), dealer_hand))
    print("Player Hand >> {0} : {1}".format(handCal(player_hand), player_hand))
    
def deal_cards(shoe):
    '''
    shoe: big list of tuples, representing the shoe being played
    
    returns: 2 list of tuples, which represent cards... in a tuple
    first element: dealer_hand
    second element: player_hand
    '''
    dealer_hand, player_hand = [], []
    for i in range(2):
        dealer_hand += draw_card(shoe)
        player_hand += draw_card(shoe)
    return (dealer_hand, player_hand)
    
def split(player_hand, deck):
    '''
    take player_hand and splits into 2 different hands, draw_card() for each
    returns: 2 player hands each a list of 2 tuples    
    '''
    right = player_hand[0]
    right += draw_card(deck)
    left = player_hand[1] 
    left += draw_card(deck)
    return left + right
        
        
def playerTurn(player_hand, deck, dealer_hand, bet):
    '''
    player_hand: list of tuples, represent the cards from the deck
    deck: is the main deck which is always getting modified
    dealer_hand passed in to reveal one card to the player
    
    returns: the player hand when they stand or the hand is greater than 21, and
    the players bet in a tuple to unpack outside function
    '''
    
    while not bust(player_hand):
        if player_hand == 21:
            return (player_hand, bet)
        print('\nYour hand = {0} : {1}'.format(handCal(player_hand), player_hand))
        print('Dealer showing... {0}'.format(dealer_hand[0]))
        choice = input("\nHit(h), Double(d), Stand(s)??  ")
        if choice == 'h':
            hit_card = draw_card(deck)
            print("\nDRAW : {0} >> {1}".format(hit_card, player_hand))
            player_hand += hit_card
            print("TOTAL : {0}".format(handCal(player_hand)))
            time.sleep(1)
        elif choice == 'd':
            bet += bet
            hit_card = draw_card(deck)
            print("\nDRAW : {0} >> {1}".format(hit_card, player_hand))
            player_hand += hit_card
            print("TOTAL : {0}".format(handCal(player_hand)))
            time.sleep(1)
            return (player_hand, bet)# not able to draw anymore
        # elif choice == 'split':
            # try:
                # if player_hand[0] != player_hand[1]:
                    # raise ValueError
            # except ValueError:
                # print("You can't split that hand")
            # else:
                # split_player_hand = split(player_hand, deck)
                
                # ##run split function##
                # # run to version of playerTurn one with the first card form 
                # # old hand other with second card
                # # remember to draw_card
        else:
            return (player_hand, bet) # when stand
    return (player_hand, bet)   # when hand over 21 meaning bust() returns True
    
def playGame():
    deck = make_shoe()
    money = float(input("CASH???   "))
    print("Start with ${0:.2f}".format(money))
    time.sleep(2)
    
    while len(deck) > 0 and money > 0:
    
        dealer_hand, user_hand = deal_cards(deck)
        bet = 0.0
        print('\nYou currently have ${0:.2f}'.format(money))
        while bet < 15.0 or bet > 500.0:
            bet = float(input("\nBet Amount... min $15 - max $500>> "))
            if bet > money:
                bet = 0.0
                print("You do not have enough money")
        
        player_control = True
        
        while player_control:
              
            if have_BJ(user_hand) and str(dealer_hand[0][0]) == "A":
                print('Your hand = {0} : {1}'.format(handCal(user_hand), user_hand))
                print('Dealer showing... {0}'.format(dealer_hand[0]))
                even_money = input("Even money??? y or n : ") 
                if even_money == 'y':
                    money += bet # take even money and end round
                    break
                else:
                    player_control = False 
                    break # goes to dealer turn at this point
            elif have_BJ(user_hand) and str(dealer_hand[0][0]) in "10JQK": 
                print('\nYour hand = {0} : {1}'.format(handCal(user_hand), user_hand))
                print('Dealer showing... {0}'.format(dealer_hand[0]))
                print("\nCHECKING FOR BLACKJACK....")
                time.sleep(2)
                if handCal(dealer_hand) == 21:
                    # money += bet # get back bet 
                    push(dealer_hand, user_hand)
                    time.sleep(1)
                    break # To start new round
                else:
                    if handCal(dealer_hand) < handCal(user_hand):
                        money += (bet*1.5) # blackJack pays 3:2
                        print("\nBLACKJACK")
                        player_win(dealer_hand, user_hand)
                        time.sleep(1)
                        break # To start new round
            elif have_BJ(user_hand):
                money += (bet*1.5) 
                print("\nBLACKJACK")
                player_win(dealer_hand, user_hand)
                time.sleep(2)
                break # To start new round
            # where user takes control of game
            # returns the user_hand and bet for reassignment
            user_hand, bet = playerTurn(user_hand, deck, dealer_hand, bet)
            if bust(user_hand):
                dealer_win(dealer_hand, user_hand)
                money -= bet
                break # To start new round
            player_control = False
        
        while not player_control:
            print("\nDEALER FLIPS>>>", dealer_hand)
            time.sleep(1)
            while handCal(dealer_hand) < 17:
                dealer_hand += draw_card(deck)
                print("\nDEALER DRAWS....\n{1} : {0}".format(
                                            handCal(dealer_hand), dealer_hand))
                time.sleep(1)
            if bust(dealer_hand):
                player_win(dealer_hand, user_hand)
                money += bet
                break
            else:
                if handCal(dealer_hand) > handCal(user_hand):
                    dealer_win(dealer_hand, user_hand)
                    money -= bet
                    break
                elif handCal(dealer_hand) == handCal(user_hand):
                    push(dealer_hand, user_hand)
                    # money += bet
                    break
                else:
                    player_win(dealer_hand, user_hand)
                    money += bet
                    break           
            player_control = True
    print("\nThank you for playing you finish with a total of ${0:.2f}" \
                                                                .format(money))        
if __name__ == '__main__':
    print("Welcome to Natac's BlackJack game")
    playGame()

