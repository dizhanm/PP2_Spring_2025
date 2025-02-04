import math

class Simple:

    def getString(self) -> None:
        a = input()

    def printString(self, s: str) -> None:
        print(s.upper())


class Shape:

    def area(self) -> float:
        return 0.0


class Square(Shape):
    def __init__(self, length: float) -> None:
        self.length = length

    def area(self) -> float:
        return self.length**2

class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def show(self) -> None:
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def dist(self, other: 'Point') -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. The balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Withdrawal denied: Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. The balance: ${self.balance:.2f}")




a = Simple()

a.printString("Hello")

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [i for i in range(0, 20)]

primeList = list(filter(lambda x: is_prime(x), numbers))
print(primeList)