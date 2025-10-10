"""
Program which Expects the user to provide two command-line arguments:
-the name of an existing CSV file to read as input, whose columns are assumed to be, in order, 
name and house, and
-the name of a new CSV to write as output, whose columns should be, in order, first, last, and 
house.
-Converts that input to that output, splitting each name into a first name and last name. 
Assume that each student will have both a first name and last name.
"""

import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    in_path, out_path = sys.argv[1], sys.argv[2]
    rows = []
    try:
        with open(in_path, newline="") as f:
            reader = csv.DictReader(f)
            for r in reader:
                if r.get("name"):
                    last, first = [p.strip() for p in r["name"].split(",", 1)]
                    rows.append({"first": first, "last": last, "house": r["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {in_path}")
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        writer.writeheader(); writer.writerows(rows)

if __name__ == "__main__":
    main()