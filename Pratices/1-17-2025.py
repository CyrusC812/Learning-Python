import random
num = random.randint(1,10)
y = int(input("Please enter a number : "))
while y != num:
  if y < num:
    y = int(input("Its higher , try again :"))
  else:
    y = int(input("Its lower , try again :"))
print("Correct!")