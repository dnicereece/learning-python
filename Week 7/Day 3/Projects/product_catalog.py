# Product catalog with categories containing products with properties
product_catalog = [
    {
        'category': 'Electronics',
        'products': [
            {'name': 'Laptop', 'price': 999.99, 'stock': 10},
            {'name': 'Smartphone', 'price': 699.99, 'stock': 25},
            {'name': 'Headphones', 'price': 199.99, 'stock': 50}
        ]
    },
    {
        'category': 'Home Appliances',
        'products': [
            {'name': 'Refrigerator', 'price': 1199.99, 'stock': 5},
            {'name': 'Microwave', 'price': 149.99, 'stock': 15},
            {'name': 'Dishwasher', 'price': 499.99, 'stock': 7}
        ]
    },
    {
        'category': 'Books',
        'products': [
            {'name': 'Python Programming', 'price': 39.99, 'stock': 100},
            {'name': 'Data Science Handbook', 'price': 49.99, 'stock': 80},
            {'name': 'Machine Learning Basics', 'price': 29.99, 'stock': 60}
        ]
    }
]

# Function to display the product catalog
def display_catalog(catalog):
    for category in catalog:
        print(f"Category: {category['category']}")
        for product in category['products']:
            print(f"  Product: {product['name']}, Price: ${product['price']}, Stock: {product['stock']}")
        print()

# Function to find a product by name
def find_product(catalog, product_name):
    for category in catalog:
        for product in category['products']:
            if product['name'].lower() == product_name.lower():
                return product
    return None

# Function to update stock of a product
def update_stock(catalog, product_name, new_stock):
    product = find_product(catalog, product_name)
    if product:
        product['stock'] = new_stock
        print(f"Updated stock for {product_name} to {new_stock}.")
    else:
        print(f"Product {product_name} not found.")

# Function to add a new product to a category
def add_product(catalog, category_name, product_name, price, stock):
    for category in catalog:
        if category['category'].lower() == category_name.lower():
            category['products'].append({'name': product_name, 'price': price, 'stock': stock})
            print(f"Added product {product_name} to category {category_name}.")
            return
    print(f"Category {category_name} not found.")

# Function to remove a product by name
def remove_product(catalog, product_name):
    for category in catalog:
        for i, product in enumerate(category['products']):
            if product['name'].lower() == product_name.lower():
                category['products'].pop(i)
                print(f"Removed product {product_name}.")
                return
    print(f"Product {product_name} not found.")

# Example usage
display_catalog(product_catalog)
update_stock(product_catalog, 'Laptop', 8)
add_product(product_catalog, 'Electronics', 'Tablet', 299.99, 30)
remove_product(product_catalog, 'Microwave')
print("\nUpdated Catalog:")
display_catalog(product_catalog)