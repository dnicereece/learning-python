# Inventory tracker to manage product data in spreadsheet format

import os
import csv

data = [
    ["Product", "Quantity", "Category"],
    ["Laptop", 10, "Electronics"],
    ["Chair", 25, "Furniture"],
    ["Notebook", 100, "Stationery"]
]

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "inventory.csv")
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Function to read and display the contents of the CSV file
def read_inventory(file_path):
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Function to add a new product record to the CSV file
def add_product_record(file_path, product_data):
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(product_data)

# Function to update a product's quantity
def update_product_quantity(file_path, product_name, new_quantity):
    rows = []
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == product_name:
                row[1] = new_quantity
            rows.append(row)
    
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

# Example usage
print("Initial Inventory:")
read_inventory(csv_path)
add_product_record(csv_path, ["Desk", 15, "Furniture"])
print("\nAfter Adding Desk:")
read_inventory(csv_path)
update_product_quantity(csv_path, "Chair", 30)
print("\nAfter Updating Chair Quantity:")
read_inventory(csv_path)