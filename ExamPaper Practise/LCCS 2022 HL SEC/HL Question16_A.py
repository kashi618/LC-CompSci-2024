# Question 16(a)
# Examination Number: 
from random import randint

print("Dice simulation and analysis program")
results = []
frequencies = [0, 0, 0, 0, 0, 0]

# Loop 100 times
for i in range (100):
    throw_result = randint(1,6) # store a random value between 1 and 6
    results.append(throw_result) # append each value to results

    # Start to build up a list of frequencies for each value thrown
    for i in range(7):
        
        if throw_result == i:
            frequencies[i-1] = frequencies[i-1] + i


# print("Results:", results)
print("Frequencies",frequencies)
print("Dice Frequency\n---- ---------")

for i in range(6):
    print(i+1, "\t",frequencies[i])
print()

for freq in frequencies:
    for i in range(freq):
        print("*",end="")
    print()

