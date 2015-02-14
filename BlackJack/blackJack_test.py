import random
from blackJack_game import *
import time

    
main_deck = make_shoe()

while len(main_deck) > 0:
    print("\n", len(main_deck), '\n') ## just to see how big the shoe is
    input("PLAY????")
    compHand, userHand = deal_cards(main_deck)
    # userHand = [('A', 'of test'), ('K', 'of test')]
    # compHand = [('Q', 'of test'), ('A', 'of test')]
    handCal(userHand)
    
    player_control = True
    while player_control:
        print('\nplayerhand', userHand, '\n{0}\n'.format(handCal(userHand)))
        print("COMP SHOWING", compHand[0])
######## A way to check for blackjack, but only the first time #####
        if have_BJ(userHand) and str(compHand[0][0]) == "A":
            ins = input("INSURANCE??? y or n : ") # for betting later
            player_control = False 
            break # goes to dealer turn at this point
        elif have_BJ(userHand) and str(compHand[0][0]) in "10JQK": 
            print("CHECKING FOR BLACKJACK....")
            time.sleep(2)
            if handCal(compHand) == 21:
                push(compHand, userHand)
                time.sleep(1)
                break # To start a whole new hand no need for dealer to proceed
            else:
                if handCal(compHand) < handCal(userHand):
                    player_win(compHand, userHand)
                    time.sleep(1)
                    break # To start a whole new hand no need for dealer to proceed
        elif have_BJ(userHand):
            player_win(compHand, userHand)
            time.sleep(2)
            break # To start a whole new hand no need for dealer to proceed
            
            
        playerTurn(userHand, main_deck)# this didnt require reassignment
        
        if bust(userHand):
            dealer_win(compHand, userHand)
            break # To start a whole new hand no need for dealer to proceed
        else:
            player_control = False
        
    while not player_control:
        print("DEALER FLIPS>>>", compHand)
        time.sleep(1)
        while handCal(compHand) < 17:
            compHand += draw_card(main_deck)
            print("DEALER DRAWS....\n{1} : {0}".format(handCal(compHand), 
                                                    compHand))
            time.sleep(1)
        if bust(compHand):
            player_win(compHand, userHand)
            break
        else:
            if handCal(compHand) > handCal(userHand):
                dealer_win(compHand, userHand)
                break
            elif handCal(compHand) == handCal(userHand):
                push(compHand, userHand)
                break
            else:
                player_win(compHand, userHand)
                break           
        player_control = True

                    
    

   
    