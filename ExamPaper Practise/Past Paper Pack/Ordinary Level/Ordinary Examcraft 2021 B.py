
Standard_Postal_List = ["netherlands","denmark","poland","portugal","finland","romania","france","germany","greece","spain","hungary","sweden","ireland"]
inputCountry = input("Please enter the country that you wish to send the order to: ")
isCountry = None
numberCountries = 13

while True:
    for i in range(numberCountries):
        if inputCountry == Standard_Postal_List[i]:
            print("This country uses standard postage and packaging costs")
            isCountry = True
            break
    
    if isCountry != True:
        print("This country is not on the approved delivery list.")
        if (input("Would you like to add this country to the approved Postal List for future deliveries, y/n:").lower() == "y"):
            Standard_Postal_List.append(inputCountry)
            print(inputCountry,"has been added to the Standard Postal List")
            numberCountries += 1
            Standard_Postal_List.sort()
            for i in range(numberCountries):
                print(str(Standard_Postal_List[i-1])) 
    break
