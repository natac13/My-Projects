# testing for Go Fish game
##
from go_fish import *

full_deck = make_deck()

phand = draw_card(9, full_deck)
chand = draw_card(9, full_deck)
print('playerhand', phand)
print('comphand', chand)
print(' ')
print('deck', full_deck)


print('')
phand += (draw_card(1, full_deck))
chand +=(draw_card(1, full_deck))
phand += (draw_card(1, full_deck))
chand += (draw_card(1, full_deck))

print('playerhand', phand)
print('comphand', chand)
print("")
print('deck' , full_deck)

x = input('rank to check for p1  ')
print(card_in_hand(x, phand))

x = input('rank to check for p2   ')
print(card_in_hand(x, phand))

for _ in range(30):
    chand += (draw_card(1, full_deck))
print(chand, '\n', full_deck)
print('\n')
chand.pop
y = input('rank to check for c1  ')
print(card_in_hand(y, chand))