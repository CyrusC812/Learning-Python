## 5: Dictionaries - Working with Key-Value Pairs

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