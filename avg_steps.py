import csv

infile = open('steps.csv', 'r')
outfile = open ('avg_steps.csv', 'w')

Months = ["January", "February", "March", "April", "May", "June", "July", "August", "Spetember", "October","November", "December"]
Counter_Months = 1

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

outfile.write("Month, Average Steps\n")



for Records in csvfile:

   


    if Months[0] == 1:

        JanSteps = (Steps/Days_In_Month)
        JanSteps = str(JanSteps)

        outfile.write(JanSteps)










    

