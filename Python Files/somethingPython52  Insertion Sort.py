
myList = [95,24,50,63,45,17,31,96]
for index in range(len(myList) - 1):
    print(myList)
    itemInsert = myList[index]
    position = index
    while position > 0 and myList[position - 1] > itemInsert:
        myList[position] = myList[position -1]
        position -=1
    myList[position] = itemInsert
print(myList)