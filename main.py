from difflib import diff_bytes
from random import random, randrange #Import random
import time


random = randrange(1, 8, 1)  #Range of Words 
difficulty = 0 # Difficulty level-yet to be integrated




print("---Python Wordle---") #Print Title
print("=====================================")
print("Please input a difficulty level (1,2,3)")
print("=====================================")
difficulty = int(input("Difficulty: "))
print("The word has six letters and you have 5 chances to correctly guess the word")

print("=====================================") # First Guess


count = 0

guessNum = 0




def guess(): 
    global guessNum
    global score
    global userInput

    
    
  
    
    
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
                compareStrings()

        elif len(userInput)== 6 and userInput != randomWord:
               
                if guessNum == 6 :
                    print("=====================================")
                    print("Sorry, you did not guess the correct word in 6 tries. Better luck next time.")
                    score = 0
                    print("Score:",score)
                    time.sleep(10)
                else:
                     print("Sorry, that is not the correct word. ")
                     guess()
                     score = score -10 
                     print("Score:",score)
                     #compareStrings()


        elif len(userInput) > 6 or len(userInput) < 6:
                print("Wrong word size. Try Again")
                userInput = str(input("Again:"))
                if len(userInput) == 6 and userInput == randomWord:
                    print("You Guessed the word!")
                    score = score +60
                    compareStrings()
                else:
                    print("You did not pick the correct word")
                    guess()
                    compareStrings()

def compareStrings():
    global results
    results = "" #FIX
    for i in range(6):
        if userInput[i] == randomWord[i]:
            results = results + userInput[i]    
            if i == 5:
                print("=====================================")  
                print(results)
                time.sleep(10)
        '''
        elif userInput[i] != randomWord[i]:
            if i == 0:
                results = results + "X"
            elif i == 1:
                results = results + "X"
            elif i == 2:
                results = results + "X"
            elif i == 3:
                results = results + "X"
            elif i == 4:
                results = results + "X"
            elif i == 6:
                results = results + "X"
            print(results)
            print(i)
            if i == 5:
                print(results)
        '''

def difficultyLevels():
    global randomWord
    if difficulty == 1:
        easyWords = ["Really", "Little", "Should", "Please", "People", "Things", "Better", "Number", "Aboard", "Actual" ] #List of Words
        randomWord = easyWords[random]
    if difficulty == 2:
        mediumWords = ["Abacus","Abated", "Abhors", "Ablaze", "Acacia", "Accost", "Acidic", "Adhere" , "Adored", "Advent"]
        randomWord = mediumWords[random]

        

difficultyLevels()   
guess()

