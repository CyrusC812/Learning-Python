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