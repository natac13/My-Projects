from go_fish import *


full_deck = make_deck()

phand = draw_card(9, full_deck)
chand = draw_card(9, full_deck)
comptotal , usertotal = 0, 0
print('playerhand', phand, '\n')
print('comphand', chand)

#chand, phand = computer_ask(chand, phand, full_deck)
#print('playerhand', phand, '\n')
#print('comphand', chand)

phand += draw_card(9, full_deck)
phand += draw_card(9, full_deck)


print('\nplayerhand', phand, '\n')

chand, phand, comptotal, usertotal = book_keeping(chand, phand,
                                                    comptotal, usertotal)
print('\nplayerhand', phand, '\n')

phand += draw_card(9, full_deck)
print('\nplayerhand', phand, '\n')
chand, phand, comptotal, usertotal = book_keeping(chand, phand, 
                                                    comptotal, usertotal)
print('\nplayerhand', phand, '\n')


