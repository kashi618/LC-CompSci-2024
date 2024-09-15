
totalNonErroneous = 0
countNonErroneous = 0
numBS = [1,-10,4,3,-5,2]

for item in numBS:
    if item >= 0:
        totalNonErroneous += item
        countNonErroneous += 1
averageNonErroneous = totalNonErroneous/ countNonErroneous
print(averageNonErroneous)

for counter in range(len(numBS)):
    if numBS[counter] < 0:
        numBS[counter] = averageNonErroneous
print(numBS)
        