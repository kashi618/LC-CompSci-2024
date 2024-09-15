
import random

number = random.randint(1,10)
print(number)
replay = 0
counter = 0
while replay < 10:

    while counter < 5:
        
        guess = int(input("Enter Number, 1-10 :"))
        if guess == number:
            print("Correct!")
        elif guess < number:
            print("Too Low")
        elif guess > number:
            print("Too High")
    counter = counter + 1
         

     
print("END")
