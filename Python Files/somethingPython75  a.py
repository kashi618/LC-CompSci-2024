def playTennis(outlook, humidity, wind):
    if outlook == "Overcast":
        return "Yes"
    elif outlook == "Sunny":
        if humidity == "High":
            return "No"
        else:
            return "Yes"
    else:
        if wind == "Strong":
            return "No"
        else:
            return "Yes"
        
shouldIPlay = playTennis("Sunny","High","Weak")
print(shouldIPlay)