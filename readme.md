# blackjack-5card-simulation

Red Dead Redemption 2's Gambler Challenge 8 requires the player to play blackjack and win 3 games in which you 'hit' (ask for another card to be dealt) 3 times or more. 

This program simulates 100000 games of blackjack to work out the probability of winning one such game under these conditions. 

# Usage
Open a command line window, navigate to the directory where `sim.py` is located and then
```
python sim.py
```

# Notes
* The success condition is where you have been dealt 5 cards, and the value of those cards sum to between `minimum_acceptable_sum` inclusive and 21 inclusive. `minimum_acceptable_sum` is set to 18 by default. Feel free to open `sim.py` with a text editor and tweak this variable (located on line 6) to whatever you want.

## Result
My simulation result concluded that there is a probability of around 3.62% of winning one such game, with `minimum_acceptable_sum` set to 18.
