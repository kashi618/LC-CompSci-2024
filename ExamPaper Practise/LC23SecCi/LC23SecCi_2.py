print("Multiplication program")
number = None

print("*******************")
print("Times Table Program")
print("*******************")

number = int(input("Enter number:"))
print("Multiplications of ",number)
if number <= 0:
    print("This program does not support negative")
else: 
    for i in range(10):
        print(number*i)

