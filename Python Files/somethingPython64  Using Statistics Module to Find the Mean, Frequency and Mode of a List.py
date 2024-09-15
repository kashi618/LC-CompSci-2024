import statistics
myList = [1,19,27,8,5,9]
colourList = ["red","blue","blue","red","green","red","red"]

## Finds the Mean
mean = statistics.mean(myList)
## Find the median
median = statistics.median(myList)
## Finds the Mode
mode = statistics.mode(colourList)




print("mean  :",mean)
print("median:",median)
print("mode  :",mode)