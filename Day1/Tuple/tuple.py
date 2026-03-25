#Tuples are used to store multiple items in a single variable.
#Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print("Created Tuple: ",thistuple)

#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:   
thistuple = ("apple", "banana", "cherry")
print("Second item in the tuple: ",thistuple[1])

#Negative Indexing
#Negative indexing means start from the end 
thistuple = ("apple", "banana", "cherry")
print("Last item in the tuple: ",thistuple[-1])

#Tuples are ordered, meaning that the items have a defined order, and that order will not change.
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a tuple, the new items will be placed 
# at the end of the tuple, and the order of the existing items will not change.


#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#But we can convert the tuple into a list, change the list, and convert it back into a tuple.
#Convert the tuple into a list to be able to change it: 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple) 
y[1] = "kiwi"
thistuple = tuple(y)
print("Changed Tuple: ",thistuple)

#Allow Duplicates
#Since tuples are indexed, they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("Tuple with duplicates: ",thistuple)

#Tuple Length
print("Length of the tuple: ",len(thistuple))

#Create Tuple With One Item
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)  
print("Tuple with one item: ",thistuple)


#The tuple() Constructor
#It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry"))
print("Tuple created with constructor: ",thistuple) 

#Note: The tuple() constructor can be used to convert other data types into a tuple, for example:
#Convert a list into a tuple:
mylist = ["apple", "banana", "cherry"]
thistuple = tuple(mylist)
print("Tuple converted from list: ",thistuple)

#Convert a string into a tuple:
mystr = "Hello" 
thistuple = tuple(mystr)
print("Tuple converted from string: ",thistuple)

#Convert a set into a tuple:
myset = {"apple", "banana", "cherry"}   
thistuple = tuple(myset)
print("Tuple converted from set: ",thistuple)

#Convert a dictionary into a tuple:
mydict = {"name": "John", "age": 36, "country": "Norway"}
thistuple = tuple(mydict)   
print("Tuple converted from dictionary: ",thistuple)
#Note: When you convert a dictionary into a tuple, it will only convert the keys, not the values.


#The tuple() constructor can also be used to create an empty tuple:
thistuple = tuple()
print("Empty Tuple: ",thistuple)

#Note: The tuple() constructor can be used to create a tuple from an iterable object, such as a list, string, or set. An iterable is any Python object capable of returning 
# its members one at a time, allowing it to be iterated over in a for-loop.

#The tuple() constructor can also be used to create a tuple from a range of numbers:
thistuple = tuple(range(5))
print("Tuple created from range: ",thistuple)

#Reverse a Tuple
#You can reverse a tuple by using the reversed() function, which returns an iterator that accesses
# the given sequence in the reverse order. You can then convert the iterator into a tuple using the tuple() constructor.
thistuple = ("apple", "banana", "cherry")
reversed_tuple = tuple(reversed(thistuple))
print("Reversed Tuple: ",reversed_tuple)

#remove() method is not available for tuples because they are immutable, meaning that we cannot change, add or remove items after the tuple has been created.

#The del keyword can be used to delete the tuple completely:
thistuple1 = ("apple", "banana", "cherry")   
#del thistuple1
#print("Tuple after deletion: ",thistuple1) #This will raise an error because the tuple has been deleted.

#Note: You cannot delete items in a tuple, but you can delete the tuple completely using the del keyword.
#If you try to delete an item in a tuple, you will get an error because tuples are immutable and do not support item deletion.


#The clear() method is not available for tuples because they are immutable, meaning that we cannot change, add or remove items after the tuple has been created.
#If you try to use the clear() method on a tuple, you will get an error because tuples do not support item deletion or clearing.
#Note: You cannot clear items in a tuple, but you can delete the tuple completely using the del keyword.

#The index() method is used to find the first occurrence of a specified value in a tuple and returns its index. If the specified value is not found, it raises a ValueError.
thistuple = ("apple", "banana", "cherry")
print("Index of 'banana': ",thistuple.index("banana"))

#The count() method is used to count the number of times a specified value appears in a tuple.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print("Count of 'apple': ",thistuple.count("apple"))
#Note: The index() and count() methods are available for tuples because they do not modify the tuple, but rather return information about the tuple.


#The len() function is used to get the number of items in a tuple.
thistuple = ("apple", "banana", "cherry")   
print("Length of the tuple: ",len(thistuple))

#The sorted() function is used to sort the items in a tuple in ascending order and returns a new sorted list. The original tuple remains unchanged.
thistuple = ("banana", "apple", "cherry")
sorted_tuple = sorted(thistuple)
print("Sorted Tuple: ",sorted_tuple)

#Note: The sorted() function can be used to sort the items in a tuple, but it returns a new sorted list, not a tuple. If you want to convert 
# the sorted list back into a tuple, you can use the tuple() constructor:
thistuple = ("banana", "apple", "cherry")   
sorted_tuple = tuple(sorted(thistuple))
print("Sorted Tuple converted back to tuple: ",sorted_tuple)


#The max() function is used to find the largest item in a tuple. The items in the tuple must be of the same data type, and the data type must be comparable.
thistuple = (3, 1, 4, 2)
print("Largest item in the tuple: ",max(thistuple))
#Note: The max() function can be used to find the largest 
# item in a tuple, but it requires that all items in the tuple are of the same data type and are comparable. If the items are of 
# different data types or are not comparable, you will get a TypeError.

#The min() function is used to find the smallest item in a tuple. The items in the tuple must be of the same data type, and the data type must be comparable.
thistuple = (3, 1, 4, 2)
print("Smallest item in the tuple: ",min(thistuple))

#Note: The min() function can be used to find the smallest item in a tuple, but it requires that all items in the tuple are of the same data type and are comparable. 
# If the items are of different data types or are not comparable, you will get a TypeError.

#The sum() function is used to calculate the sum of all items in a tuple. The items in the tuple must be of the same data type, and the data type must be numeric.
thistuple = (3, 1, 4, 2)
print("Sum of all items in the tuple: ",sum(thistuple))
#Note: The sum() function can be used to calculate the sum of all items in a tuple, but it requires that all items in the tuple are of the same data type and are numeric. 
# If the items are of different data types or are not numeric, you will get a TypeError.

#The any() function is used to check if any item in a tuple is true. It returns True if at least one item in the tuple is true, and False if all items are false.
thistuple = (0, 1, 2, 3)
print("Is any item in the tuple true? ",any(thistuple))

#Note: The any() function can be used to check if any item in a tuple is true. It returns True if at least one item in the tuple is true, and False if 
# all items are false. In this example, since 1, 2, and 3 are considered true values, the any() function will return True.

#The all() function is used to check if all items in a tuple are true. It returns True if all items in the tuple are true, and False if at least one item is false.
thistuple = (1, 2, 3)
print("Are all items in the tuple true? ",all(thistuple))

#Note: The all() function can be used to check if all items in a tuple are true. It returns True if all items in the tuple are true, and False if at least one 
# item is false. In this example, since 1, 2, and 3 are considered true values, the all() function will return True. If we had a 0 in the tuple, 
# it would return False because 0 is considered a false value.

#The zip() function is used to combine two or more tuples into a single tuple of tuples. The zip() function takes multiple iterables (such as tuples) as arguments 
# and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped_tuple = tuple(zip(tuple1, tuple2))
print("Zipped Tuple: ",zipped_tuple)
#Note: The zip() function can be used to combine two or more tuples into a single tuple of tuples. In this example, the zip() function combines the elements of tuple1 and 
# tuple2 into a new tuple of tuples, where each inner tuple contains one element from each of the original tuples. 
# The resulting zipped_tuple will be ((1, 'a'), (2, 'b'), (3, 'c')).

#The enumerate() function is used to add a counter to an iterable (such as a tuple) and returns it as an enumerate object. 
# The enumerate() function takes an iterable as an argument and returns an iterator that produces pairs of index and value for each item in the iterable.
thistuple = ('apple', 'banana', 'cherry')
enumerated_tuple = tuple(enumerate(thistuple))
print("Enumerated Tuple: ",enumerated_tuple)
#Note: The enumerate() function can be used to add a counter to an iterable (such as a tuple) and returns it as an enumerate object. 
# In this example, the enumerate() function takes the thistuple and returns an iterator that produces pairs of index and value for each item in the tuple. 
# The resulting enumerated_tuple will be ((0, 'apple'), (1, 'banana'), (2, 'cherry')).

#The map() function is used to apply a specified function to each item in an iterable (such as a tuple) and returns a map object. 
# The map() function takes a function and an iterable as arguments and applies the function to each item in the iterable.
def square(x):
    return x * x
thistuple = (1, 2, 3, 4)
squared_tuple = tuple(map(square, thistuple))
print("Squared Tuple: ",squared_tuple)
#Note: The map() function can be used to apply a specified function to each item in an iterable (such as a tuple) and returns a map object. 
# In this example, the map() function takes the square function and applies it to each item in the thistuple. The resulting squared_tuple will be (1, 4, 9, 16).

#The filter() function is used to filter items in an iterable (such as a tuple) based on a specified function and returns a filter object. 
# The filter() function takes a function and an iterable as arguments and returns an iterator that produces items from the iterable for which the function returns true.
def is_even(x):
    return x % 2 == 0
thistuple = (1, 2, 3, 4, 5, 6)
even_tuple = tuple(filter(is_even, thistuple))
print("Even Tuple: ",even_tuple)
#Note: The filter() function can be used to filter items in an iterable (such as a tuple) based on a specified function and returns a filter object. 
# In this example, the filter() function takes the is_even function and applies it to each item in the thistuple. The resulting even_tuple will be (2, 4, 6) 
# because those are the items for which the is_even function returns true.

#The reduce() function is used to apply a specified function cumulatively to the items of an iterable (such as a tuple) from left to right, 
# reducing the iterable to a single value.
from functools import reduce
def add(x, y):
    return x + y
thistuple = (1, 2, 3, 4)
sum_of_tuple = reduce(add, thistuple)
print("Sum of Tuple using reduce: ",sum_of_tuple)
#Note: The reduce() function can be used to apply a specified function cumulatively to the items of an iterable (such as a tuple) from left to right, 
# reducing the iterable to a single value. In this example, the reduce() function takes the add function and applies it cumulatively to the items in the thistuple. 
# The resulting sum_of_tuple will be 10, which is the sum of all the items in the tuple (1 + 2 + 3 + 4).

#The lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# The lambda function is often used in conjunction with functions like map(), filter(), and reduce() to create small, one-time-use functions.
thistuple = (1, 2, 3, 4)    
squared_tuple = tuple(map(lambda x: x * x, thistuple))
print("Squared Tuple using lambda: ",squared_tuple)
#Note: The lambda function can be used to create small anonymous functions that can be used in conjunction with functions like map(), filter(), and reduce().
# In this example, the lambda function takes an argument x and returns x * x, which is the square of x. The map() function applies this lambda function to each item in 
# the thistuple, resulting in a new tuple of squared values (1, 4, 9, 16).  

#The zip() function can also be used to unzip a tuple of tuples back into individual tuples.
zipped_tuple = ((1, 'a'), (2, 'b'), (3, 'c'))
unzipped_tuple1, unzipped_tuple2 = zip(*zipped_tuple)
print("Unzipped Tuple 1: ",unzipped_tuple1)
print("Unzipped Tuple 2: ",unzipped_tuple2)
#Note: The zip() function can be used to unzip a tuple of tuples back into individual tuples. In this example, the zip() function takes the zipped_tuple and unzips it 
# into two separate tuples, unzipped_tuple1 and unzipped_tuple2. The resulting unzipped_tuple1 will be (1, 2, 3) and unzipped_tuple2 will be ('a', 'b', 'c').  

#The enumerate() function can also be used to create a dictionary from a tuple by using the index as the key and the value as the value in the dictionary.
thistuple = ('apple', 'banana', 'cherry')
enumerated_dict = dict(enumerate(thistuple))
print("Enumerated Dictionary: ",enumerated_dict)
#Note: The enumerate() function can be used to create a dictionary from a tuple by using the index as the key and the value as the value in the dictionary.
# In this example, the enumerate() function takes the thistuple and returns an iterator that produces pairs of index and value for each item in the tuple. 
# The dict() constructor then takes these pairs and creates a dictionary where the keys are the indices (0, 1, 2) and the values are the corresponding 
# items from the tuple ('apple', 'banana', 'cherry'). The resulting enumerated_dict will be {0: 'apple', 1: 'banana', 2: 'cherry'}.

#The map() function can also be used to create a dictionary from two tuples by using one tuple for the keys and another tuple for the values.
keys = ('name', 'age', 'country')
values = ('John', 36, 'Norway')
mapped_dict = dict(zip(keys, values))
print("Mapped Dictionary: ",mapped_dict)
#Note: The map() function can be used to create a dictionary from two tuples by using one tuple for the keys and another tuple for the values.
# In this example, the zip() function takes the keys and values tuples and combines them into a tuple of tuples, where each inner tuple contains one key and one value. 
# The dict() constructor then takes these pairs and creates a dictionary where the keys are 'name', 'age', and 'country', and the values are 'John', 36, and 'Norway'. 
# The resulting mapped_dict will be {'name': 'John', 'age': 36, 'country': 'Norway'}.

#The filter() function can also be used to create a new tuple that contains only the items from the original tuple that satisfy a certain condition.
thistuple = (1, 2, 3, 4, 5, 6)
filtered_tuple = tuple(filter(lambda x: x % 2 == 0, thistuple))
print("Filtered Tuple (only even numbers): ",filtered_tuple)
#Note: The filter() function can be used to create a new tuple that contains only the items from the original tuple that satisfy a certain condition.
# In this example, the filter() function takes a lambda function that checks if x is even (x % 2 == 0) and applies it to each item in the thistuple.
# The resulting filtered_tuple will be (2, 4, 6) because those are the items for which the lambda function returns true (i.e., the even numbers).

