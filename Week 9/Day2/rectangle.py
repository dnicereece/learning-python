# Rectangle class for calculating area and perimeter
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Example usage:
rect = Rectangle(5, 10)
print("Area:", rect.area())            # Output: Area: 50
print("Perimeter:", rect.perimeter())  # Output: Perimeter: 30

rect2 = Rectangle(3, 4)
print("Area:", rect2.area())            # Output: Area: 12
print("Perimeter:", rect2.perimeter())  # Output: Perimeter: 14