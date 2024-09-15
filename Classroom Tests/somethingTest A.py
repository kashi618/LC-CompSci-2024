# Question 16(a)
# Student Name: Neil Jiang

length = 0
width = 0

print("This program can find the perimeter or area of a quadrilateral")

length = float(input("Please enter length: "))
width = float(input("Please enter width: "))

name = input("Please enter your user name: ")
choice = input("Do you want to find the (p)erimeter or (a)rea? ")

if choice == "p":
    print("A quadrilateral with a length of ",length," and a width of ",width,", has a perimiter of:",round(length*2 + width*2,2))
  
elif choice == "a":
    print("A quadrilateral with a length of ",length," and a width of ",width,", has an area of: ",round(length*width,2) )


print("Thank you for using the program", name)
