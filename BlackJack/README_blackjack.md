# Project BlackJack
# Natac
# This game is a vice of mine.

I have got the blackjack calculator done. This will calculate the hand values.
I add up all the first elements of the cards(which are tuples) and if one is a 
letter instead of an integer, then a TypeError is raise which I then add 10 to 
the total for each 'J', 'Q', 'K' and *** add only 1 for the aces since in a real
game of blackjack you only ever treat one ace in a multi-ace hand as 11. 
So then I check if by adding 10 when there is an ace (trigger in the code) if 
that value is less than or equal to 21 if so return that. If not then the ace 
cards get treated as 1's then return whatever value that is even if over 21...


Also I have changed the make_deck() to account for 8 deck in the shoe. And I 
just had the thought about how to deal with the yellow splitter card that cuts
out a portion of the total shoe. Well I think I will use randrange() to pick a 
value of about 83-95% of the total amount of cards. Therefore total card is 416
with 8 decks so randrange(345, 396).

I did change it to a randrange(20, 71) which is 5-17% of 416 and then get the 
deck from beginning to the end minus the yellow_card. I wonder if this makes it 
any faster. Not that I think it matters since it will only happen once, at the 
start of the game.


So far the game is working I need to find a way to turn the 3 nested if 
statements about the comphand being smaller then 17, into a while loop somehow.
Taking a break though right now.

Have made a bunch of functions out of events that were repeating in the test code.
I did this since the test code is very close to the way I will implement the 
playgame() function. 
