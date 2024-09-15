
import random

number = random.randint(1,1000)
high = 1000
guess = int(input("Enter Number Between 1 and 1000: "))

IntorStr = 0
Inta = 1
Stra = 0

if guess.isdigit():
    IntorStr += 1




    
if IntorStr == inta:
    print(" ")
elif guess == number:
    print("Correct")
elif guess > high:
    print("I said 1 and 1000")
elif guess<number:
    print("Too low")
    print("The Number was:", str(number))
elif guess>number:
    print("Too high")
    print("The Number was:", str(number))







if guess == number:
    print("Correct")
elif guess > high:
    print("I said 1 and 1000")
elif guess<number:
    print("Too low")
    print("The Number was:", str(number))
elif guess>number:
    print("Too high")
    print("The Number was:", str(number))
print("END")