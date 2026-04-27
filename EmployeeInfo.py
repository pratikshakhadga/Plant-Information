name = str(input("Enter employee name:"))
basicSalary = float(input("Enter basic salary of employee:"))
otherEarnings = float(input("Enter other earnings:"))
allowances = float(input("Enter allowances:"))
deductions = float(input("Enter total deductions:"))
bonusPercent = int(input("Enter bonus percent(x%):"))
numShare = int(input("Enter total number of shares:"))
sharePrice = float(input("Enter price of per share:"))

Gross_Pay = basicSalary+allowances+otherEarnings
Net_Pay = Gross_Pay - deductions
Bonus_Amount = Gross_Pay*(bonusPercent/100)
Stock_Options = numShare*sharePrice
Total_Compensation = Gross_Pay + Bonus_Amount + Stock_Options

print("---Employee Information---")
print("Name of employee:",name)
print("Basic Salary: Rs.",basicSalary)
print("Allowances: Rs.",allowances)
print("Other Earnings: Rs.",otherEarnings)
print("Total Deductions: Rs.",deductions)
print("Gross Pay of employee: Rs.",Gross_Pay)
print("Net Pay of employee: Rs.",Net_Pay)
print("Bonus Percent:",bonusPercent,"%")
print("Bonus Amount of employee: Rs.",Bonus_Amount)
print("Total number of shares:",numShare)
print("Price of each share: Rs.",sharePrice)
print("Stock Options of employee: Rs.",Stock_Options)
print("Total Compensation of employee: Rs.", Total_Compensation)