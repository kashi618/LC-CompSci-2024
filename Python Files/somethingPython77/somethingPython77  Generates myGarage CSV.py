import csv

record1 = ["Hoda","c1VIc","i91=d-1354"]
record2 = ["Nisin","Pulveriser","a9w_11-126a2"]
record3 = ["Dowdey","a ate","20a-k-1d15"]
file = open("myGarage.csv","a",newline="")
db = csv.writer(file)
db.writerow(record1)
db.writerow(record2)
db.writerow(record3)
file.close()
print("yippee, it werked")
