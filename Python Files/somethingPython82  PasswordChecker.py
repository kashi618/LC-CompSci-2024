# passowrd length = 7
# Include uppercase
# Include lowercase
# Include number

def passwordChecker(password):
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    
    # Checks if password length is 7 and contains a lowercase,uppcase,number
    if len(password) == 7:  # Rule1: length of password is 7
        length7 = True
    for i in range(26):     # Rule2: password contains lowercase
        if alphabet[0+i] in password:
            lowercase = True
    for i in range(26):     # Rule3: password contains uppercase
        if alphabet[0+i].upper() in password:
            uppercase = True
    for i in range(10):     # Rule4: password contains number
        if str(i) in password:
            number = True
    
    # Checks if password is valid and prints results
    if (length7==True) and (lowercase==True) and (uppercase==True) and (number==True):
        print("Valid Password")
    else:
        print("Not Valid Password")

passwordChecker(input("Enter Password: "))

