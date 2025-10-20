"""
In Python, @classmethod and @staticmethod are decorators used to define special types of methods 
within a class, differing from regular instance methods in how they interact with the class and 
its instances.
"""

# @classmethod
"""
-A class method takes the class itself as its first argument, conventionally named cls.

-It can access and modify class-level attributes, which are shared by all instances of the class.

-It is often used for creating alternative constructors or factory methods that return an 
instance of the class.
"""
class MyClass:
    class_variable = "I am a class variable"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def create_from_string(cls, data_string):
        # cls refers to the class MyClass
        instance_variable = data_string.upper()
        return cls(instance_variable)

    @classmethod
    def print_class_variable(cls):
        print(f"Class variable: {cls.class_variable}")

# Usage
obj1 = MyClass("hello")
print(obj1.instance_variable)

obj2 = MyClass.create_from_string("world")
print(obj2.instance_variable)

MyClass.print_class_variable()

# @staticmethod
"""
-A static method does not take self (the instance) or cls (the class) as its first argument.
-It behaves like a regular function but is logically grouped within the class's namespace.
-It cannot access or modify instance-specific data or class-level attributes unless explicitly 
passed as arguments.
-Static methods are useful for utility functions that belong conceptually to the class but do 
not require access to its state.
"""
class Calculator:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Usage
result_add = Calculator.add(10, 5)
print(f"Addition: {result_add}")

result_subtract = Calculator.subtract(10, 5)
print(f"Subtraction: {result_subtract}")

# Key Differences:

# First Argument: 
"""
Class methods receive cls (the class) implicitly, while static methods receive no implicit 
arguments.
"""
# Access to State: 
"""Class methods can access and modify class state (class variables), while static methods 
cannot access instance or class state without explicit arguments.
"""
# Purpose: 
"""
Class methods are often used for alternative constructors or operations involving class-level 
data, while static methods are for utility functions related to the class but independent of 
its state.
"""