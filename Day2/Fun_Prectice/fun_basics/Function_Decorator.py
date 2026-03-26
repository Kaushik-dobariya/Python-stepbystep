#Basic Decorator
def decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper
@decorator
def say_hello():
    print("Hello, World!")  
say_hello()

# Decorator with arguments
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper  
@decorator
def greet(name):
    print(f"Hello, {name}!")    
greet("Alice")

# Decorator with return value
def decorator(func):    
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper
@decorator
def add(a, b):
    return a + b
result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")   

# Decorator with class
class Decorator:
    def __init__(self, func):                            # The __init__ method is the constructor of the Decorator class. It takes a function as an argument and assigns it to the instance variable self.func. This allows the decorator to store a reference to the original function that it will wrap.
        self.func = func                                 # The __call__ method is defined to make the instance of the Decorator class callable. When the decorated function is called, it will execute the code inside the __call__ method. It prints a message before and after calling the original function (self.func) and returns the result of the original function.
    def __call__(self, *args, **kwargs):                 # The __call__ method allows the instance of the Decorator class to be called as if it were a function. It takes any number of positional and keyword arguments, which are passed to the original function (self.func) when it is called. The method also prints messages before and after calling the original function, and returns the result of the original function. This allows the decorator to modify or enhance the behavior of the original function while still preserving its functionality.
        print("Before the function is called.")
        result = self.func(*args, **kwargs)              # The line result = self.func(*args, **kwargs) calls the original function (self.func) with the provided arguments (*args and **kwargs) and stores the return value in the variable result. This allows the decorator to capture the output of the original function, which can then be returned or modified as needed. In this case, the decorator simply returns the result without modification, but it could be enhanced to perform additional processing on the result if desired.
        print("After the function is called.")
        return result   
@Decorator
def say_goodbye():                                       # The say_goodbye function is defined and decorated with the Decorator class. When this function is called, it will execute the code inside the __call__ method of the Decorator class, which will
    print("Goodbye, World!")
say_goodbye()


# Decorator with functools.wraps
import functools
def decorator(func):    
    @functools.wraps(func)                            # The @functools.wraps(func) decorator is used to preserve the metadata of the original function (func) when it is wrapped by the decorator. This means that attributes like __name__, __doc__, and others of the original function will be retained in the wrapper function, allowing for better debugging and introspection.
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper
@decorator
def greet(name):
    """This function greets the person with the given name."""  # This is a docstring that provides a description of the greet function. It explains that the function takes a name as an argument and returns a greeting message. The @functools.wraps(func) decorator ensures that this docstring, along with other metadata of the original function, is preserved in the wrapper function created by the decorator.
    print(f"Hello, {name}!")    
greet("Bob")
print(greet.__name__)  # This will print the name of the original function, which is "greet", instead of the wrapper function's name, which would be "wrapper" if @functools.wraps(func) was not used.
print(greet.__doc__)   # This will print the docstring of the original function, which is "This function greets the person with the given name.", instead of None or the docstring of the wrapper function if @functools.wraps(func) was not used.      


