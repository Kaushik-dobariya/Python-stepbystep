# Identifying base case and recursive case:
def factorial(n):
    if n == 0:                                  # Base case: factorial of 0 is 1
        return 1
    else:                                       # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)
print("factorial: ",factorial(5))               # Output: 120

# Fibonacci sequence using recursion:
def fibonacci(n):
    if n <= 0:                                  # Base case: Fibonacci of 0 is 0
        return 0
    elif n == 1:                                # Base case: Fibonacci of 1 is 1
        return 1
    else:                                       # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)
print("fibonacci: ",fibonacci(5))               # Output: 5

# Recursive function to calculate the sum of a list:
def sum_list(lst):
    if not lst:                                 # Base case: empty list has a sum of 0
        return 0
    else:                                       # Recursive case: sum of list is first element + sum of the rest of the list
        return lst[0] + sum_list(lst[1:])
print("sum_list: ",sum_list([1, 2, 3, 4, 5]))   # Output: 15

# Recursive function to reverse a string:
def reverse_string(s):
    if s == "":                                 # Base case: empty string is its own reverse
        return s
    else:                                       # Recursive case: reverse of string is last character + reverse of the rest of the string
        return s[-1] + reverse_string(s[:-1])
print("reverse_string: ",reverse_string("hello")) # Output: "olleh"

# Recursive function to find the greatest common divisor (GCD) using Euclid's algorithm:
def gcd(a, b):
    if b == 0:                                  # Base case: GCD of a and 0 is a
        return a
    else:                                       # Recursive case: GCD of a and b is GCD of b and the remainder of a divided by b
        return gcd(b, a % b)
print("gcd: ",gcd(12, 8))                        # Output: 4

#Euclid's algorithm formula: gcd(a, b) = gcd(b, a % b) where a >= b and b > 0. The algorithm continues until b becomes 0, at which point the GCD is the value of a. 
# This method is efficient for finding the GCD of two numbers.

# Recursive function to calculate the power of a number:
def power(base, exponent):
    if exponent == 0:                           # Base case: any number to the power of 0 is 1
        return 1
    else:                                       # Recursive case: base^exponent = base * base^(exponent - 1)
        return base * power(base, exponent - 1)
print("power: ",power(2, 3))                      # Output: 8

# check if a number is prime using recursion:
def is_prime(n, divisor=2):
    if n <= 1:                                   # Base case: numbers less than or equal to 1 are not prime
        return False
    if divisor >= n:                             # Base case: if divisor is greater than or equal to n, n is prime
        return True
    if n % divisor == 0:                         # Recursive case: if n is divisible by divisor, n is not prime
        return False
    return is_prime(n, divisor + 1)              # Recursive case: check the next divisor
print("is_prime: ",is_prime(11))                 # Output: True

# check if a number is a palindrome using recursion:
def is_palindrome(s):
    if len(s) <= 1:                            # Base case: a string of length 0 or 1 is a palindrome
        return True
    if s[0] != s[-1]:                          # Recursive case: if the first and last characters are not the same, it's not a palindrome
        return False
    return is_palindrome(s[1:-1])              # Recursive case: check the substring that excludes the first and last characters
print("is_palindrome: ",is_palindrome("racecar"))  # Output: True

# Check the recursion limit:
import sys
print("Recursion limit: ",sys.getrecursionlimit())  # Output: 1000 (default recursion limit in Python)

# sys.setrecursionlimit(2000)                  # Set a new recursion limit (use with caution, as it can lead to crashes if set too high)