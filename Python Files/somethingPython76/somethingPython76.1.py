import csv
header = ["firstName","lastName","phoneNum","dob","age"]
file = open("patients.csv","a",newline = "")
db = csv.writer(file)
db.writerow(header)
file.close()