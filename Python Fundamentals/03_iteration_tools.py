# map(): used to apply a given function to all the items in an input iterable (like a list, tuple, etc.)
# and return a map object (which is an iterator). This is especially useful for transforming data without using explicit loops.

def square(x):
    return x * x
numbers= [1, 2, 3, 4, 5]
squared_numbers= map(square, numbers)
print(list(squared_numbers)) # --> [1, 4, 9, 16, 25]
#----------------------------------------------------------
# map with lambda function
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)
print(list(squared_numbers))  # -->  [1, 4, 9, 16, 25]
#-----------------------------------------------------------------------------------------------------------
# filter(): used to construct an iterator from elements of an iterable (like a list, tuple, etc.) for which a function returns True

def is_even(n):
    return n % 2 ==0
numbers= [1, 2, 3, 4, 5]
even_numbers= filter(is_even, numbers)
print(list(even_numbers)) # --> [2, 4]
#----------------------------------------------------------
# filter with lamda function
numbers= [1, 2, 3, 4, 5]
even_numbers= filter(lambda n: n % 2==0, numbers)
print(list(even_numbers))  # --> [2, 4]

#-----------------------------------------------------------------------------------------------------------
# reduce(): applies a function comulatively to the items of an iterable, reducing it to a single value.

from functools import reduce
def sum_all(n1, n2):
    return n1 + n2
numbers=[1, 8, 2, 9, 100, 30]
sum_result= reduce(sum_all, numbers)
print(sum_result) # --> 150
#----------------------------------------------------------
# reduce with lambda function
numbers = [1, 2, 3, 4, 5]
multiply_result = reduce(lambda x, y: x * y, numbers)
print(multiply_result)  # Output: 120
#-----------------------------------------------------------------------------------------------------------
# enumerate(iterable, start=0): Counter

fruits= ['apple', 'banana', 'guava']
the_counter= enumerate(fruits, start=1)

for index, fruit in the_counter:
    print(f"{index}: {fruit}") # --> (1: apple), (2: banana), (3: guava)

print(type(the_counter)) # --> enumerate
#-----------------------------------------------------------------------------------------------------------
# reversed(iterable): reverse the arrange of iterables
print(reversed('ahmed')) # --> demha

for num in reversed([1, 2, 3, 4]):
    print(num) # --> 4 \n 3 \n 2 \n 1
#-----------------------------------------------------------------------------------------------------------
# Zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

combined = zip(names, ages)
print(list(combined)) # --> [('Alice', 25), ('Bob', 30), ('Charlie', 35)]