Modes
'r' --> for read file contents.
'w' --> for writing to file.
'a' --> for eppending file contents.
'r+' --> for reading and writing
'b' --> to open file in binary mode (for reading images)
Note: We can use different modes together like 'rb' can be used for reading a binary file.

file.close()  --> closes a file.
file.mode --> returns the mode the file was opened in.
file.name  --> returns the name of the file as a string.

For effiency we use context managers.