# String Methods

# len(): count the number of characters in the string or any data type except integer
print(len('programming')) # --> 11

# strip(): remove white spaces or any character from the beginning and the end of the string
print('         hello world      '.strip()) # --> hello world
print("@@@@@@@@@@@@hello world@@@@@@@@@@@@@@@".strip('@')) # --> hello world

# title(): capitalize the first letter of each word and make the letter after the number or special character capital
print('i love python and 4g graphics and @gmail'.title()) # --> I Love Python And 4G Graphics And @Gmail

# capitalize(): capitalize the first letter of the string
print("i love python and 4g graphics and @gmail".capitalize()) # --> I love python and 4g graphics and @gmail

# zfill(): fill the string with zeros from the left side to make the string length equal to the number inside the function
print('5'.zfill(3)) # --> 005
print("53".zfill(3)) # --> 053

# upper(): make all the letters in the string capital
print("i love html".upper()) # --> I LOVE HTML

# lower(): make all the letters in the string small
print("I LOVE HTML".lower()) # --> i love html

# split() and rsplit(): split the string into a list of strings
print("i love python and html".split()) # --> ['i', 'love', 'python', 'and', 'html']
print("i-love-python-and-html".split("-",3)) # --> ['i', 'love', 'python', 'and-html']
print("i-love-python-and-html".rsplit("-",3)) # --> ['i-love', 'python', 'and', 'html']

# center(): center the string in the middle of the number inside the function
print("i love python".center(21, "#")) # --> ####i love python####

# count(): count the number of the word inside the string
print("i love python and html".count("python")) # --> 1

# swapcase(): make the capital letters small and the small letters capital
print("i LOve PYthon".swapcase()) # --> I loVE pyTHON

# replace(): replace the word inside the string with another word
print("i love python and html".replace("python", "java")) # --> i love java and html

# find(): find the index of the word inside the string. it will give -1 if the word is not found
print("i love python and html".find("p")) # --> 7

# index(): find the index of the word inside the string. it will give an error if the word is not found
print("i love python and html".index("p")) # --> 7

# startswith(): check if the string starts with the word inside the function
print("i love python and html".startswith("i")) # --> True

# endswith(): check if the string ends with the word inside the function
print("i love python and html".endswith("html")) # --> True

# splitlines(): split the string into a list of strings
print("i love python\nand html".splitlines()) # --> ['i love python', 'and html']

# __contains__(): check whether a specific element exists in a collection or not.
print("i love python and html".__contains__('python')) # --> True

# isalnum(): check if the string contains only letters and numbers
print("ilovepython".isalnum()) # --> True

# isalpha(): check if the string contains only letters
print("ilovepython".isalpha()) # --> True

# isdigit(): check if the string contains only numbers
print("12345".isdigit()) # --> True
#-----------------------------------------------------------------------------------------------------------
# list methods

# append(): add an element to the end of the list
list1= [1, 2, 3]
list1.append(4)
print(list1) # --> [1, 2, 3, 4]

# extend(): add a list to the end of the list
list1= [1, 2, 3]
list1.extend([5, 6, 7])
print(list1) # --> [1, 2, 3, 5, 6, 7]

# remove(): remove an element from the list
list1= [1, 2, 4]
list1.remove(4)
print(list1) # --> [1, 2]

# sort(): arrange the elements by number or alphabet
list1= [5, 2, 3]
list1.sort()
print(list1) # --> [2, 3, 5]

# reverse(): reverse the arrange of elements
list1= [4, 5, 6]
list1.reverse()
print(list1) # --> [6, 5, 4]

# clear(): clear all item in list
list1= [1, 2, 3]
list1.clear()
print(list1) # --> []

# copy(): create copied list from list
list1= [1, 2, 3]
list2= list1.copy()
print(list2) # --> [1, 2, 3]

# count(): count the number of the elements inside the list
list1= [1, 1, 4, 1]
print(list1.count(1)) # --> 3

# index(): find the index of an element inside the list
list1= [1, 2, 3, 4]
print(list1.index(1)) # --> 0

# insert(): add an element to a list at a specific index
list1= [1, 3, 4]
list1.insert(1, 2) # --> [1, 2, 3, 4]

# pop(): return the last element in the list
list1= [1, 2, 3, 4]
print(list1.pop()) # --> 4
print(list1.pop(2)) # --> 3 (the number refers the index of returned element)
print(list1) # --> [1, 2] (returns the new list after removing or popping 3 and 4)
#-----------------------------------------------------------------------------------------------------------
# Sets methods
# Set: an unordered collection of unique(no duplicates) elemnts

# clear(): clear all elements in the set
set1= {1, 2, 3}
set1.clear()
print(set1) # --> {}

# union(): combine two or more sets into one set
set1= {"one", "two", "three"}
set2= {"four", "five", "six"}
print(set1.union(set2)) # --> {"two", "four", "five", "three", "six", "one"}
print(set1 | set2) # --> {"two", "four", "five", "three", "six", "one"}

# intersection(): retruns the elemnts that are common in all sets
set1= {"one", "two", "three"}
set2= {"three", "four", "five"}
print(set1.intersection(set2)) # --> {"three"}
print(set1 & set2) # --> {"three"}

# add(): add one element to the set
set1= {1, 2, 3}
print(set1.add(6)) # --> {1, 2, 3, 6}

# discard(): remove an element from the set
set1={1, 2, 3}
print(set1.discard(3)) # --> {1, 2}

# difference(): return the elements that are present in one set but no in another
set1= {1, 2, 3, 4}
set2= {3, 4, 5, 6}
print(set1.difference(set2)) # --> {1, 2}
print(set1 - set2) # --> {1, 2}

# symmentric_difference(): retrun the elements that are either of the two sets but not in both
set1= {1, 2, 3}
set2= {2, 3, 4}
print(set1.symmetric_difference(set2)) # --> {1, 4}
print(set1 ^ set2) # --> {1, 4}

# pop(): return a random element in the set
set1= {3, 7, 1, 9, 5}
print(set1.pop()) # --> 7

# issuperset(): check if the set contains all the elements of another set.
set1= {1, 2, 3, 4, 5}
set2= {2, 4}
print(set1.issuperset(set2)) # --> True

# issubset(): check if the another set contains all the elements of one set !!(reverse of superset)!!
set1= {1, 2}
set2= {1, 2, 3}
print(set1.issubset(set2)) # --> True

# isdisjoint(): check if two sets have any elements in common
set1= {1, 2, 3}
set2= {4, 5, 6}
print(set1.isdisjoint(set2)) # --> True
#-----------------------------------------------------------------------------------------------------------
# Dictionary
dict1= {"name": "ahmed", "age": 18, "skills":["python", "html"]}
print(dict1["name"]) # --> ahmed
print(dict1.get("name")) # --> ahmed

# two dimensional dictionary
language ={"one":{"name":"HTML","Progress":"80%"},"two":{"name":"Python", "progress":"50%"},"three":{"name":"CSS", "progress":"50%"}}
print(language["one"]) # --> {"name": "HTML", "progress": "80%"}
print(language["three"]["progress"]) # --> 50%
#-----------------------------------------------------------------------------------------------------------
# Dictionary methods

# keys(): returns all key in the dictionary
dict1= {"name": "ahmed", "age": 18, "skills":["python", "html"]}
print(dict1.keys()) # --> dict_keys(['name', 'age', 'skills'])

# values(): returns all values in the dictionary
dict1= {"name": "ahmed", "age": 18, "skills":["python", "html"]}
print(dict1.values()) # --> dict_values(['ahmed', 18, ['python', 'html']])

# clear(): clear all elements in the dictionary
dict1= {"name": "ahmed", "age": 18, "skills":["python", "html"]}
print(dict1.clear()) # --> None

# update(): modify existing key-value pairs or add new ones to a dictionary
dict1= {"a": 1, "b": 2}
dict1.update({"b": 3, "c": 4})
print(dict1) # --> {"a": 1, "b": 3, "c": 4}

# setdefault(): returns the value associated the key regardless of whether the key existed or was created
dict1= {"name": "ahmed"}
print(dict1.setdefault("name", "osama")) # --> ahmed
print(dict1.setdefault("age", 19)) # --> 19

# popitem(): returns the last key with its value 
dict1= {"rank": "perfect", "oop": "required"}
print(dict1.popitem()) # --> {"oop": "required"}

# fromkeys(): create new dictionary with a specified set of keys and a default value
keys= ("one", "two", "three")
value= "x"
print(dict.fromkeys(keys, value)) # --> {'one': 'x', 'two': 'x', 'three': 'x'}