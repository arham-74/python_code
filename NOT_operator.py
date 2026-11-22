#NOT operator

raining = input("Is it raining? Yes/No: ")

if raining == "Yes":
    raining = True
else:
    raining = False

if raining:
    print("Wear a raincoat")
if not raining:
    print("You don't need a raincoat")