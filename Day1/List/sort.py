fruits_list = ["orange", "mango", "kiwi", "pineapple", "banana"]   
digit_list = [1, 5, 3, 9, 2]

fruits_list.sort()
print("Sorted list of fruits:", fruits_list)

digit_list.sort()
print("Sorted list of digits:", digit_list)

#Sort Descending
sorted_fruits_list=["orange", "mango", "kiwi", "pineapple", "banana"]
sorted_fruits_list.sort(reverse=True)
print("Sorted list of fruits in descending order:", sorted_fruits_list)

#Customize Sort Function - Sort the list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50) #decending order
#return abs(n + 50) #ascending order
new_digit_list = [1,4,5,8,3,9,2]
new_digit_list.sort(key=myfunc)
print("Sorted list of digits:", new_digit_list)

#Case Insensitive Sort - Sort the list alphabetically, but ignore if the letters are upper or lower case
case_insensitive_fruits_list = ["banana", "Orange", "Kiwi", "cherry"]
case_insensitive_fruits_list.sort(key=str.lower)    
print("Sorted list of fruits in case insensitive way:", case_insensitive_fruits_list)

#Reverse Order - Reverse the order of the list items
reverse_fruits_list = ["banana", "Orange", "Kiwi", "cherry"]
reverse_fruits_list.reverse()   
print("Reversed list of fruits:", reverse_fruits_list)
