#1. Function with Arguments
def greet(name):
    return f"Hello, {name}! Welcome to Python programming!"
message = greet("Alice")
print(message)


#2. Function with parameters
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is: {result}")

#3. Function with default parameters
def greet(name="Guest"):
    return f"Hello, {name}! Welcome to Python programming!" 
message = greet()  # Using default parameter
print(message)

#4. Function with keyword arguments
message = greet(name="Bob")  # Using keyword argument
print(message)

#5. parameter Vs Argument
def greet(name):  # 'name' is a parameter
    return f"Hello, {name}! Welcome to Python programming!"
message = greet("Charlie")  # "Charlie" is an argument
print(message)

#6. Function with multiple parameters
def calculate_area(length, width):
    return length * width

area = calculate_area(10, 5)
print(f"The area of the rectangle is: {area}")  

#7. Function with variable number of arguments
def sum_numbers(*args):
    return sum(args)
total = sum_numbers(1, 2, 3, 4, 5)
print(f"The sum of the numbers is: {total}")    

#8. Function with keyword-only arguments
def greet(name, *, greeting="Hello"):
    return f"{greeting}, {name}! Welcome to Python programming!"
message = greet("Dave", greeting="Hi")  # Using keyword-only argument
print(message)

#function with variable keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
print_info(name="Eve", age=30, city="New York")  # Using variable keyword arguments

#9. Function with positional-only parameters (Python 3.8+)
def greet(name, /):
    return f"Hello, {name}! Welcome to Python programming!" 
message = greet("Frank")  # Positional argument
print(message)

#10. Function with keyword-only parameters (Python 3.8+)
def greet(*, name):
    return f"Hello, {name}! Welcome to Python programming!" 
message = greet(name="Grace")  # Keyword argument
print(message)

#11. Function with type hints
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Python programming!"
message = greet("Kumar")
print(message)  

#12. Function with variable positional and keyword arguments
def print_details(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
print_details("Alice", "Bob", name="Charlie", age=25)                                                   # Using variable positional and keyword arguments

#13. Function with lambda (anonymous function)
square = lambda x: x * x                                                                                # This is a lambda function that takes one argument and returns its square.
result = square(10)                                                                                     # Calling the lambda function with an argument  
print(f"The square of 10 is: {result}")

#14. Function with nested functions
def outer_function(name):
    def inner_function():
        return f"Hello, {name}! Welcome to Python programming!"
    return inner_function()                                                                             # Calling the inner function and returning its result
message = outer_function("Test")                                                                        # Calling the outer function with an argument 
print(message)

#15. Function with recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)                                                                     # Recursive call to calculate factorial
result = factorial(5)                                                                                   # Calling the factorial function with an argument
print(f"The factorial of 5 is: {result}")   

#16. Function with variable scope
def outer():
    x = "Hello"                                                                                         # This variable is in the outer function's scope
    def inner():
        print(x)                                                                                        # The inner function can access the variable 'x' from the outer function's scope
    inner()                                                                                             # Calling the inner function
outer() 

#17. Function with global variable
x = "Hello Global"                                                                                             # This variable is in the global scope      
def greet():
    global x                                                                                             # Declaring 'x' as a global variable to modify it inside the function
    x = "Hi global in inner"                                                                                              # Modifying the global variable 'x'
    print(x)                                                                                             # Printing the modified value of 'x'
greet()                                                                                                 # Calling the greet function to see the effect of modifying the global variable
print(x)                                                                                                 # Printing the global variable 'x' after modification by the greet function    