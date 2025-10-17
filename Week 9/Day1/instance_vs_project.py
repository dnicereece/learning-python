"""
In object-oriented programming, the terms "class," "object," and "instance" are closely related 
but represent distinct concepts:
"""

# Class
"""
A class acts as a blueprint or a template for creating objects. It defines the structure and 
behavior that objects of that type will possess. This includes the attributes (data or 
variables) that objects will hold and the methods (functions or behaviors) that objects can 
perform. A class itself is not a concrete entity in memory; it is a definition.
"""
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")


# Object
"""
An object is a concrete realization of a class. It is a specific entity created based on the 
class's blueprint. When you create an object, memory is allocated for its attributes, and it 
can then utilize the methods defined in its class.
"""

# Instance
"""
An instance is synonymous with an object. When an object is created from a class, it is said to 
be an "instance" of that class. Each instance has its own unique set of attribute values, even 
though it shares the same structure and behavior defined by its class. 
"""

# Creating instances (objects) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Poodle")

# 'my_dog' and 'your_dog' are both objects and instances of the 'Dog' class.
# They have their own 'name' and 'breed' values.
my_dog.bark()  # Output: Buddy says Woof!
your_dog.bark() # Output: Lucy says Woof!

"""
In summary, a class is the abstract definition, while an object or instance is a concrete 
manifestation of that definition in memory, with its own specific state. You define a class 
once, but you can create multiple objects (instances) from that single class.
"""

