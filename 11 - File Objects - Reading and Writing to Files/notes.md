# 11 - File Objects - Reading and writing to and from files

### Overview
How to manipulate file objects
## Key Concepts
### Modes
- 'r' for read file contents.
- 'w' for writing to files contents.
- 'a' for appending to files contents.
- 'r+' for read + write to files contents.
- 'b' for opening files in binary mode ( Images ).
> We can use different modes together like 'rb' can be used for reading a binary file
### Reading from files.
- file.close() for closing a file 
- file.mode returns mode the file was opened in
- file.name returns name of the file as a string
> Context managers are for effiency and organisation 
- file.read([size]) - typically used to read content of a file but when provided with <size> , it can read only the 'size'/ number of character , can be used repeatedly and it will continue off where it left off

- file.readlines() returns a list off all the lines of the file.
- file.readline() returns a single line
### Writing to files
- file.tell() returns the position of where the pointer is
- file.seek(new_position) changes the pointer's position to the specified
- file.write(content)  writes the contents to the file.
### Important Details
> trying to write to a file that does not exist will first create the file and then perform the writing operation.
> A file is treated as an iterable in python. This simply means that we can iterate over the lines of the file using a for loop (like we would loop over the elements of a list).
### Examples
- Repeating reading a file of specified size until reaches 0:
  ```python
    size = 10                              
    fileContents = file.read(size)

    while len(fileContents) > 0:     # while the length of what we have read is not 0, continue reading
        print(fileContents, end=('')
        fileContents = file.read(size)
- Using context managers to simultaneously read from a file and write to another:
  ```python
    with open("readFilePath", 'r') as readFile:
        with open("writeFilePath", 'w') as writeFile:
            _for line in readFile:
                _writeFile.write(line)
    #OR
    with open("readFilePath", 'r') as readFile:
        with open("writeFilePath", 'w') as writeFile:
            writeFile.write(readFile.read())



