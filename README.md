# Word-Hunter-Killer
 Wins at Word Hunt.

## Overview
Word Hunt is an iMessage text game. You are presented with a 4x4 grid of scrabble-esque letter tiles,
and have 80 seconds to select words by connecting adjacent tiles.

### Rules
- 80 seconds per round
- 4x4 grid of letter
- Adjacent letters are horizontal, vertical and diagonally next to each other
- No letter can be used more than once in the same word
- Point value per word is determined by word length, longer words are worth significantly more

I lost every single game, often due to my friends spamming short sequences that looked like words,
even if they did not actually know it was a word, and hoping to get lucky. Examples: HIED, BEDE,
DELS, LOTE.

Word Hunter Killer ingests the grid (currently entered via command line but I have plans for faster intake)
and then finds all possible words then serves them back via GUI so you can
enter them into your device.

## Building
You should be able to download and run - I believe(?) all libraries are included in standard Python 3 installs.

## Using
Run main.py and enter your grid, left-to-right/top-to-bottom into the prompt. No need for delimiters (though the 
system should be able to remove most). Words are served to you via a colour-based GUI system that I believe allows 
for faster recognition of swipe paths and entering into your device. 

Start at on the red square and follow the colour spectrum towards the final blue. It can take a bit of practice
but I believe it to be faster than using numbers. Colourblind people - good luck (colourblind mode coming soon).

Scroll through the answers using the left and right arrow keys.

Words are also displayed at the top of the window. Unfortunately, due to the fact that the Word Hunt wordlist
is not public, Word-Hunter-Seeker will occaisonally serve you an invalid word - just move on.
