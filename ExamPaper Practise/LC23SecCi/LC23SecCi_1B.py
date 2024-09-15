from random import randint


score = 0
replay = None

while True:
    secret_number = randint(1,100)
    user_guess = int(input("Enter your guess: "))
    
    # Checks if user guesses the Jackpot
    if secret_number == user_guess:
        print("Secret number is",secret_number,". You gussed",user_guess+". Difference is",abs(secret_number - user_guess))
        print("JACKPOT!!! You score 100 points")

    elif ((secret_number - 20) > user_guess < (secret_number)) or ((secret_number) > user_guess < (secret_number + 20)):
        print("Secret number is",secret_number,". You gussed",user_guess,". Difference is",abs(secret_number - user_guess))
        print("You score 20 points")
        score += 20
    
    elif ((secret_number - 30) > user_guess < (secret_number)) or ((secret_number) > user_guess < (secret_number + 30)):
        print("Secret number is",secret_number,". You gussed",user_guess,". Difference is",abs(secret_number - user_guess))
        print("You lose 30 points")
        score -+ 30
    
    print("Your total score is",score)
    
    replay = int(input("(1) Replay     (2) Exit\n"))
    if replay == 1:
        None 
    elif replay == 2:
        break
    






