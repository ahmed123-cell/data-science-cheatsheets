"""
Python Core Concepts: a study reference.

Topics covered:
    modules and imports, iterators and iterables, generators, decorators,
    docstrings (documentation), and type hinting.

Requires helper_functions.py in the same folder (used in the import section).
Expected output is shown in "# -->" comments.
"""

#========================
# IMPORTING MODULES
#========================
# (Imports are kept here, next to their explanation, for study purposes.
#  In real projects, put all imports at the top of the file.)

# Import a whole standard module
import math
print(math.sqrt(16))  # --> 4.0

# Import specific names so they can be used without the "math." prefix
from math import pi, factorial
print(pi)            # --> 3.141592653589793
print(factorial(5))  # --> 120

# Use an alias to shorten a module name
import random as ran
print(ran.randint(1, 10))  # --> a random integer from 1 to 10 (e.g. 4)

# Import your own module (helper_functions.py in the same folder)
import utils as ut
print(ut.delete_letter("aaaaaaaahhhhhhhmmmmmeeeeeedddd"))  # --> ahmed

# dir(): list all names (functions, variables...) a module provides
print(dir(math))  # --> ['__doc__', '__loader__', ..., 'sqrt', 'tan', 'tanh', 'trunc']


#========================
# ITERATORS AND ITERABLES
#========================
# Iterable : any object you can loop over (list, tuple, string...).
#            It has an __iter__() method that returns an iterator.
# Iterator : produces values one at a time with __next__() and remembers
#            its position between calls.
# Every iterator is also an iterable, but not every iterable is an iterator.
numbers = [1, 2, 3]
numbers_iterator = iter(numbers)  # get an iterator from the iterable

print(next(numbers_iterator))  # --> 1
print(next(numbers_iterator))  # --> 2
print(next(numbers_iterator))  # --> 3
# Another next() here would raise StopIteration (the iterator is exhausted).


#========================
# GENERATORS
#========================
# A generator is a function that uses "yield" instead of "return" to produce
# values one at a time, without storing them all in memory. Each next() call
# resumes the function where it left off, keeping its state (variables, loop
# position). This suits large or infinite sequences. Every generator is an iterator.
def count_up_to(limit):
    """Yield the numbers from 1 up to and including limit."""
    count = 1
    while count <= limit:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)  # --> 1, 2, 3, 4, 5 (one per line)


#========================
# GENERATORS: INFINITE SEQUENCE
#========================
# The loop never ends on its own, so we pull only the values we need with next().
def infinite_sequence():
    """Yield 0, 1, 2, 3, ... forever."""
    num = 0
    while True:
        yield num
        num += 1


sequence = infinite_sequence()

for _ in range(10):
    print(next(sequence))  # --> 0, 1, 2, ... 9 (one per line)


#========================
# DECORATORS: BASIC
#========================
# A decorator is a function that takes another function, wraps it with extra
# behavior (logging, validation, before/after logic...), and returns the new
# function without changing the original code. Apply it with @decorator_name
# right above the function definition.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()
# --> Something is happening before the function is called.
#     Hello!
#     Something is happening after the function is called.


#========================
# DECORATORS: WITH ARGUMENTS
#========================
# The wrapper must accept the same arguments as the function it wraps.
def our_decorator(func):
    def wrapper(n1, n2):
        if n1 < 0 or n2 < 0:
            print("Negative numbers are not allowed.")
            return  # returns None
        return func(n1, n2)
    return wrapper


@our_decorator
def add_numbers(n1, n2):
    return n1 + n2


print(add_numbers(5, 3))   # --> 8
print(add_numbers(-1, 3))  # --> Negative numbers are not allowed.
                           #     None  (the wrapper returned nothing)


#========================
# DOCUMENTATION (DOCSTRINGS)
#========================
# A string placed right under the def line is the function's docstring.
# It is available through the __doc__ attribute (and help()).
def say_hello_to(name):
    """This function will say hello to this name."""
    return f'Hello {name.capitalize()}'


print(say_hello_to("ahmed"))   # --> Hello Ahmed
print(say_hello_to.__doc__)    # --> This function will say hello to this name.


#========================
# TYPE HINTING
#========================
# Hints describe the expected types of parameters (name: str) and of the
# return value (-> str). Python does NOT enforce them; they help readers
# and tools. These functions print instead of returning, so they are hinted -> None.
def give_name(name: str) -> None:
    print(f"hello {name}")


def print_sum(numbers: list[int]) -> None:
    print(sum(numbers))


give_name("ahmed")    # --> hello ahmed
print_sum([1, 2, 3])  # --> 6