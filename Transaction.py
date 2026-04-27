number = str(input("Enter your account number: "))
name = str(input("Enter your account holder name: "))
balance1 = float(input("Enter your balance: "))
amount1 = float(input("Enter amount to be deposited: "))
deposit = balance1 + amount1
amount2 = float(input("Enter amount to be withdrew: "))
withdraw = deposit - amount2
print("Account Number: ",number)
print("Account Holder Name: ",name)
print("Balance: Rs.",balance1)
print("Deposited: Rs.",amount1)
print("Amount after deposit: Rs.",deposit)
print("Withdrew: Rs.",amount2)
print("Amount after withdrawal: Rs.",withdraw)