class BankAccount:
    def __init__(self, account_number, customer_name, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}.")
        else:
            print(f"Insufficient balance. Withdrawal of {amount} failed.")

    def display(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance}")

my_account = BankAccount("2134", "Mako", 1000)
my_account.deposit(500)
my_account.withdraw(2000)
my_account.display()
