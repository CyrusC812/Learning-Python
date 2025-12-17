# Multi-line printing
print("""This is an example of
multi-line printing""")
# Variable in strings

message = "Hello World"
print(message)

# count & find & replace
message = "Hello World"
print(message.count("e")) # Prints out 1 because theres only 1 e in "Hello World"
print(message.find("World")) # Prints out 6 because "World" starts at index 6

message = message.replace("World", "Universe") # alternative to creating a new string
print(message) # Prints out "Hello Universe" 
# String concatenation
greeting = "Hello"
name = "Alice"
message_fstring = f"{greeting.upper()}, {name} , Welcome!" # Using f-strings
message_concat = greeting + ", " + name + " , Welcome!" # Same thing but less readable
print(message_fstring)
print(message_concat)
