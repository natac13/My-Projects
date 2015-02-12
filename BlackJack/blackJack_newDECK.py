

suits = ['Spade', 'Heart', 'Club', 'Diamond']
values = list(range(2, 11)) + ['A', 'J', 'Q', 'K'] 

def make_deck():
    '''Generate list of tuples, which are the card of a deck'''
    deck = [(rank, suit) for rank in values for suit in suits]
    random.shuffle(deck) # does not return anything....
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

    return new_cards
    
main_deck = make_deck()
print(main_deck)

#print(main_deck)
compHand, userHand = [], []
for i in range(2):
    compHand += draw_card(1, main_deck)
    userHand += draw_card(1, main_deck)

print('playerhand', userHand, '\n')
print('comphand', compHand)
########   BLACK JACK CALCULATOR   #######
total = 0
for card in userHand:
    try:
        total += card[0]
    except TypeError:
        if card[0] in 'JQK':
            total += 10
        else:
            total += 11
print('\nplayerhand', userHand, '\n')
print(total)