import random


word_list = ["pineapple", "kiwi", "strawberry", "cherry", "blackberry"]

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        
        self.word = random.choice(word_list)
        self.word_guessed = len(self.word)*["_"]
        
        self.num_letters = len(self.word_guessed)

        self.list_of_guesses = []
    
    def check_guess(self, guess):
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
               
game = Hangman(word_list, num_lives=2)

def play_game(word_list):
      
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