import math, turtle

# Triangle Properties
RightAngle  = None # (True/False)      #-Does the triangle contain right angle
SideOrAngle = None # ("side"/"angle")  #-Do you want to find Side or Angle
AmountSides = None # (1-3)             #-Amount of sides known
AmountAngle = None # (1-3)             #-Amount of angles known
# Right angle Trangle lengths and angle
hyp = None                             #-Length of Hypotenuse
adj = None                             #-Length of Adjacent
opp = None                             #-Length of Opposite
deg = None                             #-Value of angle
# Triangle Lengths and angles
side1  = None                          #-Length of side 1
side2  = None                          #-Length of side 2
side3  = None                          #-Length of side 3
angle1 = None                          #-Value of angle 1
angle2 = None                          #-Value of angle 3
angle3 = None                          #-Value of angle 3

######################################

# Converts Degrees and Radians
def DegToRad(degree):
    ans = degree * (math.pi/180)
    return ans
def RadToDeg(radian):
    ans = radian * (180/math.pi)
    return ans
   
# Pythagoras Theorem   
def pythagoras(hypo, side1, side2):  
        # Calculates length of hypotenuse
    if hypo == 0:
        unknownSide = math.sqrt((side1**2) + (side2**2))
        ans = "The length of the hypotenuse is, "+ str(round(unknownSide,4))+ " (rounded to 4 decimal places)"
        return ans  
        # Calculates length of side 1                 
    elif side1 == 0:
        unknownSide = math.sqrt( (hypo**2) - (side2**2) )      
        ans = "The length of side 1 is, "+ str(round(unknownSide,4))+ " (rounded to 4 decimal places)"
        return ans    
        # Calculates length of side 2     
    elif side2 == 0:
        unknownSide = math.sqrt( (hypo**2) - (side1**2) )      
        ans = "The length of side 2 is, "+ str(round(unknownSide,4))+ " (rounded to 4 decimal places)"
        return ans

# Sin formula
def sin(deg,opp,hyp):
    if opp == 0:
        rad = DegToRad(deg)
        ans = round(math.sin(rad)*hyp,2)
        return ans  
      
    elif hyp == 0:
        rad = DegToRad(deg)
        ans = round(opp/math.sin(rad),2)
        return ans  
    
    elif deg == 0:       
        deg = RadToDeg(math.asin(opp/hyp))
        ans = round(deg,2)
        return ans

# Cos formula
def cos(deg,adj,hyp):
    if adj == 0:
        rad = DegToRad(deg)
        ans = round(math.cos(rad)*hyp,2)
        return ans
    elif hyp == 0:
        rad = DegToRad(deg)
        ans = round(adj/math.cos(rad),2)
        return ans
    elif deg == 0:
        deg = RadToDeg(math.acos(adj/hyp))
        ans = round(deg,2)
        return ans

# Tan formula
def tan(deg,adj,opp):
    if opp == 0:
        rad = DegToRad(deg)
        ans = round(math.tan(rad)*adj,2)
        return ans
    elif adj == 0:
        rad = DegToRad(deg)
        ans = round(opp/math.tan(rad),2)
        return ans
    elif deg == 0:
        deg = RadToDeg(math.atan(opp/adj))
        ans = round(deg,2)
        return ans

######################################

# Introduction
print("#############################################################################################################################")
print("##-----------------Welcome to our ALT 3 project on Simulations And Models (by Neil.J, Gabriel.C, Ross.N)-------------------##") 
print("##--This is our Trilateral Triangle Solver, abbrieviated (T.T.S)-----------------------------------------------------------##")
print('##--This program will use trigonometry to compute and solve "possible" lengths and angles of a triangle--------------------##')
print("##--No prior knowledge of trigonometry is necessary, only basic math :) ---------------------------------------------------##")  
print("#############################################################################################################################")

######################################

# Asks if contains right angle
while True: 
    RightAngle = input("Does your triangle contain a right angle, 90\N{degree sign}?\n(Yes/No): ").lower()
    
    if RightAngle == "yes":
      RightAngle = True
      break
    elif RightAngle == "no":
      RightAngle = False
      break

# Asks if side or angle needs to be found
while True: 
    SideOrAngle = input("\nDo you want to find a Side or an Angle?\n(side/angle): ").lower()
    
    if SideOrAngle == "side":
        break
    elif SideOrAngle == "angle":
        break

# Asks amount of known sides
while True: 
    AmountSides = input("\nHow many SIDES of the triangle do you know the length of?\n(1,2,3): ")
    if AmountSides == "1":
        break
    elif AmountSides == "2":
        break
    elif AmountSides == "3":
        AmountAngle = "2"
        break
   
# Asks amount of known angles
while RightAngle==False: 
    AmountAngles = input("\nHow many ANGLES of the triangle do you know the value of?\n(1,2,3): ")
    if AmountAngles == "1":
        break
    elif AmountAngles == "2":
        break
    elif AmountAngles == "3":
        AmountAngles = "2"
        break

######################################

# Pythagoras Theorum inputs
if (RightAngle == True and SideOrAngle == "side" and AmountSides == "2"):
    ans = pythagoras(
    int(input("Enter the length of the HYPOTENUSE\n(0 if unknown): ")),
    int(input("Enter the length of the ADJACENT\n(0 if unknown): ")),  
    int(input("Enter the length of the OPPOSITE\n(0 if unknown): ")) 
    )
    print("#############################################################################################################################")
    print("The Method Used: Pythagoras Theorum")
    print(ans)
    print("#############################################################################################################################")
    
# Sin, Cos, Tan inputs
if (RightAngle == True and SideOrAngle == "side" and AmountSides == "1"):
    SideToFind = int(input("\nWhich side would you like to find?\n(1) Hypotenuse\n(2) Adjacent\n(3) Opposite\n: "))
    deg = int(input("Enter the value of the angle\n(0< x >360): "))
    
    if SideToFind == 1: # finding Hypotenuse
        adj = int(input("\nEnter the Length of the ADJACENT\n(0 if unknown)"))
        opp = int(input("\nEnter the Length of the OPPOSITE\n(0 if unknown)"))
        
        if adj == 0:
            ans = sin(deg,opp,0)
            print("#############################################################################################################################")
            print("The Method Used: Sin Formula")
            print("The length of the hypotenuse is, "+str(ans)+ " (rounded to 4 decimal places)")
            print("#############################################################################################################################")
        elif opp == 0:
            ans = cos(deg,adj,0)
            print("#############################################################################################################################")
            print("The Method Used: Cos Formula")
            print("The length of the hypotenuse is, "+str(ans)+ " (rounded to 4 decimal places)")
            print("#############################################################################################################################")
            
    if SideToFind == 2: # finding adjacent
        adj = 0
        hyp = int(input("\nEnter the Length of the HYPOTENUSE\n(0 if unknown)"))
        opp = int(input("\nEnter the Length of the OPPOSITE\n(0 if unknown)"))
        
        if hyp == 0:
            ans = tan(deg,opp,0)
            print("#############################################################################################################################")
            print("The Method Used: tan Formula")
            print("The length of the adjacent is, "+str(ans)+ " (rounded to 4 decimal places)")
            print("#############################################################################################################################")
        if opp == 0:
            ans = cos(deg,0,hyp)
            print("#############################################################################################################################")
            print("The Method Used: cos Formula")
            print("The length of the adjacent is, "+str(ans)+ " (rounded to 4 decimal places)")
            print("#############################################################################################################################")
             
    if SideToFind == 3: # finding opposite
        opp = 0
        adj = int(input("\nEnter the Length of the ADJACENT\n(0 if unknown)"))
        hyp = int(input("\nEnter the Length of the HYPOTENUSE\n(0 if unknown)"))
        
        if adj == 0:
            ans = sin(deg,0,hyp)
            print("#############################################################################################################################")
            print("The Method Used: sin Formula")
            print("The length of the opposite is, "+str(ans)+ " (rounded to 4 decimal places)")
            print("#############################################################################################################################")
        
        if hyp == 0:
            ans = tan(deg,0,adj)
            print("#############################################################################################################################")
            print("The Method Used: tan Formula")
            print("The length of the opposite is, "+str(ans)+ " (rounded to 4 decimal places)")
            print("#############################################################################################################################")
              
# invSin, invCos, invTan inputs
if (RightAngle == True and SideOrAngle == "angle" and AmountSides == "1"):
        opp = int(input("\nEnter the Length of the OPPOSITE\n(0 if unknown)"))
        hyp = int(input("\nEnter the Length of the HYPOTENUSE\n(0 if unknown)"))
        adj = int(input("\nEnter the Length of the ADJACENT\n(0 if unknown)"))
        
        if opp == 0:
            ans == cos(0,opp,hyp)
        elif hyp == 0:
            ans == tan(0,opp,adj)
        elif adj == 0:
            ans == sin(0,opp,hyp)
        print(ans)
        