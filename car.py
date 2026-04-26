brand = str(input("Enter car brand:"))
model = str(input("Enter car model:"))
year = int(input("Enter manufactured year of car:"))
price = float(input("Enter total price of car:"))
warrenty = int(input("Enter warrenty of car:"))
car_type = input("Is the car electric? (yes/no):")

print("---Car Information---")
print("Brand of car: ",brand)
print("Model of car: ",model)
print("Manufactured Year of car:",year)
print("Total Price of car: Rs.",price)
print("warrenty of car:",warrenty,"years")
is_electric = car_type == "yes"
if is_electric:
    print("Type:Electrical car")
else:
    print("Type:Fuel-based car")