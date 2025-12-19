
answer = 'y'

while answer == 'y':
    name = input("Enter name of student : ")
    age = int(input(f"Enter {name}'s age : "))
    courses = input(f"Enter {name}'s courses seperated by a space : ")
    courses = courses.split(" ")
    student = {'Name': name,'Age': age,'Courses': courses}
    for x, value in student.items():
        if isinstance(value, list):
            value = ", ".join(value)  # Revise this bit nigga
        else:
            value = str(value)
        print(f"{x} : {value}")
    answer = input("\n Would you like to add another student? (Y/N) : ").lower()
else:
    print("Bye!")
    