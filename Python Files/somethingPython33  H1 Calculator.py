marks = 0
whileLoop = True
retry = None

while whileLoop == True:
    H_O = input("Are you (H)igher or (L)ower? ").lower()
    marks = int(input("What is your marks/percentage: "))
    
    if H_O == "h":
        if marks >= 90:
            if marks <= 100:
                print("H1, asmaz")
                
        elif marks >= 80:
            if marks <= 89:
                print("H2, not asian")

        elif marks >= 70:
            if marks <= 79:
                print("H3, beating")

        elif marks >= 60:
            if marks <= 69:
                print("H4, disappointment")
                
        elif marks >= 50:
            if marks <= 59:
                print("H5, disowned")

        elif marks >= 40:
            if marks <= 49:
                print("H6, don't talk to me")
                
        elif marks >= 30:
            if marks <= 39:
                print("H7, are you american?")
                
        elif marks >= 0:
            if marks <= 29:
                print("H8, yu go wok wice fewild")
    else:
        if marks >= 90:
            if marks <= 100:
                print("O1, asmaz")
                
        elif marks >= 80:
            if marks <= 89:
                print("O2, not asian")

        elif marks >= 70:
            if marks <= 79:
                print("O3, beating")

        elif marks >= 60:
            if marks <= 69:
                print("O4, disappointment")
                
        elif marks >= 50:
            if marks <= 59:
                print("O5, disowned")

        elif marks >= 40:
            if marks <= 49:
                print("O6, don't talk to me")
                
        elif marks >= 30:
            if marks <= 39:
                print("H7, are you american?")
                
        elif marks >= 0:
            if marks <= 29:
                print("H8, yu go wok wice fewild")
        
            
    retry = input("Do you wanna try again? (Y/N)").lower()
    
    if retry != "y":
        break
