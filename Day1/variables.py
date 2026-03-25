##Declare a first name variable and assign a value to it
first_name = "Kaushik"
##Declare a last name variable and assign a value to it
last_name = "Kumar"
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
#---------------------------------------------------------------------------------------------------------
#Excercise: Level 1

#Check the data type of all your variables using type() built-in function
print(type(first_name))

#Compute the factorial of a given numbers.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
number = int(input("Enter a number to compute its factorial: "))
result = factorial(number)
print(result)


