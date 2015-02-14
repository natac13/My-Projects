## Project BlackJack
### Natac
*This game is a vice of mine.*

#### Blackjack Calculator
I have got the blackjack calculator done. This will calculate the hand values.
I add up all the first elements of the cards(which are tuples) and if one is a 
letter instead of an integer, then a TypeError is raise which I then add 10 to 
the total for each 'J', 'Q', 'K' and  add only 1 for the aces since in a real
game of blackjack you only ever treat one ace in a multi-ace hand as 11. 
So then I check if by adding 10 when there is an ace (trigger in the code) if 
that value is less than or equal to 21 if so return that. If not then the ace 
cards get treated as 1's then return whatever value that is even if over 21...

#### make_shoe()
Also I have changed the make_shoe() to account for 8 deck in the shoe. And I 
just had the thought about how to deal with the yellow splitter card that cuts
out a portion of the total shoe. Well I think I will use randrange() to pick a 
value of about 83-95% of the total amount of cards. Therefore total card is 416
with 8 decks so randrange(345, 396).

I did change it to a randrange(20, 71) which is 5-17% of 416 and then get the 
deck from beginning to the end minus the yellow_card. I wonder if this makes it 
any faster. Not that I think it matters since it will only happen once, at the 
start of the game.

*So far the game is working I need to find a way to turn the 3 nested if 
statements about the comphand being smaller then 17, into a while loop somehow.
Taking a break though right now.* **COMPLETED**
I feel pretty humbled when I came to the realization of what I had to change my 
3 nested if statements to a while loop! lol 40+ lines down to about 5!

Have made a bunch of functions out of events that were repeating in the test code.
I did this since the test code is very close to the way I will implement the 
playgame() function. 

####Issue
>trying to determine how to deal with when the user wants to split the hand. I 
am lost on how to make it work with my current structure. 
>First thought was to use a playerturn function and if the user splits the to 
call the playgame() recursively with splitting my list of tuples (The hand),
but then I am not sure how to evaluate the 2+ hands after the dealer turn.


