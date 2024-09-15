def factors (x,y):
    list_factor_x = []
    list_factor_y = []
    
    # Finding the Factors of the X and adding it to list X
    divisor_x = 1
    while divisor_x <= x/2:
        if x % divisor_x == 0:
            list_factor_x.append(divisor_x)
        divisor_x += 1
    list_factor_x.append(x)
    
    # Finding the Factors of the Y and adding it to list Y
    divisor_y = 1
    while divisor_y <= y/2:
        if y % divisor_y == 0:
            list_factor_y.append(divisor_y)
        divisor_y += 1
    list_factor_y.append(y)
    
    # Prints Factors
    print("Factors of", x , "is" , list_factor_x)
    print("Factors of", y , "is" , list_factor_y)
    
    # Prints HCF 
    if int(len(list_factor_x)) or int(len(list_factor_y)) == 2:
        print("The HCF is: 1  :(")
    elif int(len(list_factor_x)) > int(len(list_factor_y)):
        print("The HCF is :",list_factor_y[-1])
    else:
        print("The HCF is :",list_factor_x[-1])
          
#  Inputs
factors(int(input("NUMBER 1:  ")),int(input("NUMBER 2:  ")))

