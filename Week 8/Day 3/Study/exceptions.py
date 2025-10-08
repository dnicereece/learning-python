"""
Handling file errors in Python involves using try-except blocks to gracefully manage potential 
issues that can arise during file operations.
"""

# Common File Errors and How to Handle Them:

# FileNotFoundError: 
"""
Occurs when attempting to open a file that does not exist.
"""
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The specified file was not found.")

# PermissionError:
"""
Occurs when the program lacks the necessary permissions to access or modify a file.
"""
try:
    with open('/root/protected_file.txt', 'w') as file:
        file.write("Attempting to write to a protected file.")
except PermissionError:
    print("Error: Insufficient permissions to access or modify the file.")

# IOError (or OSError):
"""
A general I/O error that can encompass various issues, including FileNotFoundError and 
PermissionError, as well as others like disk full errors.
"""
try:
    with open('data.txt', 'r') as file:
        content = file.read()
except IOError as e:
    print(f"An I/O error occurred: {e}")

# Best Practices for File Error Handling:

# Use with statements (Context Managers): 
"""
This ensures files are automatically closed, even if errors occur, preventing resource leaks.
"""
# Specific Exception Handling: 
"""Catch specific exceptions like FileNotFoundError and PermissionError before catching more 
general exceptions like IOError or a bare except clause. This allows for more targeted error 
messages and recovery actions.
"""
# Informative Error Messages: 
"""Provide clear and helpful messages to the user or for logging purposes, explaining what went 
wrong.
"""
# Cleanup with finally: 
"""
If not using with statements, use a finally block to ensure resources are released (e.g., 
closing a file) regardless of whether an exception occurred.
"""
# Logging: 
"""
Log errors to a file or console for debugging and monitoring purposes.
""" 