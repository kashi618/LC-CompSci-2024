import random

loop = 0
n1 = random.randint(0,12)
n2 = random.randint(0,12)
ans = n1*n2
print("%d * %d" %(n1,n2))

while loop <= 3:
    userAns = float(input("Enter your answer: "))
    if float(userAns) == float(ans):
        print("Correct!")
        break
    else:
        if  float(userAns) >= float(ans):
            print("YOUR ANSWER IS TOO HIGH LIKE")
        elif float(userAns) <= float(ans):
            print("YOUR ANSWER IS TOO LOW LIKE")
        loop += 1

print("The correct answer was %d" %(n1*n2))
print("Goodbye")