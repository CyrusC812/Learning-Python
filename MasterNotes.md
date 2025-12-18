# An Overview of all notes organised into topics

Use this as the primary reference.
## Table of Contents
- [Installation](#Installation)
- [Working with textual data](#string)
- [Working with textual data](#string)
- [List , Tuple and sets](#Lists)

## 1 - Install and Setup for Mac and Windows
→ #Installation

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

## 2 - Strings , Working with Textual Data
→ #string

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
- Standard Concatenation using + operator:
  ```python
  message_concat = greeting + ", " + name + " , Welcome!" # Same thing but less readable

## 4: Lists, Tuples, and Sets


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
- Number list sorting:
  ```python
    nums.sort() # Sorts it in ascending order
    nums.sort(reverse=True) # Sorts it in descending order
- List:
  ```python
    print(len(courses)) # len() prints how many values/index there are.

    print(courses[0]) # courses[0] returns the first index of the list

    print(courses[-1]) # Negative index allows it to count from the end
## For more examples check examples.py

