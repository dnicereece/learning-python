# Employee management System to track total employees using class variables and instance variables and class decorators
class Employee:
    # Class variable to keep track of total employees
    total_employees = 0

    def __init__(self, name, position):
        # Instance variables
        self.name = name
        self.position = position
        # Increment the class variable when a new employee is created
        Employee.total_employees += 1

    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

    @staticmethod
    def company_policy():
        return "All employees must adhere to the company's code of conduct."
    
# Creating multiple Employee objects
emp1 = Employee("John Doe", "Software Engineer")
emp2 = Employee("Jane Smith", "Data Scientist")
emp3 = Employee("Emily Davis", "Product Manager")

# Displaying employee information
print(f"Employee 1: {emp1.name}, Position: {emp1.position}")
print(f"Employee 2: {emp2.name}, Position: {emp2.position}")
print(f"Employee 3: {emp3.name}, Position: {emp3.position}")

# Displaying total employees
print(f"Total Employees: {Employee.get_total_employees()}")

# Displaying company policy
print(Employee.company_policy())