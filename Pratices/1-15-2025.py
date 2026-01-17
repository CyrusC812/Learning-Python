import random
counter = 0
for i in range(5):
  x = random.randint(1,5)
  y = random.randint(1,20)
  a = int(input(f"Please enter the answer for {x} + {y} : "))
  aa = x+y
  if a == aa:
    counter += 1
print(f"Your score is {counter}")