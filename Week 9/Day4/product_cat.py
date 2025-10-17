# Prodct cataloge module for product categories and instances
class ProductCategory:
    all_categories = []  # Class variable to track all categories

    def __init__(self, name, description):
        self.name = name  # Instance variable
        self.description = description  # Instance variable
        self.products = []  # Instance variable
        ProductCategory.all_categories.append(self)  # Track instance

    def add_product(self, product):
        self.products.append(product)

    @property
    def product_names(self):
        # Decorator for read-only access
        return [product.name for product in self.products]

class Product:
    all_products = []  # Class variable to track all products

    def __init__(self, name, price, sku):
        self.name = name  # Instance variable
        self.price = price  # Instance variable
        self.sku = sku  # Instance variable
        Product.all_products.append(self)  # Track instance

    @property
    def info(self):
        # Decorator for formatted info
        return f"Product: {self.name}, Price: ${self.price}, SKU: {self.sku}"

# Creating ProductCategory objects
electronics = ProductCategory("Electronics", "Devices and gadgets")
clothing = ProductCategory("Clothing", "Apparel and accessories")
books = ProductCategory("Books", "Printed and digital books")

# Creating Product objects
laptop = Product("Laptop", 999.99, "ELEC1234")
smartphone = Product("Smartphone", 699.99, "ELEC5678")
tshirt = Product("T-Shirt", 19.99, "CLOTH123")
jeans = Product("Jeans", 49.99, "CLOTH456")
novel = Product("Novel", 14.99, "BOOK123")
textbook = Product("Textbook", 89.99, "BOOK456")

# Adding products to categories
electronics.add_product(laptop)
electronics.add_product(smartphone)
clothing.add_product(tshirt)
clothing.add_product(jeans)
books.add_product(novel)
books.add_product(textbook)

# Displaying product category information and products
for category in ProductCategory.all_categories:
    print(f"Category: {category.name} - {category.description}")
    for product_name in category.product_names:
        print(f" - {product_name}")
    print()

# Displaying detailed product information
for product in Product.all_products:
    print(product.info)

# Displaying products in each category with details
for category in ProductCategory.all_categories:
    print(f"\nProducts in Category: {category.name}")
    for product in category.products:
        print(product.info)

# Example of accessing specific product details
print(f"\nDetails of a specific product:")
print(laptop.info)
print(tshirt.info)

# Example of listing all products in the Electronics category
print(f"\nAll products in Electronics category: {electronics.product_names}")

# Example of listing all products in the Clothing category
print(f"All products in Clothing category: {clothing.product_names}")