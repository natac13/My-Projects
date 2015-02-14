from go_fish import *


full_deck = make_deck()
print(full_deck)
#random.shuffle(full_deck)
print('\n\n', full_deck)
assert False
phand = draw_card(9, full_deck)
chand = draw_card(9, full_deck)

print('playerhand', phand, '\n')
print('comphand', chand)



test = input('card to move  ')

if card_in_hand(test, chand):
    move_list = transfer_cards(test, chand)
    chand = update_hand(test, chand)
    phand += move_list
    
print('\n player hand: {0}\n computer hand {1}'.format(phand, chand))