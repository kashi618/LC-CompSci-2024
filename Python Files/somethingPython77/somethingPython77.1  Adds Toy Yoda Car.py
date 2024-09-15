import csv

header = ["MaK3","m0dEl","R3G"]
file = open("myGarage.csv","a",newline = "")
db = csv.writer(file)
db.writerow(header)
file.close()