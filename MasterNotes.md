# An Overview of all notes organised into topics

## For more examples check examples.py of each folder

## Table of Contents
- [Install and Setup for Mac and Windows](#1---install-and-setup-for-mac-and-windows)
- [Strings, Working with Textual Data](#2---strings--working-with-textual-data)
- [Integers and Floats – Working with Numeric Data](#3-integers-and-floats---working-with-numeric-data)
- [Lists, Tuples, and Sets](#4-lists-tuples-and-sets)
- [Dictionaries - Working with Key-Value Pairs](#5-dictionaries---working-with-key-value-pairs)
- [Conditions - If elif and else](#6-conditions---if-elif-and-else-statements)
- [Loops and Iterations - For loops and while loops](#7-loops-and-iterations---for-loops-and-while-loops)
- [Functions](#8-functions)
- [Modules and Standard Library](#8---modules-and-standard-library)
- [OS Module - Use Underlying Operating System Functionality](#10--os-module---use-underlying-operating-system-functionality)
- [File Objects - Reading and Writing to Files](#11---file-objects---reading-and-writing-to-and-from-files)
- [How to Set the Path and Switch Between Different Versions](#12---how-to-set-the-path-and-switch-between-different-versions)
- [How to Set the Path and Switch Between Different Versions - Mac & Linux version](#13---how-to-set-the-path-and-switch-between-different-versions)
- [Automate Parsing and Renaming of Multiple Files](#14---Automating-renaming-files)

# 1 - Install and Setup for Mac and Windows

### Overview
Notes about checking the Python version and installing Python on Windows.

### Key Concepts
- Checking Python version
- Installing Python on Windows

### Important Details
> Running Python in PowerShell/cmd allows you to interact with its built-in one-line interactive prompt.

### Examples
- Check Python version:
  ```bash
  python --version
  ```



# 2 - Strings , Working with Textual Data

### Overview
Notes for manipulating strings 

### Key Concepts
- Concatenation
  - fstrings is f"{greeting.upper()}, {name} , Welcome!"
  - fstrings are more readable and usable than standard concatenation methods
- String maniplation
  - .upper() turns the whole text upper cased
  - .lower() turns the whole text lower cased

### Important details
> Use help for extra info , e.g. print(help(str))  
> Use dir to list all possible methods e.g. print(dir(str))

### Examples
- fstrings :
  ```python
  message_fstring = f"{greeting.upper()}, {name} , Welcome!" # Using f-strings
  ```
- Standard Concatenation using + operator:
  ```python
  message_concat = greeting + ", " + name + " , Welcome!" # Same thing but less readable
  ```



# 3: Integers and Floats - Working with Numeric Data

### Overview
Notes covering basic numeric operations in Python, including arithmetic operators, comparisons, and commonly used built-in functions.

### Key Concepts
- Odd and even numbers can be identified using `% 2`
- `abs()` returns the absolute value of a number
- Casting can be done using `int()`
- Arithmetic operators perform mathematical calculations
- Comparison operators compare values and return booleans

### Important Details
> `%` returns the remainder of a division.  
> `abs()` always returns a non-negative number.  
> `/` always returns a float.  
> `//` performs floor division and rounds down.  
> Comparison operations return `True` or `False`.

### Examples
- Odd / Even check:
  ```python
  num = 5
  num % 2 == 1
  ```



# 4: Lists, Tuples, and Sets

### Overview
Notes of lists tuples and sets and their functions

### Key Concepts
- len() prints how many values/index there are.
- courses[0] returns the first index of the list
- Negative index allows it to count from the end
- Append adds items to existing list
- .pop() removes last index , can be stored in a variable
- Insert allows more precise append
- .reverse() reverses the whole list
- .sort() sorts a list alphabetically or ascending order
- .sort(reverse=True) sorts a list in descending order and not alphabetical order
- Tuples are similar to lists except theyre **Immutable**
- sum(nums) returns the sum of all numbers
- max(nums) returns the largest number
- min(nums) returns the smallest number

### Important Details
> Lists are mutable, meaning their contents can be changed after creation.  
> Tuples are immutable and cannot be modified once created.  
> Negative indexing starts from -1 at the last element.  
> `.sort()` modifies the list in place and returns `None`.  
> `.reverse()` also modifies the list in place.  
> Sets do not allow duplicate values and are unordered.

### Examples
- Min, Max and Sum:
  ```python
  print(min(nums)) # min(nums) returns the smallest number
  print(max(nums)) # max(nums) returns the largest number
  print(sum(nums)) # sum(nums) returns the sum of all numbers
  ```

- Number list sorting:
  ```python
  nums.sort() # Sorts it in ascending order
  nums.sort(reverse=True) # Sorts it in descending order
  ```

- List:
  ```python
  print(len(courses)) # len() prints how many values/index there are.
  print(courses[0])  # courses[0] returns the first index of the list
  print(courses[-1]) # Negative index allows it to count from the end
  ```

# 5: Dictionaries - Working with Key-Value Pairs

### Overview
How to use dictionaries and when to use them.

### Key Concepts
- Dictionaries are created with {}
- .update allows you to overwrite old data but also keep unchanged data.
- You can directly change values with e.g. student['name'] = 'Joe'
- del deletes a key-value from a dictionary
- student.items() prints out the key-value pair

### Important Details
> Dictionaries can be used to store list, much like a spreadsheet row
### Examples
- Printing out a table of values using loop and fstring:
  ```python
    for x,value in student.items():
        value = str(value)
        print(f"{x.upper()} : {value.upper()}") # Applied fstring knowledge , this displays a good looking table of values
- Updating a dictionary:
  ```python
    student.update({'name': 'John', 'age': '25'})
- Printing a key-value pair:
  ```python
    print(student.items())


# 6: Conditions - If elif and else statements  

### Overview
How to use if elif and else statements , also some false values to look out for , also , and or and not
### Key Concepts
## Comparisons:
- Equal:            ==
- Not Equal:        !=
- Greater Than:     >
- Less Than:        <
- Greater or Equal: >=
- Less or Equal:    <=
- Object Identity:  is


## False Values:
- False
- None
- Zero of any numeric type
- Any empty sequence. For example, '', (), [].
- Any empty mapping. For example, {}.

### Important Details
> Look out for 0s because you might not want it to return false when value is 0 sometimes
### Examples
- If , elif and else with != , and in one code:
  ```python
    value = "water"
    if value == 'water' and value != "fire":
        print("Value is water")
    elif value != "water":
        print("Value is not water")
    else:
        print("Error")

# 7: Loops and Iterations - For loops and while loops.

### Overview

How to use for and while loops
## Key Concepts

### For loops:
- For i in range(10): allows you to loop 10 or a set times.
- For value in list: allows you to loop however many childrens there are in the list
### While loops:
- While loops continues a loop until the statement is true
- While True loops continues forever so use a break or else it will crash eventually

### Important Details
> While True loops continues forever so use a break or else it will crash eventually
### Examples
- for loop with a if else statement:
  ```python
    for numbers in number: # Looping through however many numbers there are
        if numbers == 5:
            print("Found!", numbers) # This filters out 5s and say Found if theyre a 5
        else:
            print(numbers)

# 8: Functions 

### Overview
How to define functions , use them and what are kwargs and args
## Key Concepts
- Functions are used to make sure you don't repeat yourself
- They're useful because they allow parameters
- Parameters are basically inputs for the function
- use def to make a function
- functionname() to call the function
- use **kwargs for mappings/dictionaries

### Important Details
> Functions allows modular codin
### Examples
- A script that identifies if inputted year is leap, then take a month, then tells you the amount of days it has , with an exception that februrary has more processing :
  ```python
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_names = ["placeholder","January","February","March","April","May","June","July","August","September","October","November","December"]
    year = input("Enter year : ")
    year = int(year)
    month = input("Enter month : ")
    month = int(month)
    def is_leap(year):
        """Return True for leap years, False for non-leap years."""
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0),"is"
        else:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0),"is not"
    is_leap_year, text = is_leap(year)

    def days_in_month(year, month):
        """Return number of days in that month in that year."""

        # year 2017
        # month 2
        if not 1 <= month <= 12:
            return 'Invalid Month'

        if month == 2 and is_leap_year:
            return 29

        return month_days[month]



    print(f"The year is {year}, which {text} a leap year, therefore there is {days_in_month(year,month)} days in {month_names[month]}")

# 8 : Modules and Standard library

### Overview

How to use modules and some standard libraries
## Key Concepts

### Modules
- Use modules to look more clean
- import modules using import or from module import function
- modules can be grabbed from other directories
### Standard Libraries
- Standard libraries include math,calendar,os,datetime and much more
- e.g. Math library allows calculations like sin
- OS allows more compilcated controls on operating system , more detail on next video
- calendar allows functions like isleap()
- datetime allows you to grab date and time of today for example

### Important Details
> Use libraries to simplify your code , use module to make it more readable.
### Examples
- Import maths and use sin:
  ```python
    import math
    print(math.sin(90))
- Import datetime and grab today's date:
  ```python
    import datetime
    print(datetime.date.today())

# 10 : OS Module - Use Underlying Operating System Functionality

### Overview
How to use the OS module
## Key Concepts
### directories
- Use .chdir() to change working directory
- Use .getcwd() to get the working directory
- Use .mkdir() or makedirs() to make one or more directory and sub-directories for makedirs()
- Use .rmdir() or removedirs() to remove one or more directory and sub-directories for removedirs()
## Files
- Use .rename(<from>,<to>) to rename files or directories
- Use .stat() to list file properties
- Use .walk(<>) to walk through directories , this is useful for searching
- use .environ to get enviroment variables.
## Manipulation
- os.path.join() allows you to join paths without worrying about the extra / or not
- os.path.basename gets basename
- os.path.dirname gets dir name
- os.path.split() splits a path
- dir(os) 

### Important Details
> Use os module to edit files , directories of anything
> You wont remember everything , so use print(dir(os))
### Examples
- All commands in video:
  ```python
    os.getcwd()                       # get current working directory
    os.chdir(<path>)                                    # change directory 
    os.listdir()	                                            # list directory
    os.mkdir(<dirname>)                           # create a directory
    os.makedirs(<dirname>)                    # make directories recursively
    os.rmdir(<dirname>)	                   # remove directory
    os.removedirs(<dirname>)                # remove directory recursively
    os.rename(<from>, <to>)                   # rename file
    os.stat(<filename>)                            # print all info of a file
    os.walk(<path>)	                          # traverse directory recursively
    os.environ		                                 # get environment variables
    os.path.join(<path>, <file>)              # join path without worrying about /
    os.path.basename(<filename>)     # get basename
    os.path.dirname(<filename>)         # get dirname
    os.path.exists(<path-to-file>)         # check if the path exists or not
    os.path.splitext(<path-to-file>)      # split path and file extension
    dir(os)			                               # check what methods exists
# 11 - File Objects - Reading and writing to and from files

### Overview
How to manipulate file objects
## Key Concepts
### Modes
- 'r' for read file contents.
- 'w' for writing to files contents.
- 'a' for appending to files contents.
- 'r+' for read + write to files contents.
- 'b' for opening files in binary mode ( Images ).
> We can use different modes together like 'rb' can be used for reading a binary file
### Reading from files.
- file.close() for closing a file 
- file.mode returns mode the file was opened in
- file.name returns name of the file as a string
> Context managers are for effiency and organisation 
- file.read([size]) - typically used to read content of a file but when provided with <size> , it can read only the 'size'/ number of character , can be used repeatedly and it will continue off where it left off

- file.readlines() returns a list off all the lines of the file.
- file.readline() returns a single line
### Writing to files
- file.tell() returns the position of where the pointer is
- file.seek(new_position) changes the pointer's position to the specified
- file.write(content)  writes the contents to the file.
### Important Details
> trying to write to a file that does not exist will first create the file and then perform the writing operation.
> A file is treated as an iterable in python. This simply means that we can iterate over the lines of the file using a for loop (like we would loop over the elements of a list).
### Examples
- Repeating reading a file of specified size until reaches 0:
  ```python
    size = 10                              
    fileContents = file.read(size)

    while len(fileContents) > 0:     # while the length of what we have read is not 0, continue reading
        print(fileContents, end=('')
        fileContents = file.read(size)
- Using context managers to simultaneously read from a file and write to another:
  ```python
    with open("readFilePath", 'r') as readFile:
        with open("writeFilePath", 'w') as writeFile:
            _for line in readFile:
                _writeFile.write(line)
    #OR
    with open("readFilePath", 'r') as readFile:
        with open("writeFilePath", 'w') as writeFile:
            writeFile.write(readFile.read())
# 12 - How to set the Path and switch between different versions
### Overview
How to change enviroment variable to correct python version and do same for pip
## Key Concepts
### Changing Enviroment variables on windows
- system settings -> view advanced settings -> enviroment variables
- Change enviroment variable to the correct python version
- Do the same for pip
### Important Details
> pip can be done the same , it is in similar directory
> Python default directory varies
# 13 - How to set the Path and switch between different versions - Mac
### Overview
This tutorial is exact same but for Mac/Linux which I don't really use python on 

# 14 - Automating renaming files

### Overview
How to automate file renaming, I used one of my folders that contained messy CAD .step files as example
## Key Concepts
### Striping and cleaning files
- use os.path.splitext(f) to split extension from a file
- use f.strip() to remove empty white spaces
- use zfill(2) to pad numbers , like from 2 to 02
### Other useful commands when automating file renaming
- os.rename(f,new_name) to actually rename it
- use fstrings to construct a new name for file
### Important Details
> Automating renaming files are very useful when folders are large and messy , they save a lot of time
### Examples
- Using os module, and a for file loop to rename my .step files to "XLTimmingBeltPulley_{teeth}Teeths{ext}"
  ```python
    import os,re
    os.chdir("/Users/chung/OneDrive/Documents/CADmodels/XLTimingBeltPulley_4-24teeths")
    print(os.getcwd())
    FOLDER = os.getcwd()
    for f in os.listdir(FOLDER):
        old_path = os.path.join(FOLDER, f)
        print("old_path : ",old_path)
        if not os.path.isfile(old_path):
            continue

        name, ext = os.path.splitext(f)

        match = re.search(r"\d+", name)
        if not match:
            print(f"Skipping (no number): {f}")
            continue

        teeth = match.group().zfill(2)

        new_name = f"XLTimingBeltPulley_{teeth}Teeths{ext}"
        new_path = os.path.join(FOLDER, new_name)

        print(f"{f}  ->  {new_name}")
        os.rename(old_path, new_path)

        

# Practices

## 12-18-2025
```python
answer = 'y'

while answer == 'y':
  name = input("Enter name of student : ")
  age = int(input(f"Enter {name}'s age : "))
  courses = input(f"Enter {name}'s courses seperated by a space : ")
  courses = courses.split(" ")
  student = {'Name': name,'Age': age,'Courses': courses}
  for x, value in student.items():
    if isinstance(value, list):
      value = ", ".join(value)
    else:
      value = str(value)
    print(f"{x} : {value}")
  answer = input("\n Would you like to add another student? (Y/N) : ").lower()
else:
  print("Bye!")
```
- An example use of **dictionaries** to store multiple types of data , e.g. student's profile
- Loops until user decides to stop inputting students using **while**
## 12-23-2025
```python
name = input("Please enter your name : ")
age = int(input("Please enter your age : "))
while age <= 0:
        age = int(input("Please enter a valid age : "))
answer = "y"
numlist = []
while answer == "y":
    FavNum = int(input("Please enter your favorite number : "))
    answer = input("Would you like to add another favorite number (Y/N) : ").lower()
    numlist.append(FavNum)
    print(numlist)
profile = {"Name":name,"Age":age, "FavoriteNumber":numlist}
def isodd(num):
      if num % 2 == 0:
            return("even")
      else:
            return("odd")
print(f"Hello {profile['Name']}!\nYour age is an {isodd(profile["Age"])} number!\nFavorite Numbers Summary : \nSmallest: {min(numlist)}\nLargest: {max(numlist)}\nSum : {sum(numlist)}")
```
- This is a code for profile creation via loops and inputs
- An example use of functions ( determining odd numbers )
- An example use of fstrings, list and type casting
## 12-24-2025
```python
odd = 0
even = 0
with open("numbers.txt",'w') as f:
    for i in range(1,51):
        f.write(f"{str(i)}\n")
def analyze(num):
    mi = min(num)
    ma = max(num)
    su = sum(num)
    return mi,ma,su
with open("numbers.txt",'r') as r:
    numbers = [int(x) for x in r.read().split('\n') if x]
    print(numbers)
    result = analyze(numbers)
def isodd(num):
      if num % 2 == 0:
            return(False)
      else:
            return(True)
for n in numbers:
     if isodd(n) == True:
          odd  += 1
     else:
          even += 1
print(f"The Smallest number is : {result[0]}")
print(f"The largest number is : {result[1]}")
print(f"The sum of all numbers is : {result[2]}")
print(f"There is {odd} odd numbers and {even} even numbers")


```
- Uses .read() and .write() to manipulate file objects and lines inside of it
- This code also analyses and prints out a summary of the read file
- also has functions that returns multiple variables , mi,ma and su for example.
