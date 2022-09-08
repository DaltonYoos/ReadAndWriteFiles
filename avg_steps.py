import csv

infile = open('steps.csv', 'r')
outfile = open ('avg_steps.csv', 'w')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)


outfile.write('Month, Average Steps\n')

Months_Of_Year = ['Months:','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


Month = 1
Step_Counter = 0
Days_In_Month = 0



for Record in csvfile:

    if Record[0] == str(Month):

        Step_Counter += int(Record[1])

        Days_In_Month += 1
    
    else:

        Average_Steps_Month = format(Step_Counter/Days_In_Month, '.2f')

        outfile.write(Months_Of_Year[int(Month)] + ', ' + str(Average_Steps_Month) + '\n')

        Month = Record[0]

        Step_Counter = int(Record[1])

        Days_In_Month = 1

    

outfile.close()
        