# Data value recording system with timestamped entries
# Import necessary modules
import json
import os
from datetime import datetime

# Function to load existing data from a file
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    else:
        return []
    
# Function to save data to a file
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Function to log a new data entry with a timestamp
def log_data(data, value):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {'timestamp': timestamp, 'value': value}
    data.append(entry)
    return data

# Function to display all logged data
def display_data(data):
    if not data:
        print("No data logged yet.")
    else:
        for entry in data:
            print(f"{entry['timestamp']}: {entry['value']}")

# Main function to run the data logger
def main():
    file_path = 'data_logger.json'
    data = load_data(file_path)
    
    while True:
        print("\nData Logger")
        print("1. Log New Data")
        print("2. Display Logged Data")
        print("3. Save and Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            value = input("Enter data value to log: ")
            data = log_data(data, value)
            print("Data logged.")
        elif choice == '2':
            display_data(data)
        elif choice == '3':
            save_data(file_path, data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()