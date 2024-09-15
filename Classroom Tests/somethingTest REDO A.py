def perimeter(x,y):
    ans = (x*2) + (y*2)
    return round(ans,2)
def area(x,y):
    ans = x*y
    return round(ans,2)

print("This program can find the perimeter or area of a quadrilateral")
length = float(input("Please enter Length: "))
width = float(input("Please enter Width: "))
name = input("Please enter your user name: ")
area_perimeter = input("Do you want to find the (p)erimeter or (a)rea? ")

if area_perimeter == "p":
    print("A quadrilateral with a length of",length,"and a width of",width,"has a perimiter of:",perimeter(length,width))
elif area_perimeter == "a":
    print("A quadrilateral with a length of ",length,"  and a width of ",width," , has a area of:",area(length,width))
    
print("Thank you for using the program",name)