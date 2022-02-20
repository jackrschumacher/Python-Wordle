from difflib import diff_bytes
from random import random, randrange #Import random
import time


words = ["REALLY", "LITTLE", "SHOULD", "PLEASE", "PEOPLE", "THINGS", "BETTER"] #List of Words
randomWord = randrange(0, 5, 1)  #Range of Words 
difficulty = 0 # Difficulty level-yet to be integrated
score = 0
guessNum =1

print("---Python Wordle---") #Print Title
print("=====================================")
print("The word has six letters and you have 5 chances to correctly guess the word")

print("=====================================") # First Guess


count = 0


def guess(): 

    userInput = str(input("1:")) #Guess #1
    if userInput == randomWord: #If userInput == randomWord -> You win!, Score +60
        print("Congratulations, you have selected the Correct word!")
        score = score + 60 # Score decreases by every row


    elif len(userInput)== 6 and userInput != randomWord:
        print("Sorry, that is not the correct word. Try again")

    elif len(userInput) > 6:
        print("That word is too long. Try Again.")
        guess()

    else:
        print("That word is two short. Try Again")
        guess()


while guessNum <= 6:
    guess()
    print(guessNum)
else:
    print("You have guessed over 6 times. Better Luck Next Time")