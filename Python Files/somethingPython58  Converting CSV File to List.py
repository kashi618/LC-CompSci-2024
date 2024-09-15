file = open("mySecondCSVFile.csv","r")
dataIn = file.read()
file.close()

myList = dataIn.split(",")
myList = [int(item) for item in myList]
print(myList)