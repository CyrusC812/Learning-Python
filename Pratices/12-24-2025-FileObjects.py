odd = 0
even = 0
with open("numbers.txt",'w') as f:
    for i in range(1,51):
        f.write(f"{str(i)}\n")
def analyze(num):
    mi = min(num)
    ma = max(num)
    su = sum(num)
    return mi,ma,su
with open("numbers.txt",'r') as r:
    numbers = [int(x) for x in r.read().split('\n') if x]
    print(numbers)
    result = analyze(numbers)
def isodd(num):
      if num % 2 == 0:
            return(False)
      else:
            return(True)
for n in numbers:
     if isodd(n) == True:
          odd  += 1
     else:
          even += 1
print(f"The Smallest number is : {result[0]}")
print(f"The largest number is : {result[1]}")
print(f"The sum of all numbers is : {result[2]}")
print(f"There is {odd} odd numbers and {even} even numbers")


# Here I used knowledge from file objects to grab and write into files
# I would improve this by simplifying isodd() , it can be simplfied by just doing return n % 2 != 0 because it will return either true or false.