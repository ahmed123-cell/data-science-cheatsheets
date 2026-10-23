"""
Python Standard Library - Study Reference

Modules covered (only the most commonly used functions of each):
    1.  math         - rounding, integer math, combinatorics, powers/logs, trigonometry, constants
    2.  functools    - reduce, lru_cache, cache, cached_property, wraps, partial
    3.  itertools    - count, cycle, accumulate, chain, islice, batched, pairwise,
                       groupby, zip_longest, takewhile, product, permutations, combinations
    4.  collections  - deque, Counter, defaultdict, namedtuple
    5.  datetime     - date, time, datetime, timedelta, time zones (pytz)
    6.  os           - files, folders and paths (the classic way)
    7.  pathlib      - files, folders and paths (the modern, object-oriented way)
    8.  sys          - interpreter and system information
    9.  json         - converting between Python objects and JSON text
    10. random       - random numbers and choices

Requirements:
    - Python 3.12+ (itertools.batched was added in 3.12)
    - pytz is third-party: pip install pytz

Note: sample outputs are written as `# --> ...`. Values that change on every run
(current date/time, random numbers, paths) are marked as examples.
"""

import collections
import functools
import itertools
import json
import math
import operator
import os
import random
import sys
from datetime import date, datetime, time, timedelta
from pathlib import Path

import pytz


#========================
# math: Rounding - ceil(), floor()
#========================
# ceil(x): smallest integer greater than or equal to x
print(math.ceil(4.333))   # --> 5

# floor(x): largest integer less than or equal to x
print(math.floor(3.652))  # --> 3


#========================
# math: Integer Math - factorial(), gcd(), lcm(), prod()
#========================
# factorial(n): n! = n * (n-1) * ... * 1
print(math.factorial(5))         # --> 120

# gcd(*integers): greatest common divisor
print(math.gcd(36, 66))          # --> 6

# lcm(*integers): least common multiple
print(math.lcm(2, 3, 4, 6))      # --> 12

# prod(iterable): product of all elements
print(math.prod([10, 2, 5]))     # --> 100


#========================
# math: Combinatorics - comb(), perm()
#========================
# comb(n, k): ways to choose k items from n, WITHOUT order and without repetition
print(math.comb(10, 6))  # --> 210

# perm(n, k): ways to choose k items from n, WITH order and without repetition
print(math.perm(10, 6))  # --> 151200


#========================
# math: Powers and Logarithms - sqrt(), exp(), log()
#========================
# sqrt(x): square root
print(math.sqrt(9))     # --> 3.0

# exp(x): e raised to the power x
print(math.exp(2))      # --> 7.38905609893065

# log(x, base): logarithm of x to the given base (natural log, base e, by default)
print(math.log(8, 2))   # --> 3.0


#========================
# math: Angles and Trigonometry (angles are in RADIANS)
#========================
# degrees(x) / radians(x): convert between radians and degrees
print(math.degrees(0.5235))  # --> 29.99... (about 30 degrees)
print(math.radians(30))      # --> 0.5235987755982988

# sin(x), cos(x), tan(x): results are approximate because of floating-point math
print(math.sin(0.5235))      # --> 0.4999... (about 0.5)
print(math.cos(0.5235))      # --> 0.8660... (about 0.866)
print(math.tan(0.7853))      # --> 0.9998... (about 1)


#========================
# math: Constants - pi, e, inf, nan
#========================
print(math.pi)   # --> 3.141592653589793
print(math.e)    # --> 2.718281828459045
print(math.inf)  # --> inf (positive infinity)
print(math.nan)  # --> nan (not a number)


#========================
# functools: reduce()
#========================
# reduce(function, iterable, initial): applies a function cumulatively to the
# items, reducing the iterable to a single value.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(functools.reduce(lambda total, n: total + n, numbers))  # --> 55

letters = ["a", "b", "c", "d", "e"]
print(functools.reduce(lambda text, ch: text + ch, letters))  # --> abcde

# The 3rd argument is the starting value (needed when the items aren't plain numbers)
items = [
    {"item_id": 1, "name": "hiking boots", "amount": 150.00, "qty": 1},
    {"item_id": 33, "name": "hiking poles", "amount": 95.00, "qty": 1},
    {"item_id": 1, "name": "hiking pack", "amount": 52.00, "qty": 1},
    {"item_id": 1, "name": "hiking shorts", "amount": 60.00, "qty": 2},
]
print(functools.reduce(lambda total, item: total + item["amount"], items, 0))  # --> 357.0


#========================
# functools: lru_cache()
#========================
# lru_cache(maxsize, typed): decorator that caches a function's results.
#   - maxsize: max number of stored results; when full, the Least Recently Used is dropped
#   - typed:   if True, arguments of different types are cached separately (3 vs 3.0)
@functools.lru_cache(maxsize=128, typed=False)
def fibonacci(n):
    """Return the n-th Fibonacci number (fast thanks to caching)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(35))           # --> 9227465
print(fibonacci.cache_info())  # --> CacheInfo(hits=33, misses=36, maxsize=128, currsize=36)
fibonacci.cache_clear()        # empties the cache (returns None, so there's nothing to print)


#========================
# functools: cache()
#========================
# cache: like lru_cache(maxsize=None) - simpler, but it never discards anything.
# Best for functions with a limited number of possible inputs.
@functools.cache
def factorial(n):
    """Return n! (results are cached)."""
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(10))  # --> 3628800


#========================
# functools: cached_property()
#========================
# cached_property: computes the property once on first access and stores the
# result on the instance. Useful for heavy calculations or database fetches.
class Circle:
    """A circle whose area is calculated once, then reused."""

    def __init__(self, radius):
        self.radius = radius

    @functools.cached_property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(circle.area)  # --> 78.5 (calculated)
print(circle.area)  # --> 78.5 (taken from the cache, not recalculated)


class User:
    """A user whose profile is 'fetched' only once."""

    def __init__(self, user_id):
        self.user_id = user_id

    @functools.cached_property
    def profile(self):
        return {"name": "john doe", "age": 30}  # imagine a database query here


user = User(1)
print(user.profile)  # --> {'name': 'john doe', 'age': 30} (fetched)
print(user.profile)  # --> {'name': 'john doe', 'age': 30} (cached, no refetch)


#========================
# functools: wraps()
#========================
# wraps(func): copies the name and docstring of the original function onto the
# wrapper, so custom decorators don't hide them.
def my_decorator(func):
    """Decorator that prints a message before and after the call."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
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
# --> Something is happening before the function is called.
# --> Hello Alice!
# --> Something is happening after the function is called.

print(say_hello.__name__)  # --> say_hello (would be "wrapper" without @wraps)
print(say_hello.__doc__)   # --> Greet someone by name (would be None without @wraps)


#========================
# functools: partial()
#========================
# partial(func, ...): creates a new function with some arguments pre-filled.
def power(base, exponent):
    return base ** exponent


square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print(square(5))  # --> 25
print(cube(2))    # --> 8


#========================
# itertools: count() and cycle() - infinite iterators
#========================
# count(start, step): endless counter (start and step can be ints or floats)
counter = itertools.count(10, 2)
print([next(counter) for _ in range(3)])  # --> [10, 12, 14]

# cycle(iterable): repeats the elements over and over
letters_cycle = itertools.cycle("ABCD")
print([next(letters_cycle) for _ in range(8)])  # --> ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D']


#========================
# itertools: accumulate()
#========================
# accumulate(iterable, func): running totals (a running sum by default)
print(list(itertools.accumulate([1, 2, 3, 4, 5])))                # --> [1, 3, 6, 10, 15]

# Pass another function for a different operation, e.g. running product
print(list(itertools.accumulate([1, 2, 3, 4, 5], operator.mul)))  # --> [1, 2, 6, 24, 120]


#========================
# itertools: chain() and chain.from_iterable()
#========================
# chain(*iterables): joins several iterables into one sequence
print(list(itertools.chain(["a", "b", "c"], ["e", "f", "g"])))  # --> ['a', 'b', 'c', 'e', 'f', 'g']

# chain.from_iterable(iterable_of_iterables): flattens one level of nesting
list_of_lists = [[1, 2, 3], ["a", "b", "c"], [4, 5, 6]]
print(list(itertools.chain.from_iterable(list_of_lists)))  # --> [1, 2, 3, 'a', 'b', 'c', 4, 5, 6]


#========================
# itertools: islice()
#========================
# islice(iterable, start, stop, step): slicing for ANY iterable (not just lists)
print(list(itertools.islice(range(10), 2, 8, 2)))  # --> [2, 4, 6]


#========================
# itertools: batched() and pairwise()
#========================
# batched(iterable, n): groups elements into chunks of size n (Python 3.12+)
print(list(itertools.batched("ABCDEFG", n=3)))  # --> [('A', 'B', 'C'), ('D', 'E', 'F'), ('G',)]

# pairwise(iterable): consecutive overlapping pairs (Python 3.10+)
print(list(itertools.pairwise([1, 2, 3, 4, 5])))  # --> [(1, 2), (2, 3), (3, 4), (4, 5)]


#========================
# itertools: groupby()
#========================
# groupby(iterable, key): groups CONSECUTIVE elements that share the same key.
# Sort the data by the key first if you want one group per key.
for key, group in itertools.groupby(["A", "B", "CDE"], key=len):
    print(f"key: {key}")
    print(f"group: {list(group)}")
# --> key: 1
# --> group: ['A', 'B']
# --> key: 3
# --> group: ['CDE']

# Note that 'a' appears twice below: it's not consecutive, so it forms two groups
data = [("a", 1), ("a", 2), ("b", 3), ("b", 4), ("a", 5)]
for key, group in itertools.groupby(data, key=lambda pair: pair[0]):
    print(f"Key: {key}")
    print(f"Group: {list(group)}")
# --> Key: a / Group: [('a', 1), ('a', 2)]
# --> Key: b / Group: [('b', 3), ('b', 4)]
# --> Key: a / Group: [('a', 5)]


#========================
# itertools: zip_longest() and takewhile()
#========================
# zip_longest(*iterables, fillvalue): like zip(), but runs until the LONGEST
# iterable ends, filling the gaps with fillvalue (default None).
numbers_short = [1, 2, 3]
letters_long = ["a", "b", "c", "d", "e"]
print(list(itertools.zip_longest(numbers_short, letters_long, fillvalue="unknown")))
# --> [(1, 'a'), (2, 'b'), (3, 'c'), ('unknown', 'd'), ('unknown', 'e')]

# takewhile(predicate, iterable): yields items until the predicate becomes False
print(list(itertools.takewhile(lambda x: x < 5, [1, 4, 6, 3, 8])))  # --> [1, 4]


#========================
# itertools: product() - Cartesian product
#========================
# product(*iterables, repeat): every possible pairing (like nested for-loops)
print(list(itertools.product(["a", "b"], [1, 2])))
# --> [('a', 1), ('a', 2), ('b', 1), ('b', 2)]

print(list(itertools.product([1, 2, 3], repeat=2)))
# --> [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]


#========================
# itertools: permutations() and combinations()
#========================
# permutations(iterable, length): all orderings (order matters)
print(list(itertools.permutations([1, 2, 3])))
# --> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

print(list(itertools.permutations([1, 2, 3], 2)))
# --> [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations(iterable, length): all selections (order does NOT matter)
print(list(itertools.combinations([1, 2, 3, 4], 2)))
# --> [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


#========================
# collections: deque
#========================
# deque: double-ended queue with fast O(1) appends and pops on BOTH sides
# (a list is slow when you insert or remove at the start).
my_deque = collections.deque([1, 2, 3, 4, 5])
my_deque.append(6)       # right end: [1, 2, 3, 4, 5, 6]
my_deque.appendleft(0)   # left end:  [0, 1, 2, 3, 4, 5, 6]
my_deque.pop()           # removes 6: [0, 1, 2, 3, 4, 5]
my_deque.popleft()       # removes 0: [1, 2, 3, 4, 5]

print(my_deque)  # --> deque([1, 2, 3, 4, 5])


#========================
# collections: Counter
#========================
# Counter: a dict that maps each element to how many times it appears
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_counter = collections.Counter(fruits)

print(fruit_counter["apple"])   # --> 3
print(fruit_counter["banana"])  # --> 2
print(fruit_counter["orange"])  # --> 1

# most_common(n): the n most frequent elements
print(fruit_counter.most_common(1))  # --> [('apple', 3)]
print(fruit_counter.most_common(2))  # --> [('apple', 3), ('banana', 2)]

# update(iterable): ADDS the new counts to the existing ones
fruit_counter.update(["banana", "orange", "orange"])
print(fruit_counter)  # --> Counter({'apple': 3, 'banana': 3, 'orange': 3})


#========================
# collections: defaultdict
#========================
# defaultdict(factory): a dict that creates a default value for missing keys
# (int -> 0, str -> "", list -> []), so you never get a KeyError.
count_dict = collections.defaultdict(int)
print(count_dict["a"])  # --> 0 (the key was created automatically)

count_dict["a"] += 1
count_dict["b"] += 2
print(count_dict)  # --> defaultdict(<class 'int'>, {'a': 1, 'b': 2})

text_dict = collections.defaultdict(str)
print(repr(text_dict["x"]))  # --> '' (empty string)

text_dict["x"] += "Hello"
text_dict["y"] += "World"
print(text_dict)  # --> defaultdict(<class 'str'>, {'x': 'Hello', 'y': 'World'})


#========================
# collections: namedtuple
#========================
# namedtuple(name, fields): a tuple whose items can also be read by name
Point = collections.namedtuple("Point", ["x", "y"])
point = Point(3, 4)

print(point)             # --> Point(x=3, y=4)
print(point.x, point.y)  # --> 3 4
print(point[0])          # --> 3 (still works like a normal tuple)


#========================
# datetime: date
#========================
today = date.today()
print(today)  # --> e.g. 2026-10-23

my_date = date(2024, 5, 15)
print(my_date)                                 # --> 2024-05-15
print(my_date.year, my_date.month, my_date.day)  # --> 2024 5 15
print(my_date.weekday())                       # --> 2 (Monday=0 ... Sunday=6, so Wednesday)
print(my_date.isoformat())                     # --> 2024-05-15 (YYYY-MM-DD)


#========================
# datetime: time
#========================
my_time = time(14, 30, 45)
print(my_time)                                    # --> 14:30:45
print(my_time.hour, my_time.minute, my_time.second)  # --> 14 30 45


#========================
# datetime: datetime - creating, parsing and formatting
#========================
now = datetime.now()
print(now)  # --> e.g. 2026-10-23 14:05:09.123456

my_datetime = datetime(2023, 5, 15, 14, 30)
print(my_datetime)  # --> 2023-05-15 14:30:00

# strptime(text, format): text -> datetime
parsed_date = datetime.strptime("2023-05-15 14:30", "%Y-%m-%d %H:%M")
print(parsed_date)  # --> 2023-05-15 14:30:00

# strftime(format): datetime -> text
print(now.strftime("%Y/%m/%d %H:%M:%S"))  # --> e.g. 2026/10/23 14:05:09

# Common format codes:
#   %Y year (2023)     %y year without century (23)
#   %m month number    %B full month name    %b short month name
#   %d day number      %A full day name      %a short day name
#   %H 24-hour clock   %I 12-hour clock      %p AM/PM
#   %M minute          %S second


#========================
# datetime: timedelta - date arithmetic
#========================
delta = timedelta(days=5, hours=3, minutes=30)
print(delta)  # --> 5 days, 3:30:00

print(now + delta)  # --> the current date and time moved 5 days, 3h 30m forward

date1 = datetime(2023, 5, 15)
date2 = datetime(2023, 5, 10)
difference = date1 - date2
print(difference)                           # --> 5 days, 0:00:00
print(difference.days, difference.seconds)  # --> 5 0

# Duration between two times
start = datetime(2023, 5, 1, 10, 0)
end = datetime(2023, 5, 1, 12, 30)
duration = end - start
print(f"Duration: {duration.total_seconds() / 3600} hours")  # --> Duration: 2.5 hours
print(duration)                                              # --> 2:30:00


#========================
# datetime: Time Zones (pytz)
#========================
# pytz is a third-party package. Since Python 3.9 the standard library also has
# `zoneinfo` (ZoneInfo("Africa/Cairo")), which works the same way.
now_utc = datetime.now(pytz.UTC)
print(now_utc)  # --> e.g. 2026-10-23 11:05:09.123456+00:00

egypt_tz = pytz.timezone("Africa/Cairo")
now_egypt = now_utc.astimezone(egypt_tz)
print(now_egypt)  # --> e.g. 2026-10-23 14:05:09.123456+03:00 (offset depends on daylight saving)


#========================
# os: Files and Folders
#========================
# NOTE: the Windows paths below are examples and don't exist, so the calls that
# would fail or delete things are commented out. Un-comment them with real paths.

# listdir(path): names of the files and folders inside a path
# print(os.listdir(r"E:\MySQL"))
print(os.listdir("."))  # --> list of the items in the current folder (varies)

# os.mkdir(r"E:\hello world")                              # creates a folder
# os.rmdir(r"E:\hello world")                              # removes an EMPTY folder
# os.remove(r"E:\hello world\file.txt")                    # deletes a file
# os.rename(r"E:\Safe Exam bro", r"E:\SafeExamBrowser")    # renames a file or folder


#========================
# os: Working with Paths (os.path)
#========================
# join(*parts): builds a path using the right separator for the operating system
path = os.path.join("E:\\", "Data Science", "example files", "sakila-db")
print(path)  # --> E:\Data Science\example files\sakila-db (on Windows)

# exists / isfile / isdir: they return False (not an error) for paths that don't exist
print(os.path.exists(r"E:\Data Science\example files\sakila-db"))                  # --> True if it exists
print(os.path.isfile(r"E:\Data Science\example files\Sample Data\insurance.csv"))  # --> True for a file
print(os.path.isdir(r"E:\Data Science\example files\Sample Data"))                 # --> True for a folder

# basename / dirname: split a path into its last part and the rest (on Windows)
print(os.path.basename(r"E:\Data Science\example files\Sample Data\insurance.csv"))  # --> insurance.csv
print(os.path.dirname(r"E:\Data Science\example files\Sample Data\insurance.csv"))   # --> E:\Data Science\example files\Sample Data

# getcwd(): current working directory / chdir(path): change it
print(os.getcwd())  # --> e.g. C:\Users\Ahmed\Projects
# os.chdir(r"E:\Data Science\SQL")


#========================
# pathlib: Path Objects
#========================
# pathlib is the modern alternative to os.path: paths are objects, joined with "/"
path = Path("data") / "file.csv"
print(path)           # --> data/file.csv (data\file.csv on Windows)

print(path.exists())  # --> False (True if the file exists)
print(path.name)      # --> file.csv
print(path.stem)      # --> file
print(path.suffix)    # --> .csv
print(path.parent)    # --> data

print(Path.cwd())     # --> current working directory
print(Path.home())    # --> the user's home folder


#========================
# pathlib: Folders and Files
#========================
# mkdir(exist_ok=True): no error if the folder already exists
folder = Path("data")
folder.mkdir(exist_ok=True)

# write_text() / read_text(): write and read a whole text file in one call
file = Path("Files/example.txt")
file.parent.mkdir(parents=True, exist_ok=True)  # make sure "Files" exists first
file.write_text("Hello Ahmed")

text = file.read_text()
print(text)  # --> Hello Ahmed

print(file.is_file(), file.is_dir())  # --> True False
print(file.with_suffix(".md"))        # --> Files/example.md (only builds the path)

# glob(pattern): finds matching files; iterdir() lists everything in a folder
print([p.name for p in Path("Files").glob("*.txt")])  # --> ['example.txt']
print([p.name for p in Path("Files").iterdir()])      # --> ['example.txt']

# file.unlink()  # deletes the file


#========================
# sys: Interpreter and System Information
#========================
print(sys.argv)          # --> ['07_standard_libraries.py'] (script name + command-line arguments)
print(sys.version)       # --> e.g. 3.12.3 (main, ...) [GCC ...]
print(sys.version_info >= (3, 12))  # --> True (compare versions as tuples)
print(sys.platform)      # --> 'win32', 'linux' or 'darwin'
print(sys.path[0])       # --> folder of the running script (first place Python looks for modules)
print(sys.maxsize)       # --> 9223372036854775807 (on 64-bit Python)


#========================
# sys: Memory, Recursion Limit and Output Streams
#========================
# getsizeof(obj): size of an object in bytes
print(sys.getsizeof([1, 2, 3]))  # --> 88 (varies by Python version)

# getrecursionlimit() / setrecursionlimit(n): maximum depth of recursive calls
print(sys.getrecursionlimit())   # --> 1000

# stdout / stderr: the output streams that print() uses (stderr is for errors)
sys.stdout.write("Written to standard output\n")  # --> Written to standard output
sys.stderr.write("Written to standard error\n")   # --> Written to standard error

# sys.exit(code): stops the program immediately (0 = success, non-zero = error)
# sys.exit(0)


#========================
# json: Python Objects <-> JSON Text
#========================
# dumps(obj): Python object -> JSON string
# loads(text): JSON string -> Python object
person = {"name": "Ahmed", "skills": ["python", "sql"], "active": True}

json_text = json.dumps(person)
print(json_text)  # --> {"name": "Ahmed", "skills": ["python", "sql"], "active": true}

# indent makes the output human-readable
print(json.dumps(person, indent=2))
# --> {
# -->   "name": "Ahmed",
# -->   "skills": [
# -->     "python",
# -->     "sql"
# -->   ],
# -->   "active": true
# --> }

restored = json.loads(json_text)
print(restored["skills"])  # --> ['python', 'sql']
print(type(restored))      # --> <class 'dict'>

# For files use json.dump(obj, file) and json.load(file).


#========================
# random: Random Numbers and Choices
#========================
# seed(n) makes the results repeatable. The outputs below are for seed 42.
random.seed(42)

print(random.random())                 # --> 0.6394267984578837 (float from 0.0 up to 1.0)
print(random.randint(1, 10))           # --> 1 (integer from 1 to 10, both included)
print(random.choice(["a", "b", "c"]))  # --> 'c' (one random element)

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)                  # shuffles the list IN PLACE
print(cards)                           # --> [4, 5, 1, 2, 3] (the list in a new random order)

print(random.sample(range(1, 50), 3))  # --> [48, 7, 44] (3 unique random numbers)