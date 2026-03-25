list_new = ["apple", "banana", "cherry"]

#Change Item Value
print("Before change:", list_new)
list_new[1] = "blackcurrant"
print("After change:", list_new)

#Change a Range of Item Values
listnew = ["apple", "banana", "cherry","Kiwi", "Mango", "Papaya"]
print("Before change:", listnew)
print("Range of Indexes is [0:2]:", listnew[0:2])
#listnew[0:2] = ["Watermelon", "Chikoo"]
listnew[0:2] = ["Watermelon"]
print("After change:", listnew)

#Insert Items
print("Before Insert:", list_new)
#list_new.pop(1)
list_new.insert(3, "Watermelon")

print("After Insert:", list_new)

