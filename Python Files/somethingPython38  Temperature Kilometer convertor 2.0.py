
celsius_to_farhenheight = None
distance_temperature = None
loop = True

def cels_farh(cels):
    return (9/5*cels +32)
def farh_cels(farh):
    return (5/9* farh-32)

def kilo_miles(kilometer):
    return(kilometer / 1.609)
def miles_kilo(miles):
    return(miles * 1.609)
    
while loop == True:
    distance_temperature = input("Would you like to convert [(D)istance] OR [(T)emperature]? ").lower()
    
    if distance_temperature == "t":
        celsius_to_farhenheight = input("1. Celsius >> Farhenheight\n2. Farhenheight >> Celsius\n").lower()
        
        if celsius_to_farhenheight == "1":
            print("Celsius >> Farhenheight")
            celsius = int(input("Celsius: "))
            farh = cels_farh(celsius)
            print(round(farh,2))
        
        elif celsius_to_farhenheight == "2":
            print("Farhenheight >> Celsius")
            farh = int(input("Farhenheight: "))
            cels = farh_cels(farh)
            print(round(cels,2))
                        
    if distance_temperature == "d":
        kilometer_to_miles = input("1. Kilometers >> Miles\n2. Miles >> Kilometer\n").lower()
        
        if kilometer_to_miles == "1":
            print("Kilometers >> Miles")
            kilometer = int(input("Kilometer: "))
            miles = kilo_miles(kilometer)
            print(round(miles,2))
        
        elif kilometer_to_miles == "2":
            print("Miles >> Kilometers")
            miles = int(input("Miles: "))
            kilometer = miles_kilo(miles)
            print(round(kilometer,2))
            
    retry = input("try again? (Y/N) ").lower()
    if retry != "y":
        break
        