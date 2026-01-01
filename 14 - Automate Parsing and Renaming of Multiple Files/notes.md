# 14 - Automating renaming files

### Overview
How to automate file renaming, I used one of my folders that contained messy CAD .step files as example
## Key Concepts
### Striping and cleaning files
- use os.path.splitext(f) to split extension from a file
- use f.strip() to remove empty white spaces
- use zfill(2) to pad numbers , like from 2 to 02
### Other useful commands when automating file renaming
- os.rename(f,new_name) to actually rename it
- use fstrings to construct a new name for file
### Important Details
> Automating renaming files are very useful when folders are large and messy , they save a lot of time
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