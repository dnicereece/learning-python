"""
Writing data to files in Python involves opening a file in a specific mode and then using 
methods like write() or writelines() to add content. Understanding file modes is crucial as 
they dictate how the file can be interacted with.
"""

# File Modes:

#'r' (Read): 
"""
Default mode. Opens a file for reading. If the file does not exist, it raises a 
FileNotFoundError.
"""
#'w' (Write): 
"""
Opens a file for writing. If the file exists, its content is truncated (erased). 
If the file does not exist, a new one is created.
"""
#'a' (Append): 
"""
Opens a file for appending. Data is added to the end of the file without erasing existing 
content. If the file does not exist, a new one is created.
"""
#'r+' (Read and Write): 
"""
Opens a file for both reading and writing. The file pointer is at the beginning of the file.
""" 
#'w+' (Write and Read): 
"""
Opens a file for both reading and writing. Creates a new file or overwrites an existing one.
"""
#'a+' (Append and Read): 
"""
Opens a file for both appending and reading. Data is added to the end. If the file does not 
exist, a new one is created.
"""
#'x' (Exclusive Creation): 
"""
Creates a new file and opens it for writing. Raises a FileExistsError if the file already exists.
"""
#'b' (Binary): 
"""
Used in conjunction with other modes (e.g., 'rb', 'wb', 'ab') to handle binary data 
(e.g., images, executables).
"""
#'t' (Text): 
"""Default mode, used in conjunction with other modes (e.g., 'rt', 'wt', 'at') to handle text 
data.
"""

# Writing Data to Files:
"""
The with open() statement is the recommended way to handle files, as it ensures the file is 
properly closed even if errors occur.
"""
# Writing to a new file or overwriting an existing one
with open("my_file.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

# Appending to an existing file
with open("my_file.txt", "a") as file:
    file.write("This line is appended.\n")

# Writing multiple lines from a list
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("another_file.txt", "w") as file:
    file.writelines(lines)