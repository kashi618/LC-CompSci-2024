def volCylinder(radius,height):
    volume = 3.14 * (radius ** 2) * height
    print("The Volume is:", volume)

radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
volCylinder(radius,height)
