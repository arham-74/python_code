#String type
age= "15"

#print datatype of age
print("Age: ", age)
print("the type of age: ", type(age))
#print age+10   #error occurs because one is string and the other is integer

#Typecasting string to integer
age = int(age)
print("the datatype of age is: ", type(age))
print(age+10)