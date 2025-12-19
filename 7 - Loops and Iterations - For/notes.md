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