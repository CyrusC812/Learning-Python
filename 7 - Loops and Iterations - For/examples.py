number = (1,5,2,3,5,1,3,5)

for numbers in number: # Looping through however many numbers there are
    if numbers == 5:
        print("Found!", numbers) # This filters out 5s and say Found if theyre a 5
    else:
        print(numbers)
print("Done")
x = 0

while x != 10: # while continuies a loop until a statement is done
    x += 1 
    print(x)

while True: # This continues forever until x = 50
    x += 1
    if x == 50:
        break
    print(x)
