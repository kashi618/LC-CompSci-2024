
heightFile = open("heights.csv","r")

totalHeight = 0

height = float(heightFile.readline())
totalHeight = totalHeight + height

height = float(heightFile.readline())
totalHeight = totalHeight + height

height = float(heightFile.readline())
totalHeight = totalHeight + height

height = float(heightFile.readline())
totalHeight = totalHeight + height

avgHeight = totalHeight / 5

print("avg height = ", str(avgHeight), "cm")

avgHeightIN = round(avgHeight*0.393701,2)

print("avg height = ", avgHeightIN, "in")
