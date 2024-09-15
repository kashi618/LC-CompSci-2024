
import random

computer_options = ["rock", "paper", "scissors"]

computer_choice = computer_options[random.randint(0,2)]

playerInput = input("Enter rock, paper, or scissors: ").lower()
print("Player chose:",playerInput,"\nComputer chose:",computer_choice)


if computer_choice == playerInput:
    print("Draw!")   
if ((computer_choice=="rock")and(playerInput=="scissors")) or ((computer_choice=="scissors")and(playerInput=="paper")) or ((computer_choice=="paper")and(playerInput=="rock")):
    print("Computer Wins")
else:
    print("Player Wins")
