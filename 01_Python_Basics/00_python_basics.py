"""
Python Fundamentals: a study reference.

Topics covered:
    print, variables, data types, escape sequences, strings (concatenation,
    indexing, slicing, repetition, formatting), booleans, operators, casting,
    user input, conditions, membership, and loops.

Run the file top to bottom. Expected output is shown in "# -->" comments.
Note: the "User Input" section pauses and waits for you to type.
"""

#========================
# PRINT STATEMENT
#========================
print("Hello World")  # --> Hello World


#========================
# VARIABLES
#========================
# Rules: cannot start with a number, cannot contain spaces or special
# characters (only letters, digits, and _), and are case-sensitive.
student_name = 'ahmed'

# Assign several variables in one line
a, b, c = 1, 2, 3


#========================
# DATA TYPES
#========================
# int, float, str, list, tuple, dict, set, bool
print(type(5))                            # --> <class 'int'>
print(type(5.5))                          # --> <class 'float'>
print(type("Hello"))                      # --> <class 'str'>
print(type([1, 2, 3]))                    # --> <class 'list'>
print(type((1, 2, 3)))                    # --> <class 'tuple'>
print(type({'name': 'ahmed', 'age': 25})) # --> <class 'dict'>
print(type({1, 2, 3}))                    # --> <class 'set'>
print(type(True))                         # --> <class 'bool'>


#========================
# ESCAPE SEQUENCES (BACKSLASH)
#========================
# \b : backspace (erases the previous character in the terminal)
print("hello\bworld")  # --> hellworld  (the "o" is erased)

# \ at end of line : continues the string on the next line (no newline added)
print("hello \
world")  # --> hello world

# \' or \" : escape a quote inside a string
print('hello \'world\'')  # --> hello 'world'

# \n : new line
print("hello\nworld")  # --> hello
                       #     world

# \r : carriage return (cursor returns to line start, later text overwrites)
print("12345\rAbcd")  # --> Abcd5

# \t : tab
print("hello\tworld")  # --> hello    world


#========================
# STRING CONCATENATION
#========================
word1 = 'i love'
word2 = 'programming'
print(word1 + ' ' + word2)  # --> i love programming


#========================
# QUOTES AND MULTI-LINE STRINGS
#========================
# Use the opposite quote type to include quotes without escaping
single_quoted = 'i love python "test" '
double_quoted = "i love python 'test' "

# Triple quotes allow multi-line strings; "\\" produces one literal backslash
multi_line = '''i love python
it makes \\feel "good" '''
# multi_line --> i love python
#                it makes \feel "good"


#========================
# STRING INDEXING, SLICING, AND STEPS
#========================
word = 'programming'
print(word[0])   # --> p   (first character)
print(word[-1])  # --> g   (last character)

# Slice syntax: [start:end:step]. The end index is NOT included.
print(word[0:3])    # --> pro
print(word[0:6:2])  # --> porm  (indexes 0, 2, 4, 6... up to index 5)


#========================
# BOOLEANS AND LOGICAL OPERATORS
#========================
print(100 > 4)  # --> True
print(2 == 9)   # --> False

# and: True only if ALL conditions are True
print(100 > 99 and 5 == 5 and 2 == 2)  # --> True

# or: True if AT LEAST ONE condition is True
print(88 > 99 or 4 == 9 or 2 >= 1)  # --> True

# not: reverses the logical state
age = 19
print(age > 18)      # --> True
print(not age > 18)  # --> False


#========================
# ARITHMETIC OPERATORS
#========================
# +  -  *  /  %  //  **
#              ^    ^ floor division, power
print(5.6 * 2)   # --> 11.2
print(121 // 6)  # --> 20  (floor division drops the remainder)


#========================
# REPETITION
#========================
text = "ahmed"
numbers = [1, 2]

print(text * 6)     # --> ahmedahmedahmedahmedahmedahmed
print(numbers * 6)  # --> [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]


#========================
# STRING FORMATTING
#========================
name = 'ahmed'
age = 18
skill = 'python'
rank = 1.897

# Old way: % operator (%s = string, %d = integer, %.2f = float, 2 decimals)
print("hello my name is %s and i am %d years old. My skill is %s and my rank is %.2f"
      % (name, age, skill, rank))

# Older way: str.format()
print("hello my name is {} and i am {} years old. My skill is {} and my rank is {:.2f}"
      .format(name, age, skill, rank))

# Modern way: f-strings (recommended)
# Note: no format spec on rank here, so it prints 1.897 (use {rank:.2f} for 1.90)
print(f"hello my name is {name} and i am {age} years old. My skill is {skill} and my rank is {rank}")

# Number formatting: thousands separators
number = 289469826538976
print(f"the number is {number:,}")           # --> the number is 289,469,826,538,976
print("the number is {:_}".format(number))   # --> the number is 289_469_826_538_976

# Rearranging with index numbers in str.format()
first, second, third = "one", "two", "three"
print("hello {2} {1} {0}".format(first, second, third))  # --> hello three two one


#========================
# ASSIGNMENT OPERATORS
#========================
# =  +=  -=  *=  /=  **=  %=  //=
x = 5
x += 2  # same as: x = x + 2
print(x)  # --> 7


#========================
# COMPARISON OPERATORS
#========================
# >  <  >=  <=  ==  !=
print(100 != 200)  # --> True
print(400 > 450)   # --> False


#========================
# CASTING (TYPE CONVERSION)
#========================
# To string
print(str(899))  # --> 899  (now a str, not an int)

# To list
print(list('osama'))                    # --> ['o', 's', 'a', 'm', 'a']
print(list((1, 2, 3, 4, 5)))            # --> [1, 2, 3, 4, 5]
print(list({4, 5, 6}))                  # --> e.g. [4, 5, 6]  (sets are unordered)
print(list({"a": 1, "b": 2, "c": 3}))   # --> ['a', 'b', 'c']  (keys only)

# To tuple
print(tuple("ahmed"))                   # --> ('a', 'h', 'm', 'e', 'd')
print(tuple([1, 2, 3, 4]))              # --> (1, 2, 3, 4)
print(tuple({4, 5, 6}))                 # --> e.g. (4, 5, 6)  (sets are unordered)
print(tuple({"a": 1, "b": 2, "c": 3}))  # --> ('a', 'b', 'c')  (keys only)

# To dictionary (needs pairs: key, value)
tuple_pairs = (("a", 1), ("b", 2), ("c", 3))
list_pairs = [["x", 4], ["y", 5], ["z", 6]]
print(dict(tuple_pairs))  # --> {'a': 1, 'b': 2, 'c': 3}
print(dict(list_pairs))   # --> {'x': 4, 'y': 5, 'z': 6}


#========================
# USER INPUT
#========================
# input() always returns a string, so convert it when you need a number.
# strip() removes surrounding spaces; capitalize() uppercases the first letter.
name = input("Type your name: ").strip().capitalize()
age = int(input("Type your age: "))
print(f"Hello {name}, your age is {age}")


#========================
# IF / ELIF / ELSE
#========================
age = 10

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
# --> You are a child.


#========================
# SHORT IF (TERNARY EXPRESSION)
#========================
# Syntax: value_if_true if condition else value_if_false
movie_rate = 18
age = 19
print('This movie is not good for you.' if movie_rate > age else "This movie is good for you.")
# --> This movie is good for you.


#========================
# NESTED IF
#========================
age = 20
is_student = True

if age >= 18:
    if is_student:
        print("You are an adult and a student.")
    else:
        print("You are an adult but not a student.")
else:
    print("You are a minor.")
# --> You are an adult and a student.


#========================
# MEMBERSHIP OPERATORS (in / not in)
#========================
my_name = 'mostafa'
print('m' in my_name)      # --> True
print('a' not in my_name)  # --> False

names = ["ahmed", "mahmoud", "osama"]
print("ahmed" in names)    # --> True
print("joe" not in names)  # --> True


#========================
# WHILE LOOP
#========================
count = 0
while count < 5:
    print(f"Count is: {count}")  # --> Count is: 0 ... Count is: 4
    count += 1
else:
    # Optional: runs when the condition becomes False (not after a break)
    print("Loop has finished")  # --> Loop has finished


#========================
# FOR LOOP: LISTS AND STRINGS
#========================
fruits = ['apple', 'banana', 'kiwi']
for fruit in fruits:
    print(fruit)  # --> apple
                  #     banana
                  #     kiwi

for letter in 'joe':
    print(f"[{letter}]")  # --> [j]
                          #     [o]
                          #     [e]


#========================
# FOR LOOP: RANGE AND NESTED LOOPS
#========================
# range(start, end, step): end is NOT included; start=0 and step=1 by default
for num in range(5):
    print(num)  # --> 0 1 2 3 4 (one per line)

# Nested loop: the inner loop runs fully for every step of the outer loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")  # --> i: 0, j: 0 / i: 0, j: 1 / i: 1, j: 0 ...


#========================
# FOR LOOP: DICTIONARIES
#========================
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

# .items() gives (key, value) pairs
for student, score in student_scores.items():
    print(f"{student}: {score}")  # --> Alice: 85
                                  #     Bob: 92
                                  #     Charlie: 78


#========================
# BREAK, CONTINUE, AND PASS
#========================
# break: exits the loop immediately
for i in range(10):
    if i == 5:
        break
    print(i)  # --> 0 1 2 3 4

# continue: skips the rest of the current iteration, moves to the next
for i in range(5):
    if i == 2:
        continue
    print(i)  # --> 0 1 3 4

# pass: does nothing; a placeholder where code is syntactically required
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)  # --> 0 1 3 4