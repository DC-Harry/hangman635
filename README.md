# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Contents
### Description

The Hangman project is a game in which the user inputs their guess and it is checked against a "randomly" selected word. The user get 5 valid guesses, and if they're able to succeed they win.

### Aims

The aim of the project was to build a functioning game using python, it's built in modules, functions, and data structures as well as utlilising concepts such as: object oriented programming.

### Outcomes
I learned how to pay more attention to the order variables and functions are declared in. I had a few issues with calling a function that took a variable as an arguement that hadn't yet been declared. In addition to that I had to be careful about the order of if-elif-else conditions, as if a condition is true e.g `len(guess) == 1 and guess.isalpha()` the subsequent elif conditions would not be checked. In this case that meant the game would continue despite num_lives being less than 0


### Instructions

  1. intialise local repostitory
  2. clone test-repo
  3. authenticate access
  4. execute milestone_5.py
  
   The user will be prompted for an input. If the user enters an invalid character (a number, a symbol or multiple characters), they will be prompted to try again with a single character.
   If a valid character is entered and the character is in the randomly selected word, the game will print a message informing the user that their guess was sucessful, and print a list with the guessed letter at it's position in the word and unguessed letters will be displayed as "_" The user will then be prompted to enter another letter. If the character is not in the randomly selected word, the user will be informed they guessed unsucessfully, of their remaining number of lives and prompted to guess again. before each guess the user will be displayed their previous guess attempts and if they guess a character they have already selected, they will be informed an  prompted to guess again.

   When all letters are guessed the user will be told that they've guessed correctly and the full word will be displayed
### File Structure
The game runs from a single .py file

### License information
The license for this project is GNU GENERAL PUBLIC LICENSE, allowing users to download, run, copy and modifiy the code, but requiring that it not be used for proprietery software.
