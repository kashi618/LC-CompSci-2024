def isLeap(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False
    
yr = int(input("Enter a year: "))
if isLeap(yr):
    print(yr, "is a leap year")
else:
    print(yr,"It is not a Leap YEAR")