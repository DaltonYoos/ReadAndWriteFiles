import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile) #This will skip the first row

for record in csvfile:
    #print(record)

    print("ID:", record[0])
    print("First Name:", record[1])
    print("Last Name:", record[2]) 
    print("City:", record[3])
    print("Country:", record[4])
    print("Phone:", record[5])
    input()

    

