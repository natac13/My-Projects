########        GO FISH       ########

By: Natac

Started Feb 10, 2015

First off I made a way of generating the deck from a function. To start I made 2
list, one of the suits, and the other well...start with the map() part.
In this I am making a map object from all the items from range(2, 11). I then 
turn that into a list with the built-in function. This allow me to concatenate
the numbers portion with the letters portion of the full list of ranked card 
values.

make_deck() function will return a list of tuples which represent each card.

draw_card() function will serve 2 purposes for me. One being obviously to draw a 
new card from the deck. Which I need to keep in mind has to keep modifying. The 
second purpose will be at the beginning of the game to deal out the new hands.

card_in_hand() will check to see if the value of the card the user has selected
is currently in their hand. This is really just a validation so the user is 
playing by the rules.

made transfer_cards() and update_hand() which are mirror of each other. Where 
one will get the card from a given hand and make a list out of them to transfer,
in my case I reassign the hand to the hand + what is being transferred. I had to
so that my check_in_hand() function works. I noticed during my initial testing
that is I simply append to the original hand the check_in_hand() function does
not pick up on the appended cards.

The update_hand() just returns a new hand with the cards that were transferred 
removed, or just not being creating in the new hand(list)



