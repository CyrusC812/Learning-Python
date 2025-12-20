

# 8 : Modules and Standard library

### Overview

How to use modules and some standard libraries
## Key Concepts
### directories
- Use .chdir() to change working directory
- Use .getcwd() to get the working directory
- Use .mkdir() or makedirs() to make one or more directory and sub-directories for makedirs()
- Use .rmdir() or removedirs() to remove one or more directory and sub-directories for removedirs()
## Files
- Use .rename(<from>,<to>) to rename files or directories
- Use .stat() to list file properties
- Use .walk(<>) to walk through directories , this is useful for searching
- use .environ to get enviroment variables.
## Manipulation
- os.path.join() allows you to join paths without worrying about the extra / or not
- os.path.basename gets basename
- os.path.dirname gets dir name
- os.path.split() splits a path
- dir(os) 

### Important Details
> Use os module to edit files , directories of anything
> You wont remember everything , so use print(dir(os))
### Examples
- All commands in video:
  ```python
    os.getcwd()                       # get current working directory
    os.chdir(<path>)                                    # change directory 
    os.listdir()	                                            # list directory
    os.mkdir(<dirname>)                           # create a directory
    os.makedirs(<dirname>)                    # make directories recursively
    os.rmdir(<dirname>)	                   # remove directory
    os.removedirs(<dirname>)                # remove directory recursively
    os.rename(<from>, <to>)                   # rename file
    os.stat(<filename>)                            # print all info of a file
    os.walk(<path>)	                          # traverse directory recursively
    os.environ		                                 # get environment variables
    os.path.join(<path>, <file>)              # join path without worrying about /
    os.path.basename(<filename>)     # get basename
    os.path.dirname(<filename>)         # get dirname
    os.path.exists(<path-to-file>)         # check if the path exists or not
    os.path.splitext(<path-to-file>)      # split path and file extension
    dir(os)			                               # check what methods exists