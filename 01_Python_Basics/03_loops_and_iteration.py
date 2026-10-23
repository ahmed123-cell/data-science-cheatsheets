"""
Python Iteration Tools: a study reference.

Covers map(), filter(), reduce(), enumerate(), reversed(), and zip().

Note: map(), filter(), enumerate(), reversed(), and zip() return iterators.
They produce values lazily and can be consumed only once, so wrap them in
list() (or loop over them) to see the results.

Expected output is shown in "# -->" comments.
"""

from functools import reduce


#========================
# MAP(): TRANSFORM EVERY ITEM
#========================
# map(function, iterable): apply a function to every item and return a map object
# (an iterator). Useful for transforming data without writing an explicit loop.
def square(x):
    """Return x multiplied by itself."""
    return x * x


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # --> [1, 4, 9, 16, 25]


#========================
# MAP() WITH LAMBDA
#========================
# A lambda is handy for short, one-off functions.
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x * x, numbers)
print(list(squared_numbers))  # --> [1, 4, 9, 16, 25]


#========================
# FILTER(): KEEP MATCHING ITEMS
#========================
# filter(function, iterable): keep only the items for which the function returns True.
def is_even(n):
    """Return True if n is even."""
    return n % 2 == 0


numbers = [1, 2, 3, 4, 5]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))  # --> [2, 4]


#========================
# FILTER() WITH LAMBDA
#========================
numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda n: n % 2 == 0, numbers)
print(list(even_numbers))  # --> [2, 4]


#========================
# REDUCE(): COMBINE ITEMS INTO ONE VALUE
#========================
# reduce(function, iterable): apply a two-argument function cumulatively,
# e.g. for [1, 8, 2] it computes (1 + 8) = 9, then (9 + 2) = 11.
# It lives in the functools module (imported at the top of the file).
def sum_all(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2


numbers = [1, 8, 2, 9, 100, 30]
sum_result = reduce(sum_all, numbers)
print(sum_result)  # --> 150


#========================
# REDUCE() WITH LAMBDA
#========================
numbers = [1, 2, 3, 4, 5]
multiply_result = reduce(lambda x, y: x * y, numbers)
print(multiply_result)  # --> 120  (1 * 2 * 3 * 4 * 5)


#========================
# ENUMERATE(): LOOP WITH A COUNTER
#========================
# enumerate(iterable, start=0): yields (index, item) pairs.
fruits = ['apple', 'banana', 'guava']
fruit_counter = enumerate(fruits, start=1)

for index, fruit in fruit_counter:
    print(f"{index}: {fruit}")
# --> 1: apple
#     2: banana
#     3: guava

print(type(fruit_counter))  # --> <class 'enumerate'>


#========================
# REVERSED(): ITERATE BACKWARDS
#========================
# reversed() returns an iterator, so printing it directly shows an object
# like <reversed object at 0x...>. Join the letters to see the reversed string.
print(''.join(reversed('ahmed')))  # --> demha

for num in reversed([1, 2, 3, 4]):
    print(num)  # --> 4
                #     3
                #     2
                #     1


#========================
# ZIP(): PAIR ITEMS FROM SEVERAL ITERABLES
#========================
# zip() combines items by position and stops at the shortest iterable.
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

combined = zip(names, ages)
print(list(combined))  # --> [('Alice', 25), ('Bob', 30), ('Charlie', 35)]