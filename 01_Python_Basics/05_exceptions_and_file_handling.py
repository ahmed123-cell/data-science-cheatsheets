"""
Python Exception Handling and File Handling: a study reference.

Topics covered:
    common exceptions, raising exceptions, try / except / else / finally,
    file modes, reading and writing text files, CSV files, and JSON files.

Before running, create a "Files" folder next to this script containing:
    example_txt.txt     any text file (read in the text-file section)
    example_csv.csv    a CSV file with a header row and comma-separated rows
    example_json.json  a JSON list of objects, each with "name", "age", "country"
NOTE: the script overwrites example_txt.txt, example_csv.csv, and example_json.json.

Expected output is shown in "# -->" comments.
"""

import csv
import json
from pathlib import Path

# Works on every operating system (no hard-coded "\" or "/" in the file names)
FILES_DIR = Path("Files")


#========================
# COMMON PYTHON ERRORS (EXCEPTIONS)
#========================
# SyntaxError          : code is written incorrectly and cannot be parsed
#                        (missing colon, unmatched parenthesis).
# IndentationError     : missing or inconsistent indentation (a kind of SyntaxError).
# NameError            : using a variable/function that is not defined or is misspelled.
# TypeError            : operation on the wrong data type, e.g. "2" + 2.
# ValueError           : correct type but invalid value, e.g. int("hello").
# IndexError           : list/tuple index that does not exist, e.g. my_list[10].
# KeyError             : dictionary key that does not exist.
# AttributeError       : method/attribute that does not exist, e.g. "hello".append().
# ZeroDivisionError    : dividing by zero, e.g. 5 / 0.
# ImportError / ModuleNotFoundError : module or name that does not exist or is not installed.
# FileNotFoundError    : opening a file that does not exist at the given path.


#========================
# RAISING EXCEPTIONS
#========================
# raise stops the program with an error unless it is caught with try / except.
# (Each raise is wrapped in try / except here so the rest of the file can run.)
number = -10
try:
    if number < 0:
        raise Exception("this number is less than zero")
except Exception as error:
    print(f"Exception: {error}")  # --> Exception: this number is less than zero

value = 'osama'
try:
    if not isinstance(value, int):  # preferred over: type(value) != int
        raise ValueError('only numbers allowed')
except ValueError as error:
    print(f"ValueError: {error}")  # --> ValueError: only numbers allowed


#========================
# EXCEPTION HANDLING: TRY / EXCEPT / ELSE / FINALLY
#========================
# try     : code that might fail
# except  : runs only if the matching error occurs
# else    : runs only if NO error occurred
# finally : always runs (useful for cleanup)
def divide(x, y):
    """Divide x by y and report the result or the error."""
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    else:
        print(f"The result is: {result}")
    finally:
        print("Execution complete.")


divide(10, 2)
# --> The result is: 5.0
#     Execution complete.

divide(10, 0)
# --> Error: Cannot divide by zero!
#     Execution complete.


#========================
# FILE MODES
#========================
# r  : read (the file must exist)
# r+ : read and write (the file must exist; nothing is erased on opening)
# rb : read binary files
# w  : write; overwrites the file, and creates it if it does not exist
# wb : write binary
# a  : append to the end of the file; creates it if it does not exist
# ab : append binary
# x  : create a new file; raises an error if it already exists
#
# Always open files with "with": it closes the file automatically.


#========================
# READING A TEXT FILE
#========================
with open(FILES_DIR / "example_txt.txt", mode='r', encoding='utf-8') as file:
    print(file)           # --> <_io.TextIOWrapper name='Files/ahmed_file.txt' mode='r' encoding='utf-8'>
    print(file.name)      # --> the file path, e.g. Files/ahmed_file.txt
    print(file.mode)      # --> r
    print(file.encoding)  # --> utf-8

    # Reading moves the file position forward, so we go back with seek(0)
    # before each example. Without it, a second read() would return ''.
    print(file.read())      # whole content of the file
    file.seek(0)
    print(file.read(5))     # only the first 5 characters
    file.seek(0)
    print(file.readline())  # first line
    print(file.readline())  # second line (reading continues from where it stopped)
    file.seek(0)
    print(file.readlines())  # list where every line is an element


#========================
# WRITING A TEXT FILE
#========================
# write() writes a string; writelines() writes every string of a list
# (neither adds "\n" for you).
with open(FILES_DIR / "example_txt.txt", mode='w', encoding='utf-8') as new_file:
    new_file.write("Hello my name is ahmed\nI have 19 years old\nI love Python")
    new_file.write("\nI love cheese and my friends:\n")
    new_file.writelines(['dalia\n', 'mariem\n', 'mohmoud\n'])


#========================
# TRUNCATE, TELL, AND SEEK
#========================
with open(FILES_DIR / "example_txt.txt", mode='r+', encoding='utf-8') as file:
    # truncate(size): cut the file down to `size` characters (permanently).
    # Example: "Hello world" --> "Hello". The file now contains just "Hello".
    file.truncate(5)

    # tell(): current position in the file, counted from the beginning.
    # truncate() does not move the position, so it is still at the start.
    print(file.tell())  # --> 0

    # seek(position): move the current position to read or write from there.
    # Position 6 is past the end of "Hello", so there is nothing left to read.
    file.seek(6)
    print(file.read())  # --> (an empty line)


#========================
# CSV FILES: READING
#========================
# CSV = Comma-Separated Values. Use newline='' so the csv module controls line endings.
with open(FILES_DIR / "example_csv.csv", mode='r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip the header row
    for row in csv_reader:
        print(row)    # --> one list per row, e.g. ['mostafa', '22', 'morroco']


#========================
# CSV FILES: WRITING
#========================
csv_rows = [
    ['mostafa', '22', 'morroco'],
    ['alisa', '25', 'germany'],
    ['alice', '21', 'england'],
]

# mode='w' overwrites the whole file. The csv writer wraps the open file.
with open(FILES_DIR / "example_csv.csv", mode='w', encoding='utf-8', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file)
    csv_writer.writerows(csv_rows)  # same as calling writerow() for every row


#========================
# CSV FILES: CUSTOM DELIMITER
#========================
# The delimiter must be the same when writing and when reading.
with open(FILES_DIR / "example_csv.csv", mode='w', encoding='utf-8', newline='') as new_csv_file:
    csv_writer = csv.writer(new_csv_file, delimiter='\t')  # tab-separated
    csv_writer.writerows(csv_rows)

with open(FILES_DIR / "example_csv.csv", mode='r', encoding='utf-8', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        print(row)
# --> ['mostafa', '22', 'morroco']
#     ['alisa', '25', 'germany']
#     ['alice', '21', 'england']


#========================
# JSON: STRING <--> PYTHON OBJECT
#========================
# JSON = JavaScript Object Notation.
# json.loads(): JSON string --> Python object (true --> True, null --> None...)
json_string = '{ "name":"John", "age":30, "city":"New York", "married": true, "Grades": [55, 34, 12]}'
print(json.loads(json_string))
# --> {'name': 'John', 'age': 30, 'city': 'New York', 'married': True, 'Grades': [55, 34, 12]}

# json.dumps(): Python object --> JSON string (True --> true, None --> null,
# tuple --> array)
person = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1},
    ],
}
print(json.dumps(person))
# --> {"name": "John", "age": 30, "married": true, "divorced": false,
#      "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230",
#      "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}   (printed on one line)


#========================
# JSON FILES: READING
#========================
# json.load(): read a JSON file --> Python object (here: a list of dictionaries)
with open(FILES_DIR / "example_json.json", mode='r', encoding='utf-8') as json_file:
    people = json.load(json_file)

for item in people:
    # Use different quotes inside the f-string (works on every Python version)
    print(f'"name": {item["name"]}, "age": {item["age"]}, "country": {item["country"]}')
    # --> "name": <name>, "age": <age>, "country": <country>


#========================
# JSON FILES: WRITING
#========================
# json.dump(): Python object --> JSON file
# indent=4 makes it readable; sort_keys=True orders the keys alphabetically.
new_person = {"name": "omar", "age": 28, 'city': "Giza"}
with open(FILES_DIR / "example_json.json", mode='w', encoding='utf-8') as new_json_file:
    json.dump(new_person, new_json_file, indent=4, sort_keys=True)
# The file now contains:
# {
#     "age": 28,
#     "city": "Giza",
#     "name": "omar"
# }