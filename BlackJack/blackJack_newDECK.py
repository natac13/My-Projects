import random

suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = list(range(2, 11)) + ['A', 'J', 'Q', 'K'] 

def make_deck():
    '''Generate list of tuples, which are the card of a deck'''
    deck = [(rank, suit) for rank in values for suit in suits] * 4
    random.shuffle(deck) # does not return anything....
    return deck
    
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


def blackjackCalculator(userHand):
    print('\nplayerhand', userHand, '\n')
    
    ########   BLACK JACK CALCULATOR   #######
    total = 0
    ace = False
    for card in userHand:
        try:
            total += card[0]
        except TypeError:
            if card[0] in 'JQK':
                total += 10
            else:
                total += 1
                ace = True
    print("Hand total", total)
    hard = total
    soft = total
    if ace:
        hard += 10
        if hard <= 21:
            print("hard total with ace", hard)
            print("soft total with ace", soft)
            print("HARD IS RETURNED")
        else:
            print("soft total with ace", soft)
            print("hard total with ace", hard)
            print("SOFT IS RETURNED")

    
main_deck = make_deck()
print(main_deck)
print("\n", len(main_deck))

#print(main_deck)
while True:
    compHand, userHand = [], []
    for i in range(2):
        userHand += draw_card(main_deck)
        

    blackjackCalculator(userHand)
   
    input(">>>>>")
    userHand += draw_card(main_deck)
    blackjackCalculator(userHand)
   
    input(">>>>>")
    userHand += draw_card(main_deck)
    blackjackCalculator(userHand)
   
    input("LASTTIME   >>>>>")
    userHand += draw_card(main_deck)
    blackjackCalculator(userHand)
   
    