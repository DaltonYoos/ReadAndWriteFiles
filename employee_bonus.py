import csv

infile = open('EmployeePay.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

for record in csvfile:

    ESalary = int(record[3])
    EBonus = float(record[4])

    Bonus_Pay = (ESalary * EBonus)

    Total_Pay = (ESalary + Bonus_Pay)

    Bonus = '{:.2f}'.format(Bonus_Pay)

    print("Employee ID:", record[0])
    print("Name:", record [1] + " " + record[2])
    print("Salary: $", record[3], sep="")
    print("Bonus Payment: $", Bonus, sep="")
    print("Total Employee Pay: $", Total_Pay, sep="")
    input()
