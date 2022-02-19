from difflib import diff_bytes
from random import random, randrange #Import random


words = ["REALLY", "LITTLE", "SHOULD", "PLEASE", "PEOPLE", "THINGS", "BETTER"] #List of Words
randomWord = randrange(0, 5, 1)  #Range of Words 
difficulty = 0 # Difficulty level-yet to be integrated

print("---Python Wordle---") #Print Title
print("=====================================")
print("The word has six letters and you have 5 chances to correctly guess the word")

print("=====================================") # First Guess
print("GUESS #1:")

count = 0

userInput = str(input("1: "))

if userInput == randomWord:
    print("Congratulations, you have selected the Correct word!")

for i in userInput:
    if userInput.# length
        print(i)
    