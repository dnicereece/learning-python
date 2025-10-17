# Person class definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Example usage:
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person1.introduce()
person2.introduce()