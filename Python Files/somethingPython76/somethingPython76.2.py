import csv
file = open("patients.csv","r")
records = list(csv.reader(file))
file.close()
print("First Name\t Last Name\t Phone Number\t Date of Birth\t Age")
print("-----------------------------------------------------------------------------")
for record in records [0:]:
    print(record[0],"\t\t",record[1],"\t\t",record[2],"\t",record[3],"\t",record[4])
