# Bank account class used to deposit, withdraw, and check blance. 

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance
    
# Example usage:
account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print("Current Balance:", account.get_balance())  # Output: Current Balance: 120