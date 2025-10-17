# Object Oriented Banking System with class variables, instance variables, and decorators tracking accounts, transactions, and customers. 

def log_transaction(func):
    def wrapper(self, amount):
        result = func(self, amount)
        print(f"[LOG] {func.__name__.capitalize()} of ${amount} for {self.account_holder}. New balance: ${self.balance}")
        return result
    return wrapper

class BankAccount:
    total_accounts = 0  # class variable

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        BankAccount.total_accounts += 1

    @log_transaction
    def deposit(self, amount):
        self.balance += amount

    @log_transaction
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

class Transaction:
    total_transactions = 0  # class variable

    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type

    def process(self):
        Transaction.total_transactions += 1
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type.")

class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, initial_balance=0):
        new_account = BankAccount(self.name, initial_balance)
        self.accounts.append(new_account)
        return new_account

    def get_account_info(self):
        for account in self.accounts:
            print(f"Account Holder: {account.account_holder}, Balance: ${account.balance}")

# Example usage
customer1 = Customer("Alice")
account1 = customer1.open_account(1000)
account2 = customer1.open_account(500)

transaction1 = Transaction(account1, 200, "deposit")
transaction2 = Transaction(account2, 100, "withdraw")

transaction1.process()
transaction2.process()

customer1.get_account_info()

print(f"Total accounts: {BankAccount.total_accounts}")
print(f"Total transactions: {Transaction.total_transactions}")