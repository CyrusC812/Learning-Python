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
