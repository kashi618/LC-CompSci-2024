# Questoin 16(a)
# Examination Number:

print("********************")
print("Time Table program")
print("********************")

number = int(input("Enter number: "))
if number <= 0:
    print("This program does not support negative numbers")
    exit()

print("Multiplications of ", number)

for i in range(13):
    print(i,"x",number,"=", number*i)