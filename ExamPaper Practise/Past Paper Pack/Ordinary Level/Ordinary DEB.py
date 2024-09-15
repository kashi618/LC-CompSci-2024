import random # Used to randomise 

# Function which returns location for vaccine
def vacLocation(eircode):
    eircodeStripped = eircode.strip()
    eirLastDigit = int(eircodeStripped[-1])
    if (eirLastDigit % 2) == 0:
        return "Eastwood"
    else:
        return "Northfield"
    
# Function which returns the type of vaccine
def vacType(age):
    if age > 50:
        return "MRNA"
    elif (age >= 12) or (age <= 49):
        return "ADENO"
    
# Function which returns vaccine A,B,C if user enrols in vaccine style
def vaccineTrialFunction(YN):
    if YN == "yes":
        return random.choice(vaccineTrialList)
    else:
        return False

vaccineTrialList = ["A","B","C"]

while True: # Asks for Surname, Name, Age, Eircode, vaccine trial
    s_name = input("Enter your surname: ")
    f_name = input("Enter your first name: ")
    age = int(input("Enter your age: "))
    eircode = input("Enter your eircode: ")
    vaccineTrial = input("Do you agree to enrol in a vaccine trial?\nType 'Yes' or 'No'\t\t").lower()
    
    # Prints welcome, location of vaccine, type of vaccine
    print("Hello", f_name,s_name, "you are", age, "years old and your eircode is", eircode) 
    print("You must attend",vacLocation(eircode),"for your vaccine")  
    
    # Prints out vaccine type
    if vaccineTrial == False:
        print(f_name,"you will recieve the",vacType(age),"vaccine")
    else:
        print("You are now enrolled in the trial to receive Super vaccine",vaccineTrialFunction(vaccineTrial))
    
    # Asks if user wants to continue
    if (input("If you have finished entering people's details type 'END', otherwise press RETURN: ").lower()) == "end":
        break
