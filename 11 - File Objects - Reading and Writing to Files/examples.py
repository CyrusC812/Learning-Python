import time
with open('C:/Users/chung/OneDrive/Documents/GitHub/Learning-Python/11 - File Objects - Reading and Writing to Files/test.txt','r') as var: # Loops through each line of the test.txt and prints them out one by one
    for line in var:
        print(line, end="")
print("\n\n")
with open('11 - File Objects - Reading and Writing to Files/test.txt', 'r') as var:
    f = var.read(100)
    print(f, end="\n")
    g = var.read(100)
    print(g,end='')
print("\n\n")
with open('11 - File Objects - Reading and Writing to Files/test.txt', 'r') as var:
    SizeToRead = 10
    content = var.read(SizeToRead)
    while len(content) > 0:
        print(content,end="*")
        content = var.read(SizeToRead)
        time.sleep(0.1)