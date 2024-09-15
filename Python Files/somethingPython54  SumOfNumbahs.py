
def sumOfN(n):
    total = 0
    for i in range(n+1):
        total = total + 1
    return total

ans = int(input("Type in the number: "))

if ans == 1:
    theWordIs = "number"
else:
    theWordIs = "numbers"
    
print("The sum of the first",ans,theWordIs," is: ", sumOfN(ans) )

