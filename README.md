# Numeroll: A very simple number-building game made in Python
## Version 0.2 - 2 June 2019

Numeroll is an ongoing development project which represents my attempt to create a stand-alone (if elementary) game with Python.

## In this release
- Players are now limited to entering digits corresponding to the available slots in the number; the game will continuously prompt for new input until a valid number is entered.
- The CPU will now randomly assign digits to slots instead of assigning them in reverse sequential order. (Still in vegetable mode, but at least a little less predictable :-)

At present, Numeroll consists of a single file, numeroll.py, which was created in Python 3.6. As such, the game is in very early development and likely to break if the play instructions below are not followed.

Future releases will cover:
-edits to game output and general UX enhancement
-creating a formal project skeleton for easier updates and automated testing
-building algorithms to increase the skill level of the CPU

### How to play
The game itself involves five rounds, each with a random digit, 1 through 9, which the human player and the CPU each must use to build a five-digit number. At the end of the game, the player with the higher number is declared the winner.

The game takes its inspiration from "But Who's Counting?", a game-show segment from the popular early-90s math-teaching PBS show, _Square One_.

#### Example
The first digit you receive is 7. If you entered '1' you would assign the digit to the first slot in the five-digit number. This guarantees that the final number will have a value between 70000 and 79999.

Or, if you're feeling lucky, you can assign it to slots 2 through 5 in the hopes that an 8 or 9 will come up later, increasing the size of your number even more. But choose carefully: once you have filled a slot, it cannot be unfilled or replaced later.

NOTE: there are no zeroes randomly generated in the game. A '0' on the screen simply represents a blank slot that is available for assigning a digit. Therefore, the game is not finished until all of the zeroes (i.e. blanks) in the number are filled.

Suppose that the five generated digits are 6, 4, 1, 8, 5. After all five rounds are played, your final number might be 68,514. However, the CPU could have their final number as 85,641, in which case the CPU wins and you'll have to try again.

A simple strategy, then, is to save bigger numbers for slots '1' '2' and '3' and smaller numbers for slots '4' and '5'. (In nearly all cases, this will guarantee you a tie, if not the win, as the skill level of the CPU is currently set to "Vegetable".)

Chris Mote (@Mottetts)
