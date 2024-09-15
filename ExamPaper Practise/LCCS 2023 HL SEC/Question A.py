
from random import randint

def guess_game(max_guesses_allowed):
    
    difficulty = input("Enter difficulty (E)asy or (H)ard: ").lower()
    
    if difficulty == "e":
        secret_number = randint(1,5)
    elif difficulty == "h":
        secret_number = randint(1,100)
    
    guess_count = 0
    user_guess = 0
    guessed_number = []
    
    while (user_guess != secret_number):
        
        user_guess = int(input("Enter your guess: "))
        guess_count += 1 #Increase guess_count by 1
        
        
        if guess_count > max_guesses_allowed:
            print("No more guesses!")
            exit()
        
        if user_guess in guessed_number:
            print("You've already guessed this number")
        else:
            if user_guess <= secret_number:
                print("Sorry! Your guess was too low")
            else:
                print("Sorry! Your guess was too high")
        
        if user_guess == secret_number:
            print("Congradulations! You win!")
            print("You took",guess_count,"guesses.")
            
        guessed_number.append(user_guess)
            
print("Welcome to the guessing game!")
guess_game(int(input("Enter the Maximum number of guesses allowed: ")))