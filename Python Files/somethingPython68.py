x = int(input("enter you're number please: "))
x = (x/2) * ((x/2)+1)
if (x%2) != 0:
    x += .25
print(x)