# Survey processor to analyze CSV survey results

import os
import csv

data = [
    ["Name", "Age", "Satisfaction"],
    ["Alice", 30, "High"],
    ["Bob", 25, "Medium"],
    ["Charlie", 35, "Low"]
]

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "survey_results.csv")
with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

# Function to read and display the contents of the CSV file
def read_survey(file_path):
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# Function to add a new survey response to the CSV file
def add_survey_response(file_path, response_data):
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(response_data)

# Function to correlate satisfaction levels with age groups
def correlate_satisfaction(file_path):
    age_groups = {"Under 30": [], "30 and above": []}
    with open(file_path, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            name, age, satisfaction = row
            age = int(age)
            if age < 30:
                age_groups["Under 30"].append(satisfaction)
            else:
                age_groups["30 and above"].append(satisfaction)
    
    print("Satisfaction Correlation by Age Group:")
    for group, satisfactions in age_groups.items():
        print(f"{group}: {satisfactions}")

# Example usage
print("Initial Survey Results:")
read_survey(csv_path)
add_survey_response(csv_path, ["David", 28, "High"])
print("\nAfter Adding David's Response:")
read_survey(csv_path)
print("\nSatisfaction Correlation:")
correlate_satisfaction(csv_path)