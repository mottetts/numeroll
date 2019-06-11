# Numeroll: A very simple number-building game made in Python
## Version 0.3

Numeroll is an ongoing development project which represents my attempt to create a stand-alone game with Python.

## Release notes

### 0.3 - 11 June 2019
- Zero has been enabled as one of the random digits that can be assigned to a number (originally just 1-9 were playable).
- Underscore '_ now signifies an empty slot instead of 0.
### 0.2 - 2 June 2019
- Players are now limited to entering digits corresponding to the available slots in the number; the game will continuously prompt for new input until a valid number is entered.
- The CPU will randomly assign digits to slots instead of assigning them in reverse sequential order. (Still in vegetable mode, but at least a little less predictable :-)

Future releases will cover:
- edits to game output and general UX enhancement
- creating a formal project skeleton for easier updates and automated testing
- building algorithms to increase the skill level of the CPU

## How to play
Numeroll consists of five rounds, each with a random digit (0 through 9) that the human player and computer player each must use to build the biggest five-digit number possible. At the end of the game, the player with the higher number is declared the winner.

The game takes its inspiration from "But Who's Counting?", a game-show segment from the popular early-90s math-teaching PBS show, _Square One_.

#### Example
The first digit you receive is 7. If you enter '1', you  assign the digit to the first slot in the five-digit number. This guarantees that the final number will have a value between 70000 and 79999.

If you're feeling lucky, you can assign it to slots 2 through 5 in the hopes that an 8 or 9 will come up later, increasing the size of your number even more. But choose carefully: once you have filled a slot, it cannot be unfilled or replaced later.

Suppose that the five generated digits are 6, 4, 8, 5, 0. After all five rounds are played, your final number might be 68,504. However, the CPU could have 85,640 as is final number, in which case the computer wins and you'll have to try again.

A simple strategy is to save numbers greater than 5 for slots '1' '2' and '3' and smaller numbers for slots '4' and '5'. You can gamble and leave the first slot open to try to get the highest possible number, but if the last round of the game generates a '0', your number will shrink by a whole digit! In the example above, that means 6,854 could have been the outcome, which would be a loss in nearly all scenarios...so assign wisely!

Chris Mote (@Mottetts)
