def thermostatModel(actual,target):
    if actual < target:
        return 1
    else:
        return 0
    
tempOnOrOff = thermostatModel(18,22)
print(tempOnOrOff)