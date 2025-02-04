class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            pass

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Too big amount")

owner = input("Enter account owner: ")
balance = int(input("Enter initial balance: "))

acc = Account(owner, balance)

deposit_amount = int(input("Enter deposit amount: "))
acc.deposit(deposit_amount)

withdraw_amount = int(input("Enter withdrawal amount: "))
acc.withdraw(withdraw_amount)

print(f"Final balance: {acc.balance}")