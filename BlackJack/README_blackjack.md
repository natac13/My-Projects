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
>New thought about having the dealer hit on soft 17... I cannot seem to figure
this part out at the moment, maybe I need to create a new handCal() function
for the dealer to account for this. *Going to think on this one since game is in
a working condition to see if I cannot just use the functions I have currently*

#### Abstraction
>I have turned the played turn from mine test scripts into a function. This may 
**not** be the best solution since I do not think I can deal with the user 
wanting to split. THe function player_turn returns the player_hand so I may 
compare it to the dealers later. But I am **LOST** on how to deal with a possible
of multi-hands for the user to control.

>The display outputs have also been put into functions since I think when I do 
implement the playgame() it will be easier to read and therefore work through.


#### playGame()
I have got my first version of playGame() implemented. No success on being able
to split. I thought of just added it to the original hand then evaluate only 
parts against the dealer hand but again I do not think this will work.

*Next step is to add in the betting aspect of the game*


