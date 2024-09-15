squaredNumbers = []

# Calculates and stores the squared numbers in a list
for i in range(20):
    squaredNumbers.append(i*i)

# Function which returns a specific squared number
def squared(x):
    return squaredNumbers[x+1]

# Prints the specified squared number
print("Which squared number will I display (1-20)?", squared(int(input(""))))
