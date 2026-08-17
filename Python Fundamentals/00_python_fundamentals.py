# Print Statement
print("Hello World")
#----------------------------------------------------------------------------------------------------------
# Variables: cannot start with a number, cannot contain spaces, cannot contain special characters
var= 'ahmed'

# multi variable
a, b, c = 1, 2, 3
#----------------------------------------------------------------------------------------------------------
# Data Types: int, float, string, list, tuple, dictionary, set, boolean

print(type(5))  #  --> <class 'int'>

print(type(5.5)) # --> <class 'float'>

print(type("Hello")) # --> <class 'str'>

print(type([1, 2, 3])) # --> <class 'list'>

print(type((1, 2, 3))) # --> <class 'tuple'>

print(type({'name': 'ahmed', 'age': 25})) # --> <class 'dict'>

print(type({1, 2, 3})) # --> <class 'set'>

print(type(True)) # --> <class 'bool'>
#----------------------------------------------------------------------------------------------------------
# Back Slash types

# \b: backspace
print("hello\bworld") # --> hell world

# \: escape newline
print("hello \
world") # --> hello world

# \: escape single quote or duble quote
print('hello \'world\'') # --> hello 'world'

# \n: new line
print("hello\nworld") # --> hello
                      #     world

# \r: carriage return
print("12345\rAbcd") # --> Abcd5

# \t: tab
print("hello\tworld") # --> hello    world
#------------------------------------------------------------------------------------------------------------
# Concatenation
word1= 'i love'
word2= 'programming'
print(word1 + ' ' + word2) # --> i love programming
#------------------------------------------------------------------------------------------------------------
string1= 'i love python "test" '
string2= "i love python 'test' "

string3= '''i love python
it makes \\feel "good" '''
#------------------------------------------------------------------------------------------------------------
# String Indexing and Slicing and Steps
word= 'programming'
print(word[0]) # --> p
print(word[-1]) # --> g

print(word[0:3]) # --> pro-------- the last index is not included

print(word[0:6:2]) # --> porm
#-----------------------------------------------------------------------------------------------------------
# Boolen (True and False)
print(100> 4) # --> True
print(2==9) # --> False

# Boolen operators

# and: return true if all conditions are True
print(100> 99 and 5==5 and 2==2) # --> True

# or: return true if at least one condition is True
print(88> 99 or 4==9 or 2>=1) # --> True

# and: reverse the logical state
age= 19
print(age> 18) # --> True
print(not age > 18) # --> False

#-----------------------------------------------------------------------------------------------------------
# Arithmetic Operations
#   +, -, *, /, %, //, **
print(5.6 * 2) # --> 11.2
print(121//6) # --> 20
#-----------------------------------------------------------------------------------------------------------
# Repeat
string ="ahmed"
lst = [1, 2]

print(string *6) # --> ahmedahmedahmedahmedahmedahmed
print(lst *6) # --> [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
#-----------------------------------------------------------------------------------------------------------
# Formating
name= 'ahmed'
age= 18
skill= 'python'
rank= 1.897
# Old Way
print("hello my name is %s and i am %d years old. My skill is %s and my rank is %.2f" % (name, age, skill, rank))

# Another Old Way
print("hello my name is {} and i am {} years old. My skill is {} and my rank is {:.2f}".format(name, age, skill, rank))

# New Way
print(f"hello my name is {name} and i am {age} years old. My skill is {skill} and my rank is {rank}")

# Formating for numbers 
number= 289469826538976
print(f"the number is {number:,}") # --> the number is 289,469,826,538,976
print("the number is {:_}".format(number)) # --> the number is 289_469_826_538_976

# Rearrange
a, b, c, = "one", "two", "three"
print ("hello {2} {1} {0}".format(a,b,c)) # --> hello three two one
#-----------------------------------------------------------------------------------------------------------
# Assignment Operators
# += , -= , *= , /= , **= , %= , //=
x= 5
x +=2
print(x) # --> 7

# Comparsion Operators
# >, <, <= , >=, ==, !=
print(100!=200)  # --> True
print(400 > 450) # --> False
#-----------------------------------------------------------------------------------------------------------
# Casting

# To string:
print(str(899)) # --> "899"

# To list:
print(list('osama')) # --> ['o', 's', 'a', 'm', 'a']
print(list((1, 2, 3, 4, 5))) # --> [1, 2, 3, 4, 5]
print(list({4, 5, 6})) # --> [5, 4, 6]
print(list({"a":1, "b":2, "c":3})) # --> ['a', 'b', 'c']

# To tuple
print(tuple("ahmed")) # --> ('a', 'h', 'm', 'e', 'd')
print(tuple([1, 2, 3, 4])) # --> (1, 2, 3, 4)
print(tuple({4, 5, 6})) # --> (4, 5, 6)
print(tuple({"a":1, "b":2, "c":3})) # --> ('a', 'b', 'c')

# To dictionary
dt= (("a", 1), ("b", 2), ("c", 3))
dl= [["x", 4], ["y", 5], ["z", 6]]
print(dict(dt)) # --> {'a': 1, 'b': 2, 'c': 3}
print(dict(dl)) # --> {'x': 4, 'y': 5, 'z': 6}
#-----------------------------------------------------------------------------------------------------------
# User Input
name= input("Type you name: ").capitalize().strip()
age = int(input("Type you age :"))
print(f"Hello {name}, your age is {age}")
#-----------------------------------------------------------------------------------------------------------
# if & elif & else Condition
age = 10

if age >= 18:
    print("You are an adult.")

elif age >= 13:
    print("You are a teenager.")

else:
    print("You are a child.")
# output : You are a child.
#-----------------------------------------------------------------------------------------------------------
# Short if Condition
movie_rate =18
age= 19
print('This movie is not good for you.' if movie_rate > age else "This movie is good for you.")
# output : This movie is good for you.
#-----------------------------------------------------------------------------------------------------------
# Nested if Condition
age = 20
is_student = True

if age >= 18:
    if is_student:
        print("You are an adult and a student.")

    else:
        print("You are and adult but not a student.")
else:
    print("You are a minor.")
# output: You are an adult and a student
#-----------------------------------------------------------------------------------------------------------
# Membership Operator
my_name= 'mostafa'
print('m' in my_name) # --> True
print('a' not in my_name) # --> False

my_lst= ["ahmed", "mahmoud", "osama"]
print("ahmed" in my_lst) # --> True
print("joe" not in my_lst) # --> True
#-----------------------------------------------------------------------------------------------------------
# While Loop
count =0 
while count < 5:
    print(f"Count is: {count}")
    count +=1
else:
    print("Loop has finished") #(Optional)
#-----------------------------------------------------------------------------------------------------------
# For Loop

# loop in list
fruits= ['apple', 'banana', 'kiwi']
for fruit in fruits:
    print(fruit) # --> apple\n banana\n kiwi

# loop is string
for letter in 'joe':
    print(f"[{letter}]") # --> [j] \n [o] \n [e]
#-----------------------------------------------------------------------------------------------------------
# loop in range
for num in range(5): # range (start, end[not included], step)
    print(num) # 0 \n 1 \n 2 \n 3 \n 4

# nested loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
#-----------------------------------------------------------------------------------------------------------
# loop for dictionaries
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78}

for student, score in student_scores.items():
    print(f"{student}: {score}")
#-----------------------------------------------------------------------------------------------------------
# Break & Continue & pass

# Break: exits the loop immediately, ending its executfor i in range(10):
for i in range(10):
    if i == 5:
        break
    print(i) # --> 0 \n 1 \n 2 \n 3 \n 4

# Continue: skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
for i in range(5):
    if i == 2:
        continue
    print(i) # --> 0 \n 1 \n 3 \n 4

# Pass: Does nothing; acts as a placeholder in loops, functions, or classes where code is required syntactically but you don’t want any action to be performed.
for i in range(5):
    if i == 2:
        pass
    else:
        print(i) # --> 0 \n 1 \n 3 \n 4
#-----------------------------------------------------------------------------------------------------------