from difflib import diff_bytes
from random import random, randrange #Import random
import time


words = ["Really", "Little", "Should", "Please", "People", "Things", "Better"] #List of Words
random = randrange(0, 5, 1)  #Range of Words 
randomWord = words[random]
difficulty = 0 # Difficulty level-yet to be integrated

print(randomWord)

print("---Python Wordle---") #Print Title
print("=====================================")
print("The word has six letters and you have 5 chances to correctly guess the word")

print("=====================================") # First Guess


count = 0

guessNum = 0

def guess(): 
    global guessNum
    global score
    
    
  
    
    
    if guessNum <= 5:
        guessNum = guessNum +1
        if guessNum ==6:
            userInput = str(input("6:")) #Guess #2
        if guessNum ==5:
            userInput = str(input("5:")) #Guess #2
        elif guessNum == 4:
            userInput = str(input("4:")) #Guess #3
        elif guessNum == 3:
            userInput = str(input("3: ")) #Guess 
        elif guessNum == 2:
            userInput = str(input("2: "))
        elif guessNum == 1:
            userInput = str(input("1:"))
    

    
        

        
        if userInput == randomWord:  #If userInput == randomWord -> You win!, Score +60
                print("Congratulations, you have selected the Correct word!")
                score = 0
                score = score + 60 # Score decreases by every row
                print("Score:", score)


        elif len(userInput)== 6 and userInput != randomWord:
               
                if guessNum == 6 :
                    print("=====================================")
                    print("Sorry, you did not guess the correct word in 6 tries. Better luck next time.")
                    score = 0
                    print("Score:",score)
                else:
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
                

        
        
    
guess()

