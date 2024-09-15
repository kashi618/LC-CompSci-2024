def readIntegerInRange(lwr,upr):
    valid = False
    while not valid:
        strN = input("Enter a Number: ")
        if strN.isdigit():
            n = int(strN)
            if(n >= lwr) and (n <= upr):
                valid = true
    return n
            
readIntegerInRange(int(input("lower: ")),int(input("upper: ")))


