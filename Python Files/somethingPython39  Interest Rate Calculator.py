
def future_value(principal,rate,time):
    fv = principal * (pow((1 + rate / 100),  time))
    return fv

loop = None

while loop == None:
    fv_A = future_value(1,1,1)
    fv_B = future_value(int(input("Principal: ")),int(input("Rate: ")),int(input("Time: ")))

    print("Scenario A: %.2f \nScenario B: %.2f"%(fv_A,fv_B))

      

