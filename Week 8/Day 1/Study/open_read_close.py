"""
Opening, reading, and closing text files in Python can be achieved using the built-in open() 
function and file object methods. The with statement is the recommended approach for handling 
files, as it ensures proper closing even if errors occur.
"""

# Using the with statement (Recommended):
"""
The with statement creates a context manager that automatically handles closing the file when 
the block is exited.
"""
# Open the file in read mode ('r')
with open('my_text_file.txt', 'r', encoding='utf-8') as file:
    # Read the entire content of the file
    content = file.read()
    print(content)

    # Alternatively, read line by line
    # for line in file:
    #     print(line.strip()) # .strip() removes leading/trailing whitespace, including newlines
"""
-open('my_text_file.txt', 'r', encoding='utf-8'): This opens the file named 'my_text_file.txt' 
in read mode ('r'). Specifying encoding='utf-8' is good practice to avoid UnicodeDecodeError with various text files.

-as file: This assigns the file object to the variable file.

-file.read(): Reads the entire content of the file as a single string.

-for line in file:: Iterating directly over the file object reads the file line by line, which 
is memory-efficient for large files.
"""

# 2. Manual Open, Read, and Close:
"""
This method requires explicitly calling close() to release file resources.
"""
try:
    # Open the file in read mode ('r')
    file = open('my_text_file.txt', 'r', encoding='utf-8')

    # Read the content
    content = file.read()
    print(content)

except FileNotFoundError:
    print("Error: The file 'my_text_file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Ensure the file is closed, even if an error occurred
    if 'file' in locals() and not file.closed:
        file.close()
"""
-open('my_text_file.txt', 'r', encoding='utf-8'): Opens the file.

-file.read(): Reads the content.

-file.close(): Explicitly closes the file.

-The try...except...finally block handles potential FileNotFoundError and ensures the file is 
closed in the finally block, regardless of whether an error occurred.
"""

# Key considerations:

## File Modes:
"""
Use 'r' for reading, 'w' for writing (overwrites existing files), 'a' for appending, and 'r+' 
for reading and writing. Add 'b' for binary mode (e.g., 'rb', 'wb').
"""

## Error Handling:
"""
Always consider potential errors like FileNotFoundError and implement appropriate error
handling.
"""

## Encoding Parameter:
"""
Explicitly setting the encoding (e.g., encoding='utf-8') is crucial for handling text files 
with various character sets.
"""