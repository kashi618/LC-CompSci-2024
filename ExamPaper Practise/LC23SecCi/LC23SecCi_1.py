from random import randint

guess_count = 0
user_guess = 0
max_guess = 0

print("Welcome to the guessing game!")

max_guess = int(input("Enter maximum number of guesses allowed: "))

difficulty = int(input("Enter difficulty\n (1) Easy     (2) Hard\n "))
if difficulty == "1":
    secret_number = randint(1,5)
elif difficulty == "2":
    secret_number = randint(1,100)

while (user_guess != secret_number):
    user_guess = int(input("Enter your guess: "))
    guess_count += 1
    
    if guess_count == max_guess:
        print("Your out of guesses")
        break
    
    if user_guess == secret_number:
        print("congradulations! You win!")
        print("You took",guess_count,"guesses!")
    elif user_guess < secret_number:
        print("Sorry! Your guess was too low")
    else:
        print("Sorry! Your guess was too high")


