import csv

infile = open('EmployeePay.csv', 'r')

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)

for record in csvfile:

    ESalary = int(record[3])
    EBonus = float(record[4])

    Bonus_Pay = (ESalary * EBonus)

    Total_Pay = (ESalary + Bonus_Pay)

    print("Employee ID:", record[0])
    print("Name:", record [1] + " " + record[2])
    print("Salary: $", record[3])
    print("Bonus Payment: $", Bonus_Pay)
    print("Total Employee Pay: $", Total_Pay)
    input()
