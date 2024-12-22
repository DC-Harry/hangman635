import random


word_list = ["pineapple", "kiwi", "strawberry", "cherry", "blackberry"]

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(self, guess)
        Checks if the guess is in the word.
    ask_for_input()
        Asks the user to guess a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word)*["_"]
        
        self.num_letters = len(self.word_guessed)

        self.list_of_guesses = []
    
    def check_guess(self, guess):
        '''
        Checks if the letter is in the word. 
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1. Converts guesses to lower case

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''
        guess = guess.lower()
        if guess in self.word:

            print(f"Good guess! {guess} is in the word.")

            for index in range(len(self.word)):
              if self.word[index] == guess:
                  self.word_guessed[index] = guess
                  print(self.word_guessed)
                  self.num_letters -=1 
                  print(self.num_letters)
        
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
            
    
    def ask_for_input(self):
        '''
        Asks the user to input a single charcter. If the guess is a single character, not a number or symbol or other special character and hasn't been guessed before, it calls the check_guess method and appends the guess to the list_of_guesses
        '''
        while True:
            guess = input("please enter a single letter ")

            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
                
            
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)
                break
               
game = Hangman(word_list, num_lives=5)

def play_game(word_list):
      '''
      Calls function ask_for_input if they still have lives and haven't guessed the word.  
      '''
      while True:
           if game.num_lives == 0:
               print("You lost!")
               break
           elif game.num_lives !=0 and game.num_letters > 0:
               game.ask_for_input()                            
           else:
               print("Congratulations. You won the game!")
               break
              
play_game(word_list)