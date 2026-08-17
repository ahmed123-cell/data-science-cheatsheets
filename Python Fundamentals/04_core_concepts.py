#-----------------------------------------------------------------------------------------------------------
# Import Module

# Import a Standard Module
import math
print(math.sqrt(16)) # --> 4.0

# Importing Specific Functions or Variables
from math import pi, factorial
print(pi) # --> 3.141592653589793
print(math.factorial(5)) # --> 120

# Using Aliases
import random as ran
print(ran.randint(1, 10)) # --> 4 (random number)

# Import Custom Module
import helper_functions as hf
print(hf.delete_letter("aaaaaaaahhhhhhhmmmmmeeeeeedddd")) # --> ahmed

# Show all functions and variables of a module
print(dir(math))
#-----------------------------------------------------------------------------------------------------------
# Iterator & Iterable
"""
An Iterable is any object you can loop over (like a list, tuple, or string) -
it has an __iter__() method that returns an Iterator.
An Iterator is the object that actually produces the values one at a time
using __next__(), and it remembers its current position (state) between calls.
Every Iterator is also an Iterable, but not every Iterable is an Iterator.
"""
mylist= [1, 2, 3]
my_iterator= iter(mylist)
print(next(my_iterator)) # --> 1
print(next(my_iterator)) # --> 2
print(next(my_iterator)) # --> 3
#-----------------------------------------------------------------------------------------------------------
# Generators
"""
A Generator is a special kind of function that uses "yield" instead of
"return" to produce a sequence of values, one at a time, without storing
them all in memory. Each call to next() resumes the function right where
it left off, keeping its previous state (variables, loop position, etc.).
This makes generators memory-efficient and great for large or infinite
sequences. Every generator is automatically an Iterator.
"""
# EX:
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for number in count_up_to(5):
    print(number) # 1, 2, 3, 4, 5
#----------------------------------------------------
# EX2:
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()

for i in range(10):
    print(next(gen))
#-----------------------------------------------------------------------------------------------------------
# Decorator
"""
A Decorator is a function that takes another function as input, wraps it
with extra behavior (before/after logic, validation, logging, etc.), and
returns a new function - all without changing the original function's code.
It's applied using the "@decorator_name" syntax placed right above the
function definition.
"""
# Creating Simpler Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():    #                  Something is happening before the function is called.
    print("Hello!") #----------------> Hello!
                    #                  Something is happening after the function is called.
say_hello()
#--------------------------------------------------------------------
# Decorator with Arguments
def our_decorator(func):
    def wrapper(n1, n2):
        if n1 < 0 or n2 < 0:
            print("Negative numbers are not allowed.")
            return
        return func(n1, n2)
    return wrapper

@our_decorator
def add_numbers(n1, n2):
    return n1 + n2

print(add_numbers(5, 3))  # --> 8
print(add_numbers(-1, 3))  # --> Negative numbers are not allowed.

#-----------------------------------------------------------------------------------------------------------
# Documentation
def say_helloo(name):
    '''This function will say hello to this name.'''
    return f'Hello {name.capitalize()}'
print(say_helloo("ahmed")) # --> Hello Ahmed
print(say_helloo.__doc__) # --> This function will say hello to this name
#-----------------------------------------------------------------------------------------------------------
# Type Hinting
def give_name(name: str) -> str: 
    print(f"hello {name}")

def add_numbers(lst: list[int]) -> int:
    print(sum(lst))