
def validateEmail(emailAddressIn):
    if(emailAddressIn.count("@") == 1 and emailAddressIn.count(".") >= 1 and len(emailAddressIn) >= 8):
        return True
    else:
        return False
    
emailAddress = input("Please enter email address: ")
if(validateEmail(emailAddress)):
    print("Email Address Valid")
else:
    print("Email Address Not Valid")
    