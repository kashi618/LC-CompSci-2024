def add(x,y):
    z = x+y
    print(z)
def minus(x,y):
    z = x-y
    print(z)
def multiply(x,y):
    z = x*y
    print(z)
def dividex(x,y):
    z = x/y
    print("answer: "z)

answer = str(input("Would you like to \n (1) Add\n (2) Minus\n (3) Multiple\n(4) divide").lower())

if (answer == "add") or (answer == "1"):
    add(int(input("First number: ")),int(input("Second Number:")))
elif (answer == "minus") or (answer == "2"):
    minus(int(input("First number: ")),int(input("Second Number:")))
elif (answer == "multiply") or (answer == "3"):
    multiply(int(input("First number: ")),int(input("Second Number:")))
elif (answer == "divide") or (answer == "4"):
    divide(int(input("First number: ")),int(input("Second Number:")))    

    
