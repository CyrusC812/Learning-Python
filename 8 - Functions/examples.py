def functionname(name): # An example of how to setup a function with 1 parameter 
    return f"Hello , {name}"

print(functionname("Cyrus"))

lists = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
info = {"name" : "Joe","Language": "English"} 
def unpack(*args,**kwargs):
    return f"{args}\n {kwargs}"

print(unpack(*lists,**info)) # This allows mappings to be returned


# Number of days per month. First value placeholder for indexing purposes.
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