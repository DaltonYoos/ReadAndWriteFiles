import csv

infile = open('customers.csv', 'r')

outfile = open('customer_country.csv', 'w')
outfile.write("Full Name, Country")
outfile.write("\n")

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

i = 1

for record in csvfile:

    i += 1 
    Full_Name = [record[1], record[2]]
    Country = [record[4]]

outfile.write(Full_Name + Country)

print("There are", i, "customers on file.")