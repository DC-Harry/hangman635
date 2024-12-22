import random


word_list = ["pineapple", "kiwi", "strawberry", "cherry", "blackberry"]

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("please enter a single letter ")

if len(guess) == 1:
    print(" Good guess!")
else:
    print("Oops! That's not a valid input")