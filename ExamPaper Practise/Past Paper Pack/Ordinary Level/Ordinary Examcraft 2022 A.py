length = 6
width = 4

print("This program can find the perimeter or area of a quadrilateral")

length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))
name = input("Please enter your namer")
choice = input("Do you want to find the (p)erimeter or (a)rea? ")

if choice == "p":
    perimeter = round(length + length + width + width,2)
    print("A quadrilateral with a length of",length,"and a width of",width,"has a perimeter of", perimeter)
    
elif choice == "a":
    are = round(length*width,2)
    print("A quadrilateral with a length of",length,"and a width of",width,"has an area of", are)


print("Thank you for using the program",name)
