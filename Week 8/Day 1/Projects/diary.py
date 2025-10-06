# Diary Application that appends entries to a text file

# File path for the diary file
diary_file_path = "/Users/denisereece/Documents/Intern To Junior Dev 2025/GitHub/learning-python/Week 8/Day 1/Projects/diary.txt"

# Function to add a diary entry
def add_diary_entry(month, day, year, entry):
    with open(diary_file_path, "a") as file:
        file.write(f"{month}, {day}, {year}, {entry}\n")

# Example usage
add_diary_entry("October", "7th", 2025, "Today I made my file path work correctly.")