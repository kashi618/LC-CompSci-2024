

def volCylinder(radius,height):
    volume = 3.14*(radius**2)*height
    return volume

def unitTest():
    testR = 2
    testH = 1
    expectedVal = 3.14 = (testR ** 2) * testH
    testAns = volCylinder(testR, testH)
    passed = True
    if expectedVal != testAns:
        passed = False
    return passed

print("Test passed: ", unitTest())
        
    
print(vol(int(input("Height: ")),int(input("Radius: "))))


