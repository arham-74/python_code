units = int(input("Number of units consumed: "))

if units <= 50:
    amount = units*2.6
    tax = 25

elif units>50 and units <=100:
    amount = (50*2.6)+((units-50)*3.25)
    tax = 35

else:
    amount = (50*2.6)+(50*3.25)+(units-100)*8.425
    tax = 45

total = amount + tax
print("Your bill is: ₹", total)