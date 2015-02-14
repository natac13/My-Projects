from go_fish import *



main_deck = make_deck()
print(main_deck)

#print(main_deck)
compHand, userHand = [], []
for i in range(9):
    compHand += draw_card(1, main_deck)
    userHand += draw_card(1, main_deck)

print('playerhand', userHand, '\n')
print('comphand', compHand)



test = input('card to move  ')
total = 0
for card in userHand:
    try:
        
print('\n player hand: {0}\n computer hand {1}'.format(phand, chand))