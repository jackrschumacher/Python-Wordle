from difflib import diff_bytes
from random import random, randrange #Import random
import time


words = ["REALLY", "LITTLE", "SHOULD", "PLEASE", "PEOPLE", "THINGS", "BETTER"] #List of Words
randomWord = randrange(0, 5, 1)  #Range of Words 
difficulty = 0 # Difficulty level-yet to be integrated
score = 0


print("---Python Wordle---") #Print Title
print("=====================================")
print("The word has six letters and you have 5 chances to correctly guess the word")

print("=====================================") # First Guess


count = 0

guessNum = 0

def guess(): 
    global guessNum
    
  
    
    
    if guessNum <= 6:
        guessNum = guessNum +1
        #Add if-else for custom user inputs -> 1,2, etc.
        if guessNum ==6:
            userInput = str(input("6:")) #Guess #1
        elif guessNum ==5:
            userInput = str(input("5:"))
        elif guessNum == 4:
            userInput = str(input("4"))
        elif guessNum == 3:
            userInput = str(input("3: "))
        elif guessNum == 2:
            userInput = str(input("2: "))
        elif guessNum == 1:
            userInput = str(input("1:"))
    
        

        
        if userInput == randomWord:  #If userInput == randomWord -> You win!, Score +60
                print("Congratulations, you have selected the Correct word!")
                score = score + 60 # Score decreases by every row


        elif len(userInput)== 6 and userInput != randomWord:
                print("Sorry, that is not the correct word. ")
                guess()

        elif len(userInput) > 6 or len(userInput) < 6:
                print("Wrong word size. Try Again")
                userInput = str(input("Again:"))
                if len(userInput) == 6 and userInput == randomWord:
                    print("You Guessed the word!")
                    score = score +60
                else:
                    print("You did not pick the correct word")
                    guess()
                

        
        
    else:
        print("You have guessed over 6 times. Better Luck Next Time.")

guess()