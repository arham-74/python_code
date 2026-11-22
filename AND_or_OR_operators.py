day = input("Enter the day of the week: ")
age = int(input("Enter your age: "))

weekend = False

#OR operator
if day.lower() == "saturday" or day.lower() == "sunday":
    weekend = True
    print("It's weekend! Enjoy!")

else:
    print("It's a weekday, it's time to work hard!")

#AND operator
if age >= 10 and weekend:
    print("You can access the pool! Enjoy the swim!")
else:
    print("You can't access the pool")