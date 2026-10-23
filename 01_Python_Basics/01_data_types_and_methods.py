"""
Python Types and Methods: a study reference.

Covers the most common built-in methods of:
    strings, lists, sets, and dictionaries.

Expected output is shown in "# -->" comments.
Note: sets are unordered, so the printed order of set elements may vary.
"""

#========================
# STRING METHODS: SIZE AND CLEANING
#========================
# len(): number of characters (also works on lists, tuples, dicts, sets...,
# but not on integers)
print(len('programming'))  # --> 11

# strip(): remove spaces (or the given characters) from both ends
print('         hello world      '.strip())                      # --> hello world
print("@@@@@@@@@@@@hello world@@@@@@@@@@@@@@@".strip('@'))      # --> hello world


#========================
# STRING METHODS: CHANGING CASE
#========================
text = 'i love python and 4g graphics and @gmail'

# title(): capitalize each word; a letter after a digit or symbol is capitalized too
print(text.title())       # --> I Love Python And 4G Graphics And @Gmail

# capitalize(): capitalize only the first letter of the string
print(text.capitalize())  # --> I love python and 4g graphics and @gmail

# upper() / lower(): all capital / all small letters
print("i love html".upper())  # --> I LOVE HTML
print("I LOVE HTML".lower())  # --> i love html

# swapcase(): swap capital letters with small ones and vice versa
print("i LOve PYthon".swapcase())  # --> I loVE pyTHON


#========================
# STRING METHODS: PADDING AND ALIGNMENT
#========================
# zfill(width): pad with zeros on the left until the string reaches `width`
print('5'.zfill(3))   # --> 005
print("53".zfill(3))  # --> 053

# center(width, fill_char): center the string inside `width`, padded with fill_char
print("i love python".center(21, "#"))  # --> ####i love python####


#========================
# STRING METHODS: SPLITTING
#========================
# split(): string -> list. Default separator is whitespace.
# The optional second argument is the maximum number of splits.
print("i love python and html".split())          # --> ['i', 'love', 'python', 'and', 'html']
print("i-love-python-and-html".split("-", 3))    # --> ['i', 'love', 'python', 'and-html']

# rsplit(): same as split() but starts counting from the right
print("i-love-python-and-html".rsplit("-", 3))   # --> ['i-love', 'python', 'and', 'html']

# splitlines(): split at line breaks (\n)
print("i love python\nand html".splitlines())    # --> ['i love python', 'and html']


#========================
# STRING METHODS: SEARCHING AND REPLACING
#========================
sentence = "i love python and html"

# count(): how many times a substring appears
print(sentence.count("python"))  # --> 1

# replace(old, new): return a new string with `old` replaced by `new`
print(sentence.replace("python", "java"))  # --> i love java and html

# find(): index of the first match, or -1 if not found
print(sentence.find("p"))   # --> 7

# index(): index of the first match, or raises ValueError if not found
print(sentence.index("p"))  # --> 7

# startswith() / endswith(): check the beginning / end of the string
print(sentence.startswith("i"))     # --> True
print(sentence.endswith("html"))    # --> True


#========================
# STRING METHODS: CONTENT CHECKS
#========================
# isalnum(): only letters and numbers?
print("ilovepython".isalnum())  # --> True

# isalpha(): only letters?
print("ilovepython".isalpha())  # --> True

# isdigit(): only digits?
print("12345".isdigit())  # --> True


#========================
# LIST METHODS: ADDING ELEMENTS
#========================
# append(): add ONE element to the end
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # --> [1, 2, 3, 4]

# extend(): add ALL elements of another list to the end
numbers = [1, 2, 3]
numbers.extend([5, 6, 7])
print(numbers)  # --> [1, 2, 3, 5, 6, 7]

# insert(index, element): add an element at a specific index
numbers = [1, 3, 4]
numbers.insert(1, 2)
print(numbers)  # --> [1, 2, 3, 4]


#========================
# LIST METHODS: REMOVING ELEMENTS
#========================
# remove(): delete the first occurrence of a value
numbers = [1, 2, 4]
numbers.remove(4)
print(numbers)  # --> [1, 2]

# pop(): remove AND return an element (the last one by default, or the one at a given index)
numbers = [1, 2, 3, 4]
print(numbers.pop())   # --> 4  (last element)
print(numbers.pop(2))  # --> 3  (element at index 2)
print(numbers)         # --> [1, 2]

# clear(): remove all elements
numbers = [1, 2, 3]
numbers.clear()
print(numbers)  # --> []


#========================
# LIST METHODS: ORDERING, COPYING, AND SEARCHING
#========================
# sort(): sort in place (ascending numbers, or alphabetical order)
numbers = [5, 2, 3]
numbers.sort()
print(numbers)  # --> [2, 3, 5]

# reverse(): reverse the order of elements in place
numbers = [4, 5, 6]
numbers.reverse()
print(numbers)  # --> [6, 5, 4]

# copy(): create a separate (shallow) copy of the list
numbers = [1, 2, 3]
numbers_copy = numbers.copy()
print(numbers_copy)  # --> [1, 2, 3]

# count(): how many times a value appears
numbers = [1, 1, 4, 1]
print(numbers.count(1))  # --> 3

# index(): position of the first occurrence of a value
numbers = [1, 2, 3, 4]
print(numbers.index(1))  # --> 0


#========================
# SET METHODS: OVERVIEW
#========================
# A set is an unordered collection of unique elements (no duplicates).
# Methods that change a set in place (add, discard, clear, pop) return None,
# so call them first, then print the set.


#========================
# SET METHODS: ADDING AND REMOVING
#========================
# add(): add one element
numbers = {1, 2, 3}
numbers.add(6)
print(numbers)  # --> {1, 2, 3, 6}

# discard(): remove an element (no error if it is missing)
numbers = {1, 2, 3}
numbers.discard(3)
print(numbers)  # --> {1, 2}

# pop(): remove and return an arbitrary element
numbers = {3, 7, 1, 9, 5}
print(numbers.pop())  # --> any one element of the set (e.g. 1)

# clear(): remove all elements
numbers = {1, 2, 3}
numbers.clear()
print(numbers)  # --> set()  (an empty set; {} would be an empty dict)


#========================
# SET METHODS: COMBINING SETS
#========================
# union() or |: all elements from both sets
set_a = {"one", "two", "three"}
set_b = {"four", "five", "six"}
print(set_a.union(set_b))  # --> {'two', 'four', 'five', 'three', 'six', 'one'} (order may vary)
print(set_a | set_b)       # --> same as above

# intersection() or &: elements common to both sets
set_a = {"one", "two", "three"}
set_b = {"three", "four", "five"}
print(set_a.intersection(set_b))  # --> {'three'}
print(set_a & set_b)              # --> {'three'}

# difference() or -: elements in the first set but not in the second
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.difference(set_b))  # --> {1, 2}
print(set_a - set_b)            # --> {1, 2}

# symmetric_difference() or ^: elements in either set, but not in both
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a.symmetric_difference(set_b))  # --> {1, 4}
print(set_a ^ set_b)                      # --> {1, 4}


#========================
# SET METHODS: RELATIONSHIPS BETWEEN SETS
#========================
# issuperset(): does this set contain ALL elements of the other set?
set_a = {1, 2, 3, 4, 5}
set_b = {2, 4}
print(set_a.issuperset(set_b))  # --> True

# issubset(): are ALL elements of this set inside the other set? (reverse of superset)
set_a = {1, 2}
set_b = {1, 2, 3}
print(set_a.issubset(set_b))  # --> True

# isdisjoint(): do the two sets have NO elements in common?
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print(set_a.isdisjoint(set_b))  # --> True


#========================
# DICTIONARIES: ACCESSING VALUES
#========================
person = {"name": "ahmed", "age": 18, "skills": ["python", "html"]}

print(person["name"])      # --> ahmed  (KeyError if the key is missing)
print(person.get("name"))  # --> ahmed  (returns None if the key is missing)


#========================
# DICTIONARIES: NESTED (TWO-DIMENSIONAL)
#========================
languages = {
    "one":   {"name": "HTML",   "progress": "80%"},
    "two":   {"name": "Python", "progress": "50%"},
    "three": {"name": "CSS",    "progress": "50%"},
}
print(languages["one"])               # --> {'name': 'HTML', 'progress': '80%'}
print(languages["three"]["progress"]) # --> 50%  (chain keys to go deeper)


#========================
# DICTIONARY METHODS: READING
#========================
person = {"name": "ahmed", "age": 18, "skills": ["python", "html"]}

# keys(): all keys
print(person.keys())  # --> dict_keys(['name', 'age', 'skills'])

# values(): all values
print(person.values())  # --> dict_values(['ahmed', 18, ['python', 'html']])


#========================
# DICTIONARY METHODS: MODIFYING
#========================
# update(): change existing keys and/or add new ones
scores = {"a": 1, "b": 2}
scores.update({"b": 3, "c": 4})
print(scores)  # --> {'a': 1, 'b': 3, 'c': 4}

# setdefault(): return the value of a key; if the key is missing,
# add it with the given default and return that default
person = {"name": "ahmed"}
print(person.setdefault("name", "osama"))  # --> ahmed  (key exists, unchanged)
print(person.setdefault("age", 19))        # --> 19     (key added)

# popitem(): remove and return the last inserted (key, value) pair as a tuple
course = {"rank": "perfect", "oop": "required"}
print(course.popitem())  # --> ('oop', 'required')

# clear(): remove all items. It changes the dict in place and returns None.
person = {"name": "ahmed", "age": 18, "skills": ["python", "html"]}
print(person.clear())  # --> None


#========================
# DICTIONARY METHODS: CREATING
#========================
# dict.fromkeys(keys, value): new dict where every key gets the same value
keys = ("one", "two", "three")
default_value = "x"
print(dict.fromkeys(keys, default_value))  # --> {'one': 'x', 'two': 'x', 'three': 'x'}