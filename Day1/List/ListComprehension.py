#syntex: newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

#Sortest way - With list comprehension you can do all that with only one line of code:
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print("List will contain fruits with 'a' in their name:",newlist)  

#with condition 
newlist = [x for x in fruits if x != "apple"]
print("List will contain fruits except 'apple':",newlist)

#with condition 
newlist = [x for x in fruits if x == "apple"]
print("List will contain only 'apple':",newlist)


#With no if statement
newlist = [x for x in fruits]
print("List will contain all fruits:",newlist)

#upper case
newlist = [x.upper() for x in fruits]   
print("List will contain fruits in upper case:",newlist)

#iterable without if condition
newlist = [x for x in range(10)]
print("List will contain numbers from 0 to 9:",newlist)

#iterable with if condition
newlist = [x for x in range(10) if x < 5]
print("List will contain numbers from 0 to 4:",newlist)

#set all values in the list to hello 
newlist = ["hello" for x in fruits]
print("List will contain 'hello' for each fruit:",newlist)

#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print("List will contain 'orange' instead of 'banana':",newlist)    

