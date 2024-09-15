# Control Poem [ (first line poem) , (second line of poem) ]
# User Poem    [ (first line poem) , (second line of poem) ]

# Function
# compare controlPoem[1] with userPoem[1]
# if yes then do this
# if no then do this

# controlPoem:
# Someone call a paramedic
# I can't speak it's all phonetic
# Made me forget every word 'cause like tha t's a lot of letters
controlPoem = open
inputPoem = []
controlPoem.readlines("alt_shelly.txt")
inputPoem.readlines("alt_shelly.txt")
while True:
    inputPoem.append(input("input line"))
    if input("Enter another Line? (Y/N)").lower() != "y":
        break
    for i in range(len(controlPoem)):
        if controlPoem[0+i] != inputPoem[0+i]:
            print("NO SAME")
            quit()
print("Yes is same")
