import random

number = random.randint(1,10)

keepGoing = True

while keepGoing:
    
    guess = input("Enter a number (1-10): ")
    
    while not guess.isdigit():
        guess = input("Enter a number (1-10): ")
        
    guess = int(guess)
    
    if guess == int(guess)
    
    if guess == number:
        print("Correct !")
        goAgain = input("play again? (Y/N): ")
        if go again.upper() == "N"
            keepGoing = False
        else:
            number = random.randint(1,10)
        
    elif guess < number:
        print("Too low")
    else:
        print("Too high")
        
print("Goodbye")
        
    