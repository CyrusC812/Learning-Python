import random
x = []
for i in range(50):
  x.append(i)
for i in range(49):
  y = random.choice(x)
  input(f"{y} \n Press enter for next number :")
  x.pop(y)
