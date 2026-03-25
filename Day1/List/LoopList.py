loop_list=["apple", "banana", "cherry","mango", "papaya"]
print("loop_list:", loop_list)

#Loop through the list items by using a for loop
print("Loop through the list items by using a for loop:")
for x in loop_list:
    print(x)
    
#Loop through the list items by using a For loop with the range() and len() functions
print("Loop through the list items by using a For loop with the range() and len() functions:")
print(len(loop_list))
for i in range(len(loop_list)):
    print(str(i+1) + "." + loop_list[i]) 
    
#Loop through the list items by using a while loop
print("Loop through the list items by using a while loop:")
i = 0
while i < len(loop_list):
    print(str(i+1) + "." + loop_list[i]) 
    i = i + 1
    
#Loop through the list items by using a list comprehension - List Comprehension offers the shortest syntax for looping through lists:

print("Loop through the list items by using a list comprehension:")
[print(x) for x in loop_list]

