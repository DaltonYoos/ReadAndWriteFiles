import csv

infile = open('steps.csv', 'r')
outfile = open ('avg_steps.csv', 'w')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

outfile.write("Month, Avg Steps\n")

