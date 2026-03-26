def greet():
    return "Hello, welcome to Python programming!"                          # This will return a greeting message when the function is called.

message=greet()                                                             # This will call the greet function and execute its code
print(message)                                                              # This will print the return value of the greet function, which is None since the function does not return anything.

                                                                            #If a function doesn't have a return statement, it returns "None" by default.
                                                                            #Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:

def placeholder_function():
    pass                                                                   # This is a placeholder function that does nothing. It allows you to define a function without any code inside it.
placeholder_function()                                                     # This will call the placeholder function, which does nothing and returns None.


def greet(name):    
    return f"Hello, {name}! Welcome to Python programming!"                # This function takes a parameter 'name' and returns a personalized greeting message.

#1. Calling the function with an argument
message=greet("Alice") 
print(message) 

#2. You can also call the function with different arguments to get different greetings.
message=greet("Bob") 
print(message) 

#3. You can also use keyword arguments to call the function, which allows you to specify the parameter name explicitly.
message=greet(name="Charlie") 
print(message) 

#4. You can also use default parameter values in a function definition.
def greet(name="Guest"):    
    return f"Hello, {name}! Welcome to Python programming!"                  # This function now has a default parameter value of "Guest" for the 'name' parameter.  

#5.Calling the function without an argument will use the default value.
message=greet() 
print(message) 


