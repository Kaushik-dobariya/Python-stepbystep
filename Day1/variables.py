
#---------------------------------------------------------------------------------------------------------
#Excercise: Level 1



#Compute the factorial of a given numbers.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
number = 6 #int(input("Enter a number to compute its factorial: "))
result = factorial(number)
print(result)

#dict() function can be used to create a dictionary. A dictionary is a collection of key-value pairs. Each key is unique and maps to a value. The dict() function can take an iterable of key-value pairs or keyword arguments to create a dictionary.
a=2 #int(input("Enter a number: "))
d=dict()
for i in range(1,a+1):
    d[i]=i*i
print(d)


values=input()
l=values.split(",")
m=tuple(l)
print(l)
print(m)


