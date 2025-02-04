class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self):
        self.length = int(input("Enter length: "))
    
    def area(self):
        return self.length * self.length

square = Square()

print(square.area())


