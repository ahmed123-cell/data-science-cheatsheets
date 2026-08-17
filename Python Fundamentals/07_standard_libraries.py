# Learn Basic Modules

# import math
import math

# ceil: Returns the smallest integer greater than or equal the giving input.
print(math.ceil(4.333)) # --> 5

# floor: Returns the largest integer less than or equal the giving input.
print(math.floor(3.652)) # --> 3

# comb(n, k): Returns the number of ways to choose k items from n items without repitition and without order.
print(math.comb(10, 6)) # --> 210

# perm(n, k): Returns the number of ways to choose k item from n items without repittion and WITH order
print(math.perm(10, 6)) # --> 151200

# factorial: Returns the factorial of the number as an integer
print(math.factorial(5)) # --> 120

# gcd(*integers): Returns the greatest common divisor of the specified integer arguments.
print(math.gcd(36, 66)) # --> 6

# lcm(*integers): Returns the least common multiple of the specified integer arguments.
print(math.lcm(2, 3, 4, 6)) # --> 12

# sqrt(x): Takes the square root of x 
print(math.sqrt(9)) # --> 3.0

# modf(x): Returns the fractional and integer parts of x
print(math.modf(8.22)) # --> (0.22000000000000064, 8.0)

# prod(iterable): Calculates the product of all elements in the iterable
print(math.prod([10, 2, 5])) # --> 100

# cbrt(x): Returns the cube root of x
print(math.cbrt(8)) # --> 2

# exp(x): Returns the result of e power of x
print(math.exp(2)) # --> 7.38905609893065

# log(x, base): Logarithm of x to the given base (e by default)
print(math.log(8, 2)) # --> 3.0

# degrees(x): Convert angle x from radians to degrees
print(math.degrees(0.5235)) # --> 30

# radians(x): Convert angle x from degrees to radians
print(math.radians(30)) # --> 0.5235987755982988

# sin(x): Retruns the sine of x
print(math.sin(0.5235)) # --> 0.5

# cos(x): Returns the cosine of x
print(math.cos(0.5235)) # --> 0.86

# tan(x): Returns the tanget of x
print(math.tan(0.7853)) # --> 1

# asin(x): Returns the arc sine of x
print(math.asin(0.5)) # --> 0.5235 (30 in radians)

# acos(x): Returns the arc cosine of x
print(math.acos(0.86)) # --> 0.5235 (30 in radians)

# atan(x): Returns the arc tanget of x
print(math.atan(1)) # --> 0.7853 (45 in radians)

# pi
print(math.pi) # --> π = 3.141592

# e
print(math.e) # --> e = 2.718281

# inf
print(math.inf) # --> positive infinity

# nan
print(math.nan) # --> Not a number
#-----------------------------------------------------------------------------------------------------------
# Import functools
import functools

# reduce(): applies a function cumulatively to the items of an iterable, reducing it to a single value.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(functools.reduce(lambda x, y: x+y , numbers)) # --> 55
#-------------
lst_of_strings = ['a', 'b', 'c', 'd', 'e']
print(functools.reduce(lambda x, y: x + y, lst_of_strings)) # --> abcde
#-------------
lst_of_dicts = [
    {'item_id': 1, 'name': 'hiking boots', 'amount': 150.00, 'qty': 1},
    {'item_id': 33, 'name': 'hiking poles', 'amount': 95.00, 'qty': 1},
    {'item_id': 1, 'name': 'hiking pack', 'amount': 52.00, 'qty': 1},
    {'item_id': 1, 'name': 'hiking shorts', 'amount': 60.00, 'qty': 2},
]
print(functools.reduce(lambda x, y: x + y['amount'], lst_of_dicts, 0)) # --> 357.0
#_____________________________________________________________________
# lru_cache(maxsize, typed): it is a decorator stores the result of functions in the cache using (least recently used) algorithm
# which means that the least used elements deleted when the cache is full

# maxsize: the maximum number of stored elements
# typed: distinguish inputs, it is True when the inputs are different

@functools.lru_cache(maxsize=128, typed=False)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(35)) # --> 9227465
print(fibonacci.cache_info()) # --> used for giving cahce info
print(fibonacci.cache_clear()) # --> used for clear cache data
#----------------------------------------------------------------
# cache: it is a decorator stores the result of functions in the cache. It is simpler than lru_cache
# it has no maxsize, which means it stores all data without deleting or configuration. Useful for limited inputs

@functools.cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
print(factorial(10)) # --> 3,628,800
#----------------------------------------------------------------
# Cached_property: it is a decorator stores the result of property feature in the class
# Used when doing hard arthimetic process or fetching from databases
class Circle:
    def __init__(self, raduis):
        self.raduis = raduis

    @functools.cached_property
    def area(self):
        return 3.14 * self.raduis**2
circle = Circle(5)
print(circle.area) # Calculate the area --> 78.539
print(circle.area) # it is already stored in the cache without needing of calculate it --> 78.539

# another ex.
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    @functools.cached_property
    def profile(self):
        return {'name': 'john doe', 'age': 30}
user = User(1)
print(user.profile) # Fetching from database --> {'name': 'john doe', 'age': 30}
print(user.profile) # Without refetching from database --> {'name': 'john doe', 'age': 30}
#___________________________________________________________________________________________
# wraps: it is a decorator used for copying metadata from main function to wrapped function
# useful for saving the name and docs of the main function when making custom decorators
def my_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function docstring"""
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Greet someone by name"""
    print(f"Hello {name}!")

say_hello("Alice")

print(say_hello.__name__) # --> say_hello & (wrapper if not using wraps decorator)
print(say_hello.__doc__) # --> Greet someone by name & (Wrapper functon docstring if not using wraps decorator)
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# import itertools
import itertools

# count(start, step): creates an iterator that generates consecutive integers, starting from a specified number
# By default, it starts from zero and increments by one, but you can customize both the starting point and the step size.
# Both start and steps can be integers or floats
counter = itertools.count(10, 2)

for _ in range(3):
    print(next(counter)) # --> 10 \n 12 \n 14 
#-------------------------------------------------------------
# cycle(p): creates an iterator that cycles through an iterable indefinitely.
# Useful when you need to repeat a sequence of elements over and over again.
my_cycle = itertools.cycle("ABCD")

for _ in range(8):
    print(next(my_cycle)) # --> A \n B \n C \n D \n A \n B \n C \n D
#-------------------------------------------------------------
# repeat(elem., n): creates an iterator that returns the same value repeatedly.
# You can specify the number of repetitions, or if you don't, it will repeat indefinitely.
repeater = itertools.repeat(10, 3)
for value in repeater:
    print(value) # --> 10 \n 10 \n 10
#-------------------------------------------------------------
# accumulate(p): performes cumulative operations on an iterable.
# By default, it performs cumulative summation, but you can also specify a different binary function to apply cumulatively.
accumulator = itertools.accumulate([1, 2, 3, 4, 5])
for number in accumulator:
    print(number) # --> 1, 3, 6, 10, 15

# another ex for multiplication.
import operator
accumulator2 = itertools.accumulate([1, 2, 3, 4, 5], operator.mul)
for number in accumulator2:
    print(number) # --> 1, 2, 6, 24, 120
#-------------------------------------------------------------
# batched(iterable, n): Used to group elements from an iterable into fixed-size chunks or batches.
# This can be particularly useful when you need to process data in smaller, manageable pieces.
bathces = itertools.batched('ABCDEFG', n=3)
for batch in bathces:
    print(batch) # --> ('A', 'B', 'C') \n ('D', 'E', 'F') \n ('G',)
#-------------------------------------------------------------
# chain(*iterables): allows you to combine multiple iterables into a single continuous sequence.
chained = itertools.chain(['a', 'b', 'c'], ['e', 'f', 'g'])
for chain in chained:
    print(chain) # --> 'a' \n 'b' \n 'c' \n 'e' \n 'f' \n 'g'
#-------------------------------------------------------------
# chain.from_iterable(iterables within iterable): flatten a list of iterables. It takes a single iterable argument that produces iterables,
# and it returns an iterator that yields elements from the first iterable, then the second, and so on.
list_of_lists = [[1, 2, 3], ['a', 'b', 'c'], [4, 5, 6]]
flattend = itertools.chain.from_iterable(list_of_lists)
for value in flattend:
    print(value) # --> 1 \n 2 \n 3 \n 'a' \n 'b' \n 'c' \n 4 \n 5 \n 6
#-------------------------------------------------------------
# compress(iterable, selectors): Used to filter elements from an iterable based on a corresponding selector iterable.
# It returns only the elements where the corresponding selector is True (1).
filtered =itertools.compress("ABCDEF", [1,0,1,0,1,1])
for letter in filtered:
    print(letter) # --> "A" \n "C" \n "E" \n "F"
#-------------------------------------------------------------
# dropwhile(func, iterable): Used to drop elements from an iterable as long as a specified predicate is true.
# Once the predicate becomes false, it returns the remaining elements.
dropped = itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8, 9])
for value in dropped:
    print(value) # --> 5 \n 6 \n 7 \n 8 \n 9
#-------------------------------------------------------------
# filterfalse(func, iterable): Used to filter elements from an iterable based on a predicate function.
# It returns only the elements for which the predicate function returns False.
filtered = itertools.filterfalse(lambda x: x % 2 ==0, [1, 2, 3, 4, 5, 6, 7, 8, 9])
for value in filtered:
    print(value) # --> 1 \n 3 \n 5 \n 7 \n 9
#-------------------------------------------------------------
# groupby(iterable, key): Used to group consecutive elements in an iterable that have the same key value.
# It's particularly useful for grouping data that is already sorted by the key.
grouped = itertools.groupby(['A', 'B', 'CDE'], key=len)
for key, group in grouped:
    print(f"key: {key}")
    print(f"group: {list(group)}")

# another ex.
data = [('a', 1), ('a', 2), ('b', 3), ('b', 4), ('a', 5)]
grouped = itertools.groupby(data, key=lambda x: x[0])
for key, group in grouped:
    print(f"Key: {key}")
    print(f"Group: {list(group)}")
#-------------------------------------------------------------
# isslice(iterable, start, stop, step): create an iterator that returns selected elements from an iterable.
# It works similarly to slicing a list, but it can be used with any iterable, not just lists.
sliced = itertools.islice(range(10), 2, 8, 2) 
for value in sliced:
    print(value) # --> 2 \n 4 \n 6
#-------------------------------------------------------------
# pairwise(iterable): Used to create an iterator that returns consecutive overlapping pairs from an iterable
pairs = itertools.pairwise([1, 2, 3, 4, 5])
for pair in pairs:
    print(pair) # --> (1, 2) \n (2, 3) \n (3, 4) \n (4, 5)
#-------------------------------------------------------------
# starmap(iterable): Used to apply a function to the elements of an iterable, where the elements are expected to be tuples.
# It is similar to the built-in map function, but it unpacks the arguments from the tuples before applying the function.
data = [(2, 5), (3, 2), (10, 3)]
result = itertools.starmap(pow, data)
for value in result:
    print(value) # --> 32 \n 9 \n 1000
#-------------------------------------------------------------
# takewhile(func, iterable): used to return elements from an iterable as long as a specified predicate is true.
# Once the predicate becomes false, it stops and returns no more elements.
taken = itertools.takewhile(lambda x: x< 5, [1, 4, 6, 3, 8])
for value in taken:
    print(value) # --> 1 \n 4
#-------------------------------------------------------------
# zip_longest(*iterables, fillvalue): Used to combine multiple iterables into a single iterator, similar to the built-in zip function.
# However, zip_longest continues until the longest iterable is exhausted, filling in missing values with a specified fill value (default is None).
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c', 'd', 'e']
combined = itertools.zip_longest(lst1, lst2, fillvalue="unknown")
for value in combined:
    print(value) # --> (1, a) \n (2, b) \n (3, c) \n (unknown, d) \n (unknown, e)
#-------------------------------------------------------------
# product(*iterables, repeat): used to compute the Cartesian product of input iterables.
# It returns an iterator that yields tuples representing all possible combinations of elements from the input iterables.
cartesian_product= itertools.product(['a', 'b'], [1, 2])
print(list(cartesian_product)) # --> [('a', 1), ('a', 2), ('b', 1), ('b', 2)]

# another ex.
cartesian_product = itertools.product([1, 2, 3], repeat=2)
for value in cartesian_product:
    print(value) # --> (1, 1)-(1, 2)-(1, 3)-(2, 1)-(2, 2)-(2, 3)-(3, 1)-(3, 2)-(3, 3)
#-------------------------------------------------------------
# permutations(iterable, length): used to generate all possible permutations (orderings) of elements in an iterable.
# You can specify the length of the permutations, and if not specified, it defaults to the length of the input iterable.
perms = itertools.permutations([1, 2, 3])
for perm in perms:
    print(perm) # --> (1, 2, 3)-(1, 3, 2)-(2, 1, 3)-(2, 3, 1)-(3, 1, 2)-(3, 2, 1)

# another ex.
perms = itertools.permutations([1, 2, 3], 2)
for perm in perms:
    print(perm) # --> (1, 2)-(1, 3)-(2, 1)-(2, 3)-(3, 1)-(3, 2)
#-------------------------------------------------------------
# combinations(iterable, length): used to generate all possible combinations of a specified length from an iterable.
# Unlike permutations, combinations do not consider the order of elements, and each combination is unique.
combs = itertools.combinations([1, 2, 3, 4], 2)
for comb in combs:
    print(comb) # --> (1, 2)-(1, 3)-(1, 4)-(2, 3)-(2, 4)-(3, 4)
#-------------------------------------------------------------
# combinations_with_replacement(iterable, length): used to generate all possible combinations of a specified length from an iterable,
# allowing individual elements to be repeated. This is different from the combinations function, which does not allow repeated elements.
combs_with_replacement= itertools.combinations_with_replacement([1, 2, 3], 2)
for comb in combs_with_replacement:
    print(comb) # --> (1, 1)-(1, 2)-(1, 3)-(2, 2)-(2, 3)-(3, 3)
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# import collcetions
import collections

# deque(iterable): supports thread-safe, memory-efficient appends and pops from either side of the deque
# with approximately the same O(1) performance in either direction.
my_deque = collections.deque([1, 2, 3, 4, 5])
my_deque.append(6) # --> [1, 2, 3, 4, 5, 6]
my_deque.appendleft(0) # --> [0, 1, 2, 3, 4, 5, 6]

my_deque.pop() # --> [0, 1, 2, 3, 4, 5]
my_deque.popleft() # --> [1, 2, 3, 4, 5]

print(my_deque) # --> [1, 2, 3, 4, 5] (the final result)
#-------------------------------------------------------------
# ChainMap(*dicts): allows you to group multiple dictionaries (or other mappings) together to create a single, updateable view.
# This can be useful when you want to work with multiple contexts or scopes, such as combining global and local variables.
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "c": 3}
chain = collections.ChainMap(dict1, dict2)

# show the values
print(chain['a']) # --> 1
print(chain['b']) # --> 2
print(chain['c']) # --> 3

# update a value
chain['a'] = 10
print(dict1['a']) # --> 10

# add new key
chain['d'] = 5
print(dict1['d']) # --> 5
#-------------------------------------------------------------
# Counter(): a dictionary where the keys are the elements and the values are their counts.
# It provides several useful methods for working with counts, such as finding the most common elements or updating counts from another iterable.
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_counter = collections.Counter(fruits)

# show the values
print(fruit_counter['apple']) # --> 3
print(fruit_counter['banana']) # --> 2
print(fruit_counter['orange']) # --> 1

# find the most common elements
print(fruit_counter.most_common(1)) # --> [('apple', 3)]
print(fruit_counter.most_common(2)) # --> [('apple', 3), ('banana', 2)]

# update counts from another iterable
more_fruits = ['banana', 'orange', 'orange']
fruit_counter.update(more_fruits)
print(fruit_counter) # --> Counter({'apple': 3, 'banana': 3, 'orange': 3})
#-------------------------------------------------------------
# OrderedDict: remembers the order in which items were inserted. This can be useful when you need to maintain the order of elements for tasks
# like sorting, reordering, or simply preserving the sequence of operations.

# create an ordered dict
ordered_dict = collections.OrderedDict()

# add items to the ordered dict
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# access items
print(ordered_dict) # --> OrderedDict({'a': 1, 'b': 2, 'c': 3})

# move an item to the end
ordered_dict.move_to_end('a')
print(ordered_dict) # --> OrderedDict({'b': 2, 'c': 3, 'a': 1})

# move an item to the beginning
ordered_dict.move_to_end('a', last=False)
print(ordered_dict) # --> OrderedDict({'a': 1, 'b': 2, 'c': 3})
#-------------------------------------------------------------
# defaultdict(type): works just like a regular dictionary, but it takes a default factory function as an argument.
# This factory function is called to provide a default value when a key is accessed that does not exist in the dictionary.
default_dict = collections.defaultdict(int)
print(default_dict['a']) # --> 0

default_dict['a'] += 1
default_dict['b'] += 2

print(default_dict) # --> defaultdict(<class 'int'>, {'a': 1, 'b': 2})
#---------------
# another ex.
my_defualt_dict = collections.defaultdict(str)
print(my_defualt_dict['x']) # --> ""

my_defualt_dict['x'] += 'Hello'
my_defualt_dict['y'] += 'World'

print(my_defualt_dict) # --> defaultdict(<class 'str'>, {'x': 'Hello', 'y': 'World'})
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# import datetime and pytz
from datetime import date, time, datetime, timedelta
import pytz

# date functions
today = date.today()
print(today)

my_date = date(2024, 5, 15)
print(my_date)
print(my_date.year, my_date.month, my_date.day)
print(my_date.weekday())
print(my_date.isoformat()) # --> returns the date to YYYY-MM-DD format
#-----------------------------------------------
# time functions
my_time = time(14, 30, 45)
print(my_time)
print(my_time.hour, my_time.minute, my_time.second)
#-----------------------------------------------
# datetime functions
now = datetime.now()
print(now)

my_datetime = datetime(2023, 5, 15, 14, 30)
print(my_datetime)

date_string = '2023-05-15 14:30'
parsed_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M')
print(parsed_date)

print(now.strftime('%Y/%m/%d %H:%M:%S'))
"""
%Y: year with century -- %y: year withour century
%m: month as a number -- %B: full month name -- %b: abbreviated month name
%d: day as a number -- %A: full day name -- %a: abbreviated day name
%H: 24-clock -- %I: 12-clock -- %p: AM or PM
%M: minute
%S: second
"""
#------------------------------------------
# timedelta and difference between dates
delta = timedelta(days=5, hours=3, minutes=30)
print(delta)

future_delta = now + delta
print(future_delta)

date1 = datetime(2023, 5, 15)
date2 = datetime(2023, 5, 10)

difference = date1 - date2
print(difference)
print(difference.days, difference.seconds)

# calculate the duration
start = datetime(2023, 5, 1, 10, 0)
end = datetime(2023, 5, 1, 12, 30)
diff = end - start
print(f"Duration: {diff.total_seconds() / 3600} hours")
print(diff)
#------------------------------------------
# the time by area zone
now = datetime.now(pytz.UTC)
print(now) # --> the time UTC

egypt_tz = pytz.timezone('Africa/Cairo')
now_egypt = now.astimezone(egypt_tz)
print(now_egypt)
#---------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
# import os
import os

# files and folders management
# NOTE: ALL PATHS HERE IS NOT REAL

print(os.listdir(r"E:\MySQL")) # --> Returns the list of files and folders in this path
print(os.listdir(".")) # --> Returns the list of files and folders in the current path

os.mkdir(r"E:\hello world") # --> creates a new folder
os.rmdir(r"E:\hello world") # --> removes an empty folder
os.remove(r"E:\hello world\file.txt") # --> remvoes the file
os.rename(r"E:\Safe Exam bro", r"E:\SafeExamBrowser") # Rename the file or the folder

# dealing with paths
path = os.path.join(r'E:\\', r'Data Science', r'example files', r'sakila-db')
print(path) # --> joins the pathes in line with the operating system

print(os.path.exists(r"E:\Data Science\example files\sakila-db")) # --> check if the path exists
print(os.path.isfile(r'E:\Data Science\example files\Sample Data\insurance.csv')) # --> check if path refers to a file
print(os.path.isdir(r'E:\Data Science\example files\Sample Data')) # --> check if path refers to a folder

print(os.path.basename(r'E:\Data Science\example files\Sample Data\insurance.csv')) # --> return the file or the folder from the path
print(os.path.dirname(r'E:\Data Science\example files\Sample Data\insurance.csv')) # --> returns the path without the file or the folder

print(os.getcwd()) # --> get the current working dircotory
os.chdir(r"E:\Data Science\SQL") # change the working directory
#--------------------------------------------------------------------------------------------------------
from pathlib import Path

path = Path("data") / "file.csv" 
print(path) # --> data/file.csv

print(path.exists()) # does file exists?
print(path.name)     # the name of the file
print(path.stem)     # file
print(path.suffix)   # .csv
print(path.parent)   # data

# Make Folders
folder = Path("data")
folder.mkdir(exist_ok=True)

# Read and write Files
file = path("Files/example.txt")
file.write_text("Hello Ahmed")

text = file.read_text()
print(text)

#---------------------------------------------------------------------------------------------------------------
# Virtual Enviroment

# python -m venv [name]: creates a virtual enviroment
# [name]\Scripts\activate: activate the virtual eniroment
# deactivate: deactivate it
# pip freeze > requirements.txt: shows all packages and their versions and save it into requrements.txt
# pip install -r requirments.txt: install all packages in requirements.txt