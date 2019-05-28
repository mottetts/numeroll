# Numeroll: A very simple number-building game made in Python
## Version 0.1

## Release notes
This is the very first edition of Numeroll and consists of a single file, numeroll.py, which was created in Python 3.6. As such, the game is extremely _not_ test-proof and likely to break easily unless the play instructions below are followed.

Future releases will cover adding exceptions to limit user input, building algorithms to increase the skill level of the CPU, and creating a more formal skeleton to allow for easier updates and automated testing.

### How to play
Numeroll is one of my first attempts at designing a game with Python. The game itself involves five random digits, 0 through 9, which the human player and the CPU each must assign to a five-digit number. After five rounds, the player with the higher number is declared the winner.

The game takes its inspiration from "But Who's Counting?", a game-show segment from the popular early-90s math-teaching PBS show, _Square One_.

#### Example
The first digit you receive is 7. If you entered '1' you would assign the digit to the first slot in the five-digit number. This guarantees that the final number will have a value between 70000 and 79999.

Or, if you're feeling lucky, you can assign it to slots '2' through '5' in the hopes that an 8 or 9 will come up later, increasing the size of your number even more. But choose carefully: once you have filled a slot, it cannot be unfilled or replaced later.

A simple strategy, then, is to save bigger numbers for slots '1' '2' and '3' and smaller numbers for slots '4' and '5'. (In nearly all cases, this will guarantee you a tie, if not the win, as the skill level of the CPU is currently set to "Vegetable".)
