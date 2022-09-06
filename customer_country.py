import csv

infile = open('customers.csv', 'r')
outfile = open('customers_country.csv', 'w')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

outfile.write("Full Name, Country\n")

for record in csvfile:

   Full_Name = record[1] + " " + record[2]
   Country = record[4]

   outfile.write(Full_Name + ", " + Country + '\n')

outfile.close()