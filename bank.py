class BankAccount:
    def __init__(self, accNumber, initialBalance):
        self.account_number = accNumber
        self.balance = float(initialBalance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def get_balance(self):
        return self.balance


acc = BankAccount("10596770", 15)


acc.withdraw(10)
acc.deposit(70)
print(acc.get_balance())
