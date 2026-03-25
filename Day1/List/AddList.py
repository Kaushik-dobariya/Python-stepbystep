#Append list
append_list_new = ["apple", "banana", "cherry"]
print("Before append:", append_list_new)
append_list_new.append("orange")
print("After append:", append_list_new)

#Insert list
insert_list_new = ["apple", "banana", "cherry"]
print("Before insert:", insert_list_new)    
insert_list_new.insert(1, "orange")
print("After insert:", insert_list_new) 

#Extend list
extend_list_new = ["apple", "banana", "cherry"]
print("Before extend:", extend_list_new)
new_list = ["orange", "mango", "grapes"]
extend_list_new.extend(new_list)
print("After extend:", extend_list_new)

#Add Any Iterable
add_iterable_list_new = ["apple", "banana", "cherry"]
print("Before adding any iterable:", add_iterable_list_new)
iterable_list_any = ("orange", "mango", "grapes") #tuple
add_iterable_list_new.extend(iterable_list_any)
print("After adding any iterable:", add_iterable_list_new)