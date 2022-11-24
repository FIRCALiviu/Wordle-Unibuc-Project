# Wordle-Unibuc-Project
The optimal solution for Wordle, written for a uni assignment @The University of Bucharest. Courtesy to 3b1b for explaining us the entropy "algorithm" used in project in his video https://youtu.be/v68zYyaEmEA. We got our 11 thousand words from https://cs.unibuc.ro/~crusu/asc/cuvinte_wordle.txt and they are in Romanian.
This project includes a bot for wordle which will guess the word automatically in ~ 4,37 guesses.

Dependencies for the project:
- termcolor 2.1.1
- python's 3.11 core library

Written by :
- Tirila Patric-Gabriel
- Alexandru Andrei
- Mincu Adrian-Lucian
- Firca Liviu Nicolae



The conventions used are the following:
- Red means the letter isn't in the word to guess
- Yellow means the letter is in the word to guess but not at the right spot
- Green means Yellow but it is at the right spot


- When runnig the bot, 1 means Red, 2 means Yellow, 3 means Green

! This is the buggy behaviour version of wordle, meaning that if the letter x is in the word to guess, all letter x will be colored at least yellow!

The analysis folder contains :
- line by line the word to guess and then all the guesses the bot did in solutions.txt
- the generator for the file
- average, which produced the average score of the bot