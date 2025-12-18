

courses = ['History', 'Math', 'Physics', 'CompSci']

print(len(courses)) # len() prints how many values/index there are.

print(courses[0]) # courses[0] returns the first index of the list

print(courses[-1]) # Negative index allows it to count from the end


courses.append('Art') # append adds items to existing list

print(courses) # Added Art at the end
courses.pop() # Pops Art off the end

print(courses.insert(2,'Art')) # Adds Art on index 2 instead
print(courses) # Prints course with art in index 2.

courses.reverse() # .reverse() reverses the whole list
print(courses)

nums = [1,5,3,5,1]
nums.sort() # Sorts it in ascending order
nums.sort(reverse=True) # Sorts it in descending order
courses.sort() # Alphabetical order
print(nums)
print(courses)

print(min(nums)) # min(nums) returns the smallest number
print(max(nums)) # max(nums) returns the largest number
print(sum(nums)) # sum(nums) returns the sum of all numbers