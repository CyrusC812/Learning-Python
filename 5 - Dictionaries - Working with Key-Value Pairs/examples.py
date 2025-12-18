student = {'name': 'John','age': '25','course': ['Physics','Chemistry']}

print(student['name']) # printing value from key
 
print(student['name'],student['age']) # printing 2 values from 2 keys but same dictionary

student['name'] = 'Joe' # Directly changing value
student['age'] = '30' # Directly changing value

student.update({'name': 'John', 'age': '25'}) # .update({}) allows you to overwrite old data but also keep unchanged data

# del student['age'] - deletes age
print(student.items())

for x,value in student.items():
    value = str(value)
    print(f"{x.upper()} : {value.upper()}") # Applied fstring knowledge , this displays a good looking table of values