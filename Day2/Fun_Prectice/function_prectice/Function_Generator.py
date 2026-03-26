#For large datasets, generators save memory:
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1  
counter = count_up_to(100)
#for number in counter:
#print(number)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
    
#Generators can be used to create infinite sequences:
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1    
infinite_gen = infinite_sequence()
print(next(infinite_gen))

#List comprehension vs generator expression:
squared_list = [x ** 2 for x in range(10)]  # List comprehension creates a list of squared numbers from 0 to 9
squared_gen = (x ** 2 for x in range(10))   # Generator expression creates a generator that produces squared numbers from 0 to 9 on demand
print(squared_list)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(next(squared_gen))  # Output: 0   
print(next(squared_gen))  # Output: 1
print(next(squared_gen))  # Output: 4   

#Generator with multiple yields:
def multi_yield():
    yield "First yield"
    yield "Second yield"
    yield "Third yield" 
multi_gen = multi_yield()
print(next(multi_gen))  # Output: "First yield" 
print(next(multi_gen))  # Output: "Second yield"
print(next(multi_gen))  # Output: "Third yield"

#Generator to read a file line by line:
def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()                                      # Yield each line without leading/trailing whitespace       

for line in read_file_line_by_line('D:\Documents\savevideo.txt'):
    print(line)