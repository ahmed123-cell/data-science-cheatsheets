"""
Python Functions: a study reference.

Topics covered:
    defining functions, default parameters, *args / **kwargs, argument
    unpacking, variable scope (local, enclosing, global, nonlocal),
    recursion, lambda functions, and commonly used built-in functions.

Expected output is shown in "# -->" comments.
"""

#========================
# DEFINING A FUNCTION
#========================
def greet(name):
    """Print a greeting for the given name (no return value)."""
    print(f"Hello {name}")


greet("ahmed")  # --> Hello ahmed


#========================
# FUNCTION WITH A RETURN VALUE
#========================
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add(2, 3))  # --> 5


#========================
# DEFAULT PARAMETERS
#========================
# The default value is used when the argument is not provided.
def say_hello(name='Guest'):
    print(f"Hello {name}")


say_hello()         # --> Hello Guest
say_hello("osama")  # --> Hello osama


#========================
# ARGUMENT PACKING: *args
#========================
# *args collects any number of positional arguments into a tuple.
def add_numbers(*args):
    return sum(args)


print(add_numbers(1, 2, 3))     # --> 6
print(add_numbers(4, 5, 6, 7))  # --> 22


#========================
# ARGUMENT PACKING: **kwargs
#========================
# **kwargs collects any number of keyword arguments into a dictionary.
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_details(name="Alice", age=30, city="New York")
# --> name: Alice
#     age: 30
#     city: New York


#========================
# ARGUMENT UNPACKING
#========================
def hello(name, age):
    print(f"Hello {name}, your age is {age}")


# * unpacks a tuple/list into positional arguments
person_tuple = ("Bob", 18)
hello(*person_tuple)  # --> Hello Bob, your age is 18


def greeting(name, age):
    print(f"Hello, {name}! You are {age} years old.")


# ** unpacks a dictionary into keyword arguments (keys must match parameter names)
person_dict = {"name": "Carol", "age": 28}
greeting(**person_dict)  # --> Hello, Carol! You are 28 years old.


#========================
# SCOPE: LOCAL
#========================
# A variable created inside a function exists only inside that function.
def show_local():
    local_var = 10
    print(local_var)


show_local()  # --> 10

try:
    print(local_var)
except NameError as error:
    print(f"NameError: {error}")  # --> NameError: name 'local_var' is not defined


#========================
# SCOPE: ENCLOSING (NONLOCAL)
#========================
# An inner function can read variables of the function that contains it.
def outer_function():
    enclosing_var = 20

    def inner_function():
        print(enclosing_var)

    inner_function()


outer_function()  # --> 20


#========================
# SCOPE: GLOBAL
#========================
# Functions can read global variables.
global_var = 30


def read_global():
    print(global_var)


read_global()  # --> 30


#========================
# THE global KEYWORD
#========================
# Without `global`, assigning inside a function would create a new local variable.
counter = 100


def modify_global():
    global counter
    counter = 200


modify_global()
print(counter)  # --> 200


#========================
# THE nonlocal KEYWORD
#========================
# nonlocal lets an inner function modify a variable of the enclosing function.
def outer_func():
    value = 50

    def inner_func():
        nonlocal value
        value = 60

    inner_func()
    print(value)  # --> 60


outer_func()


#========================
# RECURSION
#========================
# A recursive function calls itself and needs a base case that stops the calls.
def delete_letters(word):
    """Remove consecutive repeated letters: 'aabbc' -> 'abc'."""
    if len(word) == 1:  # base case
        return word

    if word[0] == word[1]:
        return delete_letters(word[1:])  # skip the repeated first letter

    return word[0] + delete_letters(word[1:])


print(delete_letters("wwwwwwwwoooooooorrrrrrrllllldddd"))  # --> world


def factorial(number):
    """Return number! (e.g. 5! = 5 * 4 * 3 * 2 * 1)."""
    if number in (0, 1):  # base case
        return 1
    return number * factorial(number - 1)


print(factorial(5))  # --> 120


#========================
# LAMBDA FUNCTIONS
#========================
# lambda: a small anonymous function written as a single expression.
make_greeting = lambda name, age: f"Hello {name}!, your age is {age}."

print(make_greeting("ahmed", 18))  # --> Hello ahmed!, your age is 18.
print(type(make_greeting))         # --> <class 'function'>


#========================
# BUILT-IN FUNCTIONS: TRUTH TESTS AND CONVERSIONS
#========================
# all(): True if ALL elements are truthy
print(all([1, 2, 3, 4]))  # --> True

# any(): True if AT LEAST ONE element is truthy
# (takes ONE iterable; [], (), and '' are falsy, 3 is truthy)
print(any([[], (), '', 3]))  # --> True

# bin(): integer -> binary string, prefixed with "0b"
print(bin(10))  # --> 0b1010

# ord(): character -> its numeric code (ASCII for basic characters)
print(ord("a"))  # --> 97
print(ord("A"))  # --> 65

# chr(): numeric code -> character
print(chr(65))  # --> A
print(chr(97))  # --> a

# id(): unique identifier (memory address) of an object
number_x = 10
print(id(number_x))  # --> a large number that differs on every run


#========================
# BUILT-IN FUNCTIONS: MATH
#========================
# sum(iterable, start=0): add all elements (plus the optional start value)
print(sum([67, 23, 12, 23]))    # --> 125
print(sum([12, 23, 45], 19))    # --> 99  (12 + 23 + 45 + 19)

# round(number, digits): round to `digits` decimals (nearest integer if omitted)
print(round(3.14159))     # --> 3
print(round(3.14159, 2))  # --> 3.14

# abs(): absolute value
print(abs(100))   # --> 100
print(abs(-100))  # --> 100

# pow(base, exponent, modulus): base ** exponent, with an optional modulus
print(pow(2, 3))     # --> 8
print(pow(2, 3, 3))  # --> 2  (8 % 3)

# min() / max(): smallest / largest element of an iterable
print(min([1, 2, 3, 4]))  # --> 1
print(max([1, 2, 3, 4]))  # --> 4


#========================
# BUILT-IN FUNCTIONS: SEQUENCES
#========================
# range(start, end, step): end is NOT included
print(list(range(0, 20, 2)))  # --> [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(list(range(10)))        # --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# slice(start, end, step): a reusable slice object (end is NOT included)
letters = ["A", "B", "C", "D", "E", "F"]
print(letters[slice(3)])        # --> ['A', 'B', 'C']
print(letters[slice(0, 5, 2)])  # --> ['A', 'C', 'E']

# del: a statement (not a function) that deletes list items, dict keys, or variables
veggies = ["tomato", "carrot", "lettuce"]
del veggies[1]
print(veggies)  # --> ['tomato', 'lettuce']


#========================
# BUILT-IN FUNCTIONS: print() OPTIONS
#========================
# sep: text placed between the values (default: a space)
print("my", "name", "is", "ahmed", sep="-")  # --> my-name-is-ahmed

# end: text printed at the end (default: a new line)
print('i love python ', end="and php")  # --> i love python and php
print()  # finishes the line, so the output below starts on a new line


#========================
# BUILT-IN FUNCTIONS: help() AND eval()
#========================
# help(): show documentation of a function, class, module, or keyword
help(print)  # --> prints the documentation of print()

# eval(): run a Python expression stored in a string
# Only use it with trusted strings: it executes whatever code it receives.
print(eval("2 + 3 * 4"))  # --> 14