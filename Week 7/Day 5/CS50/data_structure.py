FILEPATH = "/Users/denisereece/Documents/Intern To Junior Dev 2025/GitHub/learning-python/Week 7/Day 5/CS50/data_structure.tx"

def load_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        data = []
        for line in lines:  # Do NOT skip the header
            if line.strip():     # Ignore blank lines
                parts = [p.strip() for p in line.strip().split(',')]
                if len(parts) == 3:
                    item, type_, quantity = parts
                    # Try converting quantity to int, skip header if fails
                    try:
                        data.append({'item': item, 'type': type_, 'quantity': int(quantity)})
                    except ValueError:
                        continue  # Skip header or malformed lines
        return data

def lookup(data, item=None, type_=None, quantity=None):
    results = []
    for entry in data:
        if (
            (item is None or entry['item'].lower() == item.lower()) and
            (type_ is None or entry['type'].lower() == type_.lower()) and
            (quantity is None or entry['quantity'] == quantity)
        ):
            results.append(entry)
    return results

def print_entries(entries):
    for entry in entries:
        print(f"Item: {entry['item']}, Type: {entry['type']}, Quantity: {entry['quantity']}")

# Print example lookups
data = load_data(FILEPATH)

print("Full data:")
print_entries(data)

print("\nLookup by item 'Apple':")
print_entries(lookup(data, item="Apple"))

print("\nLookup by type 'Bakery':")
print_entries(lookup(data, type_="Bakery"))

print("\nLookup by quantity 30:")
print_entries(lookup(data, quantity=30))