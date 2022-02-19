from difflib import diff_bytes
from random import random, randrange #Import random


words = ["REALLY", "LITTLE", "SHOULD", "PLEASE", "PEOPLE", "THINGS", "BETTER"]
randomWord = randrange(0, 5, 1)
difficulty = 0

print("---Python Wordle---")
print("=====================================")
print("The word has six letters and you have 5 chances to correctly guess the word")