import csv

record1 = ["Joan", "Byrne", "0981 45877", "2/2/75","45"]
record2 = ["Gideon", "Jones", "098376800",  "4/7/59" ,"61"]
record3 = ["Noor", "Patel","0983 54689", "3/6/03","17"]
file = open("patients.csv","a",newline="")
db = csv.writer(file)
db.writerow(record1)
db.writerow(record2)
db.writerow(record3)
file.close()
