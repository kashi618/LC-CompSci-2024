# Question 16(b)
# Student Name: Neil Jiang

import random

win = ""

computer_options = ["rock","paper","scissors"]
computer_choice = computer_options[random.randint(0,2)]
computer_choiceSTR = str(computer_choice)


player_input = input("Enter (R)ock, (P)aper or (S)cissors: ")


if player_input is str("r"):
    player_choice = "Rock"
    

print("Player chose:", player_choice)
print("Computer chose:", computer_choice)



if player_choice is "rock" and computer_choiceSTR is "paper": #Rock Paper
    win = "Computer wins"
    print(win)
    
elif player_choice is "paper" and computer_choice is "paper": #Paper Paper
    win = "player wins"
    print(win)
    
elif player_choice is "scissors" and computer_choice is "paper": #Scissors Paper
    
    
elif player_choice is "rock" and computer_choice is "rock":
    
elif player_choice is "paper" and computer_choice is "rock":
    
elif player_choice is "scissors" and computer_choice is"rock":
    
    
#elif player_choice is "rock" and computer_choice is ["scissors"]:
    
#elif player_choice is "paper" and computer_choice is ["scissors"]:
    
#elif player_choice is "scissors" and computer_choice is ["scissors"]: 
    

