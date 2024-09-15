# gues numbver 1-100
# scret number = random 1-100
# userGuess = input guess
# difference between userGuss and scret number
# 
# if secret number is userGuess
#   Jakpot
# if difference +- 20
#   20 points
# if difference +- 30
#   30 points
#
# ask to replay

import random as pp
score = 0

while True:
    secretNumber = pp.randint(1,100)
    userGuess = int(input("Enter Guess (1-100): "))
    
    # Rule 1: Jackpot
    if secretNumber == userGuess:
        score += 100