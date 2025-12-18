# An Overview of all notes organised into topics

Use this as the primary reference.

## 1 - Install and Setup for Mac and Windows

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


