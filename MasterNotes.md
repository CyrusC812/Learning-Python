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