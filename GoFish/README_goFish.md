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

Making the computer_ask() function I wanted to make it a completely isolated 
event, that would have the computer randomly pick a card ask user if they have 
said card? Not that the user response matters since I verify the card is in hand
or not then run the trnsfer_card() and update_hand() functions on the user_hand.
Afterwards I reassign the user_hand and comp_hand hands then return them in a 
tuple. I found this is the best way to get to updated variables (the hands) from
one function.
** I have to remember that while making the playgame() function later I need to 
include a deck variable that updates through as well as book collection 
variables to total the score, and the reason that got me typing this reminder is
to unpack the tuple return from computer_ask() so that the "main" computer hand 
and user hand are reassign outside the function!

book_keeping() function done. And all I can say is it took a fair bit of time to 
come up with the simple test of using my transfer_cards() to make generate a 
list that I check if the length match 4 which means the player has a complete 
book. I decided to automate the whole process for both user and computer.
I will call this function after each round to update both hand and then the book
totals. *The way I got rid of the books I think is a bit clever since I just 
use my update_hand() function which returns a new list of tuples without the 
cards of the giving value present



