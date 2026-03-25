#Remove Specified Item
list_new = ["apple", "banana", "cherry"]
print("Before remove:", list_new)
list_new.remove("banana")
print("After remove:", list_new)    

#Remove Specified Index
index_remove_list_new = ["apple", "banana", "cherry"]
print("Before pop:", index_remove_list_new)
index_remove_list_new.pop(1)
print("After pop:", index_remove_list_new)  

#Remove Specified Index - last item
last_index_remove_list_new = ["apple", "banana", "cherry"]
print("Before pop:", last_index_remove_list_new)
last_index_remove_list_new.pop()    
print("After pop:", last_index_remove_list_new)

#Remove Specified Index - return removed item
return_removed_item_list_new = ["apple", "banana", "cherry"]
print("Before pop:", return_removed_item_list_new)
removed_item = return_removed_item_list_new.pop(1)  
print("After pop:", return_removed_item_list_new)
print("Removed item:", removed_item)    

#The del keyword also removes the specified index:
del_list_new = ["apple", "banana", "cherry"]
print("Before del:", del_list_new)
del_list_item = del_list_new[1]
del del_list_new[1]
print("After del:", del_list_new)
print("Deleted item:", del_list_item)

#Clear the list
clear_list_new = ["apple", "banana", "cherry"]  
print("Before clear:", clear_list_new)
clear_list_new.clear()
print("After clear:", clear_list_new)
