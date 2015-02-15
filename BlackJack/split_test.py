import random
from blackJack_game import *
import time


def split(player_hand, deck):
    '''
    take player_hand and splits into 2 different hands, draw_card() for each
    returns: 2 player hands each a list of 2 tuples    
    '''
    right, left = [(player_hand[0]),], []
    right += player_hand[0]
    right += draw_card(deck)
    left += player_hand[1] 
    left += draw_card(deck)
    return (left, right)
        
        
def playerTurn(players, deck, dealer_hand):
    '''
    players: list of list of tuples, represent the cards from the deck
    deck: is the main deck which is always getting modified
    
    returns: the player hand when they stand or the hand is greater than 21
    '''
    
    while not bust(players[0]):
        print('Your hand = {0} : {1}'.format(handCal(players[0]), players[0]))
        print('Dealer showing... {0}'.format(dealer_hand[0]))
        choice = input("Hit(h), Double(d), Stand(s)??  ")
        if choice == 'h':
            hit_card = draw_card(deck)
            print("DRAW : {0} >> {1}".format(hit_card, players[0]))
            players[0] += hit_card
            print("TOTAL : {0}".format(handCal(players[0])))
            time.sleep(1)
        elif choice == 'd':
            hit_card = draw_card(deck)
            print("DRAW : {0} >> {1}".format(hit_card, players[0]))
            players[0] += hit_card
            print("TOTAL : {0}".format(handCal(players[0])))
            time.sleep(1)
            return players[0] # not able to draw anymore
        elif choice == 's':
            try:
                if players[0][0] != players[0][1]:
                    raise ValueError
            except ValueError:
                print("You can't split that hand")
            else:
                newc = draw_card(deck)
                newv = draw_card(deck)
                players[1] = [[players[0][1]], newc] 
                players[0] = [[players[0][0]], newv]
                print(players[1])
                playerTurn((players[1]+newc), deck, dealer_hand)
                print(players[0])
                
                
                
                ##run split function##
                # run to version of playerTurn one with the first card form 
                # old hand other with second card
                # remember to draw_card
        else:
            return players[0] # when stand
    return players[0]   # when hand over 21 meaning bust() returns True
    
deck = make_shoe()
    
while len(deck) > 0:
    dealer_hand, user_hand = deal_cards(deck)
    user_hand = [(8, 'of test'), (8, 'of test')]
    phs = [user_hand, [(),()]]
    print(phs)
    
    
    input("\nDeal hand?? ")
    player_control = True
    
    while player_control:
        # print('Your hand = {0} : {1}'.format(handCal(phs[0]), phs[0]))
        # print('Dealer showing... {0}'.format(dealer_hand[0]))
        if have_BJ(phs[0]) and str(dealer_hand[0][0]) == "A":
            ins = input("INSURANCE??? y or n : ") # for betting later
            player_control = False 
            break # goes to dealer turn at this point
        elif have_BJ(phs[0]) and str(dealer_hand[0][0]) in "10JQK": 
            print("\nCHECKING FOR BLACKJACK....")
            time.sleep(2)
            if handCal(dealer_hand) == 21:
                push(dealer_hand, phs[0])
                time.sleep(1)
                break # To start new round
            else:
                if handCal(dealer_hand) < handCal(phs[0]):
                    player_win(dealer_hand, phs[0])
                    time.sleep(1)
                    break # To start new round
        elif have_BJ(phs[0]):
            player_win(dealer_hand, phs[0])
            time.sleep(2)
            break # To start new round
        # where user takes control of game
        # returns the phs[0] without having to reassign 
## this is where i do a for each ele in dict run player turn        
        playerTurn(phs, deck, dealer_hand)
        if bust(phs[0]):
            dealer_win(dealer_hand, phs[0])
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
            player_win(dealer_hand, phs[0])
            break
        else:
            if handCal(dealer_hand) > handCal(phs[0]):
                dealer_win(dealer_hand, phs[0])
                break
            elif handCal(dealer_hand) == handCal(phs[0]):
                push(dealer_hand, phs[0])
                break
            else:
                player_win(dealer_hand, phs[0])
                break           
        player_control = True



