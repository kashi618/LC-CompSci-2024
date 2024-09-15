def maxOf4 (x,y,z,l):
    if (x>y)and (x>z) and (x>l):
        return x
    elif (y>z) and (x>l) and (x>l):
        return y
    elif (z>y) and (z>x) and (z>l):
        return z
    elif (l>y) and (l>z) and (l>x):
        return l
   
def Truefalse (x):
    if (x/2==0):
        return True
    else:
        return False
   
loop = None
while loop == None:
    maxOf4 = int(input("Num1: ")),int(input("Num2: ")),int(input("Num3: ")),int(input("Num4: "))
    print(maxOf4)
    if Truefalse(maxOf4) == True:
        print("Even")
    else:
        print("Odd")
    
    retry = input("(Y/N)").lower()
    if retry == "n":
        break