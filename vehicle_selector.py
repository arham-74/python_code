#Choosing a vehicle
print("Select a ride: ")
print("1. Bike")
print("2. Car")
vehicle = input("Enter your choice: ")

if vehicle == "1":
    print("Select a type: ")
    print("1. Yamaha")
    print("2. Harley Davidson")
    type_bike = input("Enter your type: ")
    if type_bike == "1":
        print("You chose the Yamaha bike")
    if type_bike =="2":
        print("You chose the Harley Davidson bike")

if vehicle == "2":
    print("Select a type: ")
    print("1. Ferarri")
    print("2. McLaren")
    type_car = input("Enter your type: ")
    if type_car == "1":
        print("You chose the Ferarri car")
    if type_car =="2":
        print("You chose the McLaren car")