def readIntegerV1():    
    strN = input("Enter a number: ")
    while not strN.isdigit():
        strN = input("Enter a number")        
    return int(strN)

def readIntegerV2():
    valid = False
    while not valid:
        strN = input("Enter a number: ")
        if strN.isdigit():
            valid = True           
    return int(strN)

def readIntegerV3():
    while True:
        strN = input("Enter a number: ")
        if strN.isdigit():
            break
        
def readIntegerV4():
    while True:
        strN = input("Enter a number: ")
        if strN.isdigit():
            break
    return int(strN)

def readIntegerVBEST():
    while True:
        strN = input("Enter a number only: ")
        if strN.isdigit():
            break 
    return int(strN)

print("VERSION !")
readIntegerV1()
print("VERSION !!")
readIntegerV2()
print("VERSION !!!")
readIntegerV3()
print("VERSION !!!!")
readIntegerV4()

print("Version THE BEST")
readIntegerVBEST()