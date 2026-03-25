##Declare a first name variable and assign a value to it
first_name = "Kaushik Kumar"
##Declare a last name variable and assign a value to it
last_name = "Dobariya"
##Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name
##Declare a country variable and assign a value to it
country = "India"
##Declare a city variable and assign a value to it
city = "Ahmedabad"
##Declare an age variable and assign a value to it
age = 42
##Declare a year variable and assign a value to it
year = 1984
##Declare a variable is_married and assign a value to it
is_married = True
##Declare a variable is_true and assign a value to it
is_true = True
##Declare a variable is_light_on and assign a value to it
is_light_on = True
##Declare multiple variables on one line
x, y, z = 5, 10, 15

#Excercise Level
#Check the data type of all your variables using type() built-in function
print(type(first_name))
print(len(first_name))

#Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print("your first name is longer than your last name")
elif len(first_name) < len(last_name):
    print("your last name is longer than your first name")
else:
    print("your first and last names have the same length")
