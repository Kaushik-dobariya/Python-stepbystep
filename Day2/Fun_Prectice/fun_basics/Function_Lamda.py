#Add 10 to argument a, and return the result:

add_ten = lambda a: a + 10
result = add_ten(5)
print(result)  

#Multiply two arguments a and b, and return the result:
multiply = lambda a, b: a * b
result = multiply(3, 4) 
print(result)

#Check if a number is even or odd:
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(10))
print(is_even(7))

#Summarize argument a, b, and c and return the result:
summarize = lambda a, b, c: a + b + c
result = summarize(1, 2, 3)
print(result)

#Lambda Functions
def square(x):
    return lambda:x * x
square_of_5 = square(5)
print(square_of_5())  

#2
def power(n):
    return lambda x: x ** n 
square = power(2)
cube = power(3) 
print(square(4))
print(cube(2))


#Lambda with Built-in Functions
#map() function with lambda to square each element in a list:
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))                 # The map() function applies the lambda function (which squares each element) to each item in the numbers 
                                                                       # list, and the result is converted to a list using the list() constructor. 
                                                                       # The squared_numbers variable will contain the squared values of the original numbers list, 
                                                                       # which are [1, 4, 9, 16, 25]. 
print(squared_numbers)   

#filter() function with lambda to filter out even numbers from a list:
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

#sorted() function with lambda to sort a list of tuples based on the second element:
data = [(3, 'apple'), (6, 'banana'), (1, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

#sorted() function with lambda to sort a list of tuples based on the first element:
data = [(3, 'apple'), (6, 'banana'), (1, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[0])
print(sorted_data)

#reduce() function with lambda to calculate the product of all elements in a list:
nums=[10,15,1,0]
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
print(product)

#Sort strings by length:
strings = ["apple", "pineapple", "cherry", "date"]
sorted_words=sorted(strings,key=lambda x:len(x))
print(sorted_words)