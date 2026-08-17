# Defining a Function
def greet(name):
    print(f"Hello {name}")

greet("ahmed") # Call the function. --> Hello ahmed

# Function with return Value
def add(a, b):
    return a + b

print(add(2, 3)) # Call the function. --> 8
#-----------------------------------------------------------------------------------------------------------
# Default Parameter
def say_hello(name='Guest'):
    print(f"Hello {name}")

say_hello() # --> Hello Guest
say_hello("osama") # --> Hello osama
#-----------------------------------------------------------------------------------------------------------
# Function Packing and Unpacking of Arguments

# Arguments Packing
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # --> 6
print(add_numbers(4, 5, 6, 7))  # --> 22
#-------------------------------------------
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")
#-------------------------------------------
# Argument Unpacking
def hello(name, age):
    print(f"Hello {name}, your age is {age}")
person= ("Bob", 18)
hello(*person) # --> Hello Bob, your age is 18
#-------------------------------------------
def greeting(name, age):
    print(f"Hello, {name}! You are {age} years old.")

person = {"name": "Carol", "age": 28}
greeting(**person)  # -->  Hello, Carol! You are 28 years old.
#-----------------------------------------------------------------------------------------------------------
# Function Scope

# Local Scope
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # -->  10
print(x)  # Error: NameError: name 'x' is not defined
#-------------------------------------------
# Enclosing Scope (also known as Nonlocal Scope)
def outer_function():
    y = 20  # Enclosing variable

    def inner_function():
        print(y)  # Can access enclosing variable

    inner_function()

outer_function()  # --> 20
#-------------------------------------------
z = 30  # Global variable

def another_function():
    print(z)  # Can access global variable

another_function()  # --> 30
#-------------------------------------------
# The global Keyword
a = 100  # Global variable

def modify_global():
    global a
    a = 200

modify_global()
print(a)  # --> 200
#-------------------------------------------
# nonlocal Keyword
def outer_func():
    b = 50

    def inner_func():
        nonlocal b
        b = 60

    inner_func()
    print(b)  # --> 60

outer_func()
#-----------------------------------------------------------------------------------------------------------
# Function recursion
# EX: Delete multiple letters
def delete_letters(word):
    if len(word)== 1:
        return word

    if word[0]== word[1]:
        return delete_letters(word[1: ])

    return word[0] + delete_letters(word[1: ])
print(delete_letters("wwwwwwwwoooooooorrrrrrrllllldddd")) # --> world

# EX: Factorial
def factorial(number):
    if number == 1 or number ==0 :
        return 1
    else:
        return number * factorial(number - 1)
print(factorial(5)) # --> 120
#-----------------------------------------------------------------------------------------------------------
# Lambda Function
greet_hello= lambda name, age: f"Hello {name}!, your age is {age}."
print(greet_hello("ahmed", 18)) # --> Hello ahmed!, your age is 18.
print(type(greet_hello)) # --> Function
#-----------------------------------------------------------------------------------------------------------
# Build in Functions

# all(): return True if all elements in the iterables are True
print(all([1, 2, 3, 4])) # --> True

# any(): return True if at least one element is True
print(any([], (), '', 3)) # --> True

# bin(): converts an integer number to binary string prefixed with "Ob"
print(bin(10)) # --> Ob1010

# id(): returns the unique identifier (memory address) of an object.
var_x= 10
print(id(var_x)) # --> (identifier): A unique number representing the memory address of x

# sum(): gives an addition of the iterable
print(sum[67, 23, 12, 23]) # --> 125
print(sum([12, 23, 45], 19)) # --> 80

# round(): round a floating-point number to a specified number of decimal places. 
print(round(3.14159)) # --> 3 (If no number of decimal places is specified, it rounds the number to the nearest integer)
print(round(3.14159, 2)) # --> 3.14

# range(start, end[not included] , step):
print(list(range(0, 20, 2)))
print(list(range(10)))

# print():
print("my", "name", "is", "ahmed", sep="-") # --> my-name-is-ahmed
print('i love python ', end= "and php") # --> i love python and php

# abs(): gives an absolute value of the number
print(abs(100)) # --> 100
print(abs(-100)) # --> 100

# pow(base, exponent, modulus) modulus: optional
print(pow(2, 3)) # --> 8
print(pow(2, 3, 3)) # --> 2

# min(): gives the minimum element in the iterable
print(min([1, 2, 3, 4])) # --> 1

# max(): give the maximum element in the iterable
print(max([1, 2, 3, 4])) # --> 4

# slice(start, end[not included], step):
my_list= ["A", "B", "C", "D", "E", "F"]
print(a[slice(3)]) # --> ["A", "B", "C"]
print(a[slice(0, 5, 2)]) # --> ["A", "C", "E"]

# help(): provides the documentation of modules, functions, classes, methods, and keywords
print(help(print))

# del: delete one element or more in lists, tuples, keys in dictionaries and the variables
veggie= ["tomato", "carrot", "lettuce"]
del veggie[1]
print(veggie) # --> ["tomato", "lettuce"]

# ord(): Takes a single character and returns its corresponding ASCII
print(ord("a")) # --> 97
print(ord("A")) # --> 65

# chr(): Takes ASCII integer value and returns its character
print(chr(65)) # --> "A"
print(chr(97)) # --> "a"

# eval(): Excutes python operations inside the string
print(eval("2 + 3 * 4")) # --> 14
#-----------------------------------------------------------------------------------------------------------
