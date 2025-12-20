import os
os.chdir(r"C:\Users\chung\Downloads\TestFolder")
list = ("a","b","c","d","e","f","g")
for v in list:
    for i in range(1,3):
        os.makedirs(f"{v}{i}/{i}")
        print(os.listdir())
