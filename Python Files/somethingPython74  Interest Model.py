def finalAmount(principalAmount,interest,years):
    finalAmount = principalAmount * ((1+interest) ** years) 
    return finalAmount

print(finalAmount(10000,0.032,6))