"""
To write structured data into a CSV file using Python, you can utilize the built-in csv module 
or the pandas library for more complex data handling.
"""
# Using the built-in csv module
"""
The csv module provides writer and DictWriter classes for writing data.
"""
# 1. Writing with csv.writer (for list-like data):
"""
This method is suitable when your data is structured as lists of values, where each inner list 
represents a row.
"""
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"],
    ["Charlie", 35, "Paris"]
]

with open("output.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# 2. Writing with csv.DictWriter (for dictionary-like data):
"""
This method is ideal when your data is structured as a list of dictionaries, where each 
dictionary represents a row and keys correspond to column headers.
"""
import csv

data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "London"},
    {"Name": "Charlie", "Age": 35, "City": "Paris"}
]

fieldnames = ["Name", "Age", "City"] # Define the order of columns

with open("output_dict.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row
    writer.writerows(data)

# Using the pandas library
"""
The pandas library offers a powerful and convenient way to handle structured data, especially 
when dealing with DataFrames.
"""
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 25, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)

# Write the DataFrame to a CSV file
df.to_csv("output_pandas.csv", index=False) # index=False prevents writing the DataFrame index as a column

# Explanation:
"""
-open(filename, "w", newline=""): Opens the specified file in write mode ("w"). newline="" is 
crucial to prevent extra blank rows in the CSV file, especially on Windows.

-csv.writer(csvfile): Creates a writer object that allows you to write data as rows.

-writer.writerows(data): Writes multiple rows from a list of lists.

-csv.DictWriter(csvfile, fieldnames=fieldnames): Creates a DictWriter object, mapping dictionary 
keys to CSV headers. fieldnames specifies the order of columns.

-writer.writeheader(): Writes the header row using the fieldnames.

-writer.writerows(data) (for DictWriter): Writes multiple rows from a list of dictionaries.

-pd.DataFrame(data): Creates a Pandas DataFrame from your structured data (e.g., a dictionary 
of lists).

-df.to_csv(filename, index=False): Writes the DataFrame to a CSV file. index=False prevents 
writing the DataFrame's index as a column in the CSV.
"""