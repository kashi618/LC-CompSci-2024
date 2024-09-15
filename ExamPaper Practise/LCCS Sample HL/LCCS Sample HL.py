bmi_values = [24, 19, 33, 35, 27, 18, 15, 33, 35, 23, 32, 23]
obesity_values = []
obese = 0

#def bmi(height,weight):
#    bmi = ((weight / pow(height,2)) * 10000)

def find_nth_largest(n, list_of_values):
    print(obesity_values[n-1])
    

for i in range(13):
    if bmi_values[i-1] > 30:
        obese += 1
        obesity_values.append(bmi_values[i]) 
obesity_values.sort()

print(find_nth_largest(int(input("What kind of fat on the scale of fat peepo do you need")),obesity_values))