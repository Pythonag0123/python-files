#Bank Transaction System
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"{self.owner}'s balance is {self.balance}")
acc1 = BankAccount("Rohan", 1000)
acc1.deposit(500)
acc1.withdraw(200)
acc1.check_balance()

