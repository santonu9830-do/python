
print("Electricity Bill Calculator")
units = float(input("Enter the number of units consumed: "))

if units < 50:
    cost_per_unit = 2.60
    tax = 25
elif units < 100:
    cost_per_unit = 3.25
    tax = 35
elif units < 200:
    cost_per_unit = 5.26
    tax = 45
else:
    cost_per_unit = 8.45
    tax = 75
bill_amount = units * cost_per_unit
total_amount = bill_amount + tax



print("Units consumed: ",units)
print("Cost per unit: ",cost_per_unit)
print("Bill amount: ",bill_amount)
print("Tax: ",tax)
print("Total amount to be paid: ",total_amount)

