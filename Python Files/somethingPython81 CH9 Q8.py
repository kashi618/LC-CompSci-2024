

def validEmail(email):
    # Checks if email is above 8 characters, and if "@" and "." are present
    if "@" in email:
        at = True
    if "." in email:
        dot = True
    if len(email) > 8:
        lengthMin8 = True
    
    # Checks if email is valid using variables from above
    if (at == True) and (dot == True) and (lengthMin8 == True):
        print("Valid Email")
    else:
        print("Not Valid Email")

# Uses validEmail function with user input 
validEmail(input("Enter Email: "))


S