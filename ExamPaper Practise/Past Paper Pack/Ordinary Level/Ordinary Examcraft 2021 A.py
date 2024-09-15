# This program is a simple ordering system

print("Welcome to the new online ordering system.\n")
total_cost = 0
staffMemberName = input("Please enter your user name: ")

item_count = int(input("How many items are in the customers order:"))
if item_count <= 0:
    print("Invalid")


for i in range(item_count):
    priceOfItem = float(input("Enter price of item " + str(i+1) + " : €"))
    total_cost += priceOfItem

print("You entered", item_count,"items and the total is €", total_cost)
print("The member of staff who processed your oder was:", staffMemberName)
customerBalance = float(input("What is the customers account balance €"))
print("Your remaining balance is: €", total_cost - customerBalance)

if total_cost > customerBalance:
    print("The customer does not have enough credit in their account, they still owe: €", abs(total_cost - customerBalance))