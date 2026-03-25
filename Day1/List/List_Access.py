list_new = ["apple", "banana", "cherry"]
print(list_new[0])

#Negative Indexing
print("Negetive Index is:", list_new[-1])

#Range of Indexes
print("Range of Indexes is [0:3]:", list_new[0:3])

print("Range of Indexes is [:3]:", list_new[:3])

print("Range of Indexes is [1:]:", list_new[1:])


#Check if "apple" is present in the list
if "Kiwi" in list_new:
    print("Yes")
else:    
    print("No")