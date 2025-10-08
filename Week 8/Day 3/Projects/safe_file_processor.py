# File processor that safely handles missing files with error handling

import os

SAFE_DIR = "/Users/denisereece/Documents/Intern To Junior Dev 2025/GitHub/learning-python/Week 8/Day 3/Projects"

def process_file(filename):
    full_path = os.path.abspath(os.path.join(SAFE_DIR, filename))
    if not full_path.startswith(SAFE_DIR):
        print("Error: Invalid file path.")
        return
    try:
        with open(full_path, 'r') as file:
            data = file.read()
            print("File contents:")
            print(data)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename to process: ").strip()
    process_file(filename)