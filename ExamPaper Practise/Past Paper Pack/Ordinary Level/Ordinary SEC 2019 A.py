

# This calculator can only add or subtract
name = input("Please enter your name: ")
print("Hello",name+".")
print("Welcome to the addition and subtraction calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while True:
    choice = input('Do you want me to (a)dd or (s)ubtract?').lower()
    
    if choice == 'a':
        print (num1,"+",num2,"=",num1+num2)
        break
    elif choice == 's':
        print (num1,"-",num2,"=",num1-num2)
        break
    else:
        print("Invalid Option")
