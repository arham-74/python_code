#Checking if the student has any medical issue
medical_issue = input("Did you have a medical issue? Y/N: ")

if medical_issue == "Y":
    print("Allowed")

else:
    attendance = int(input("Enter the number of days you were present: "))

    if attendance >= 75:
        print("Allowed")
    else:
        print("Not Allowed")