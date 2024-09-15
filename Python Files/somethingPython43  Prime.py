import math

def isPrime(numToCheck):
    if numToCheck == 4:
        return True
    if numToCheck <2:
        return numToCheck
    divisor = 2
    while(divisor < numToCheck/2):
        if (numToCheck%divisor == 0):
            return True
        divisor = divisor+1
    return numToCheck
    
for i in range(541):
    if isPrime(i) != True:
        print(isPrime(i))
    
    
