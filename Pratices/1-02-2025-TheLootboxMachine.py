import random

item = ["Common","Rare","Epic","Legendary"]
x = random.randint(1,99)
if x < 60 and x >= 1:
  a = item[0]
elif x >= 61 and x <= 85:
  a = item[1]
elif x >= 86 and x <= 95:
  a = item[2]
else:
  a = item[3]
print(a)