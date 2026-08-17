# Common Python Errors
"""
These are some of the most frequent errors (exceptions) you'll run into in Python:

1. SyntaxError        - The code is written incorrectly and Python can't even
                        parse it (e.g. missing colon, unmatched parenthesis).

2. IndentationError   - Inconsistent or missing indentation (Python relies on
                        indentation to define code blocks).

3. NameError           - Using a variable or function that hasn't been defined
                        yet, or is misspelled.

4. TypeError            - An operation is applied to the wrong data type
                        (e.g. adding a string and an integer: "2" + 2).

5. ValueError           - The type is correct, but the value itself is invalid
                        (e.g. int("hello") - "hello" isn't a valid number).

6. IndexError           - Trying to access a list/tuple index that doesn't
                        exist (e.g. mylist[10] when mylist only has 3 items).

7. KeyError             - Trying to access a dictionary key that doesn't exist.

8. AttributeError       - Calling a method or accessing an attribute that
                        doesn't exist on that object (e.g. "hello".append()).

9. ZeroDivisionError     - Dividing a number by zero (e.g. 5 / 0).

10. ImportError / ModuleNotFoundError - Trying to import a module/function
                                        that doesn't exist or isn't installed.

11. FileNotFoundError    - Trying to open a file that doesn't exist at the
                          given path.
"""

#-----------------------------------------------------------------------------------------------------------
# Exception and Errors
x= -10
if x <0:
    raise Exception("this number is less than zero")

# ValueError:
y= 'osama'
if type(y) != int:
    raise ValueError('only numbers allowed')
#-----------------------------------------------------------------------------------------------------------
# Exceptions Handling (try, except, else, finally)
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution complete.")

# Test cases
divide(10, 2)  # Normal division -----> The result is: 5.0 \n  Execution complete.
divide(10, 0)  # Division by zero ------> Error: Cannot divide by zero! \n  Execution complete

#-----------------------------------------------------------------------------------------------------------
# File Handling

# r : read the file
# r+ : read and write (Better one)
# rb : read binary files
# w : overwrite on the file and if the doesn't exist, it creates it
# wb : writes binary
# a : append the data to the file and it doesn't create a file
# ab: append binary
# x : creates the file
with open(r"Files\ahmed_file.txt", mode='r', encoding='utf-8') as file:
    print(file) # --> shows file data object
    print(file.name) # --> shows the path on name of the file
    print(file.mode) # --> shows the mode of the file
    print(file.encoding) # --> show the encoding of the file

    print(file.read()) # reads all the content of the file
    print(file.read(5)) # reads the number of specific characters of the file
    print(file.readline()) # reads the first line 
    print(file.readline()) # reads the second line 
    print(file.readlines()) # converts every line to an element in a list
    print(file.close()) # close the file


with open(r"Files\example_txt.txt", mode='w', encoding='utf-8') as new_file:
    new_file.write("Hello my name is ahmed\nI have 19 years old\nI love Python")
    new_file.write("\nI love cheese and my friends:\n")
    new_file.writelines(['dalia\n', 'mariem\n', 'mohmoud\n'])

with open(r"Files\example_txt.txt", mode='r+', encoding='utf-8') as file:
    # truncate(): Used to resize the file to specific size of characters: ex: Hello world --> Hello
    file.truncate(5)

    # tell(): returns the current file position, which is the byte offset from the beginning of the file.
    # It's useful for determining where you are in the file after reading or writing.
    print(file.tell())

    # seek(): Used to change the file's current position. You can move to a specific location in the file for reading or writing.
    file.seek(6)
    print(file.read())
#---------------------------------------------------------------------------------------------
# Read CSV files (Comma seperated values)
import csv

with open(r"Files\example_csv.csv", mode='r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file) # read the csv file
    next(csv_reader)                  # skip the headers
    for line in csv_reader:
        print(line)                   # show the csv line

# sample data
data = [
    ['mostafa', '22', 'morroco'],
    ['alisa', '25', 'germany'],
    ['alice', '21', 'england']
]

with open(r"Files\example_csv.csv", mode='w', encoding='utf-8', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file) # read the csv file to overwrite
    for row in data:
        csv_writer.writerow(row)          # overwrite the csv file
#----------------------------------------------------------------------------------------
with open(r"Files\example_csv.csv", mode='w', encoding='utf-8', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file, delimiter='\t') # read the csv file to overwrite data with dellimter \t
    for row in data:
        csv_writer.writerow(row)

with open(r"Files\example_csv.csv", mode='r', encoding='utf-8', newline='') as file:
    csv_reader = csv.reader(file, delimiter='\t')
    for line in csv_reader:
        print(line)
#--------------------------------------------------------------
# Read Json Files (JavaScript-Seperated Notation)
import json

x = '{ "name":"John", "age":30, "city":"New York", "married": true, "Grades": [55, 34, 12]}' # --> # JSON string
print(json.loads(x)) # --> Converts JSON string to python dictionary (from javascript language to python language ex: true to True)

# Convert a Python object containing all the legal data types to Json string:
z = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(z))
#------------------------------------------
with open(r"Files\example_json.json", mode='r', encoding='utf-8') as json_file:
    data = json.load(json_file)
for item in data:
    print(f'"name": {item['name']}, "age": {item['age']}, "country": {item['country']}')


data = {"name": "omar", "age":28, 'city':"Giza"}
with open(r"Files\example_json.json", mode='w', encoding='utf-8') as new_json_file:
    json.dump(data, new_json_file, indent=4, sort_keys=True)