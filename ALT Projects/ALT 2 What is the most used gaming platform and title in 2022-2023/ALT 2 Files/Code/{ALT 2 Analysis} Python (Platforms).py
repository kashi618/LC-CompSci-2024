import matplotlib.pyplot as plt
import csv
  
Subjects = []
Scores = []
  
with open('{ALT 2 Analysis} DataSet (Platforms).csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter = ',')
    for row in lines:
        Subjects.append(row[0])
        Scores.append(int(row[1]))
  
plt.pie(Scores,labels = Subjects,autopct = '%.2f%%')
plt.title('Platforms', fontsize = 25)
plt.show()




