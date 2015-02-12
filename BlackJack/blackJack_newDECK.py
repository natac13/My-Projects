import random

suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = list(range(2, 11)) + ['A', 'J', 'Q', 'K'] 

def make_deck():
    '''Generate list of tuples, which are the card of a deck'''
    deck = [(rank, suit) for rank in values for suit in suits] * 8
    random.shuffle(deck) # does not return anything....
    yellow_card = random.randrange(20, 71)
    # I wonder if there is a difference in time?
    #yellow_card = random.randrange(345, 395)
    #return deck[:yellow_card]
    return deck[:-yellow_card]
    
def draw_card(deck):
    ''' 
    n: an integer which is how many card to draw from the deck, usually 1
    deck: is a non-empty list of tuples when n is 9
    
    return: a list of tuples which are the cards, this coud be one card,
    will return none is the deck is empty
    '''
    new_cards = []
    
    try:
        card = deck.pop(0) # no need to del since pop() removes element as well
    except IndexError:
        print("No cards, left in deck")
        return []
    else:
        new_cards.append(card)
    
    return new_cards


def blackjackCalculator(Hand):
    
    
    ########   BLACK JACK CALCULATOR   #######
    total = 0
    ace = False
    for card in Hand:
        try:
            total += card[0]
        except TypeError:
            if card[0] in 'JQK':
                total += 10
            else:
                total += 1
                ace = True
    
    hard = total
    soft = total
    if ace:
        hard += 10
        if hard <= 21:
            # print("hard total with ace", hard)
            # print("soft total with ace", soft)
            # print("HARD IS RETURNED")
            return hard
        else:
            # print("soft total with ace", soft)
            # print("hard total with ace", hard)
            # print("SOFT IS RETURNED")
            return soft
    return total ### this is if no ace

    
main_deck = make_deck()
# print(main_deck)
print("\n", len(main_deck))

#print(main_deck)
while True:
    compHand, userHand = [], []
    for i in range(2):
        userHand += draw_card(main_deck)
        compHand += draw_card(main_deck)
    blackjackCalculator(userHand)
    
    go = True
    while go:
        print('\nplayerhand', userHand, '\n')
        print("COMP SHOWING", compHand[0])
        print(blackjackCalculator(userHand))
   ######## A way to check for blackjack, but only the first time #####
        # if blackjackCalculator(userHand) == 21:
            # print("User WIN")
            # print("COMP>>> {0}".format(blackjackCalculator(compHand)))
            # print("USER>>> {0}".format(blackjackCalculator(userHand)))
            # break
        choice = input("H, S?>>>>>")
        if choice == 'h':
            userHand += draw_card(main_deck)
            print(blackjackCalculator(userHand))
        else:
            print("COMP shows", compHand)
            
            ## if user hand bigger then 21 then just show comp hand and end turn
            if blackjackCalculator(userHand) > 21:
                print("COMP WIN")
                print("COMP>>> {0}".format(blackjackCalculator(compHand)))
                print("USER>>> {0}".format(blackjackCalculator(userHand)))
                break
            if blackjackCalculator(compHand) < 17:
                compHand += draw_card(main_deck)
                
                print("COMP shows", compHand)
                if blackjackCalculator(compHand) < 17:
                    compHand += draw_card(main_deck)
                    print("COMP shows", compHand)
                    if blackjackCalculator(compHand) < 17:
                        compHand += draw_card(main_deck)
                        print("COMP shows", compHand)
                    else:
                        if blackjackCalculator(compHand) > blackjackCalculator(userHand) and blackjackCalculator(compHand) <= 21:
                            print("COMP WIN")
                            print("COMP>>> {0}".format(blackjackCalculator(compHand)))
                            print("USER>>> {0}".format(blackjackCalculator(userHand)))
                            break
                        else:
                            print("User WIN")
                            print("COMP>>> {0}".format(blackjackCalculator(compHand)))
                            print("USER>>> {0}".format(blackjackCalculator(userHand)))
                            break    
                else:
                    if blackjackCalculator(compHand) > blackjackCalculator(userHand) and blackjackCalculator(compHand) <= 21:
                        print("COMP WIN")
                        print("COMP>>> {0}".format(blackjackCalculator(compHand)))
                        print("USER>>> {0}".format(blackjackCalculator(userHand)))
                        break
                    else:
                        print("User WIN")
                        print("COMP>>> {0}".format(blackjackCalculator(compHand)))
                        print("USER>>> {0}".format(blackjackCalculator(userHand)))
                        break
            else:
                if blackjackCalculator(compHand) > blackjackCalculator(userHand) and blackjackCalculator(compHand) <= 21:
                    print("COMP WIN")
                    print("COMP>>> {0}".format(blackjackCalculator(compHand)))
                    print("USER>>> {0}".format(blackjackCalculator(userHand)))
                    break
                else:
                    print("User WIN")
                    print("COMP>>> {0}".format(blackjackCalculator(compHand)))
                    print("USER>>> {0}".format(blackjackCalculator(userHand)))
                    break
       
        # input(">>>>>")
        # userHand += draw_card(main_deck)
        # blackjackCalculator(userHand)
       
        # input("LASTTIME   >>>>>")
        # userHand += draw_card(main_deck)
        # blackjackCalculator(userHand)
   
    