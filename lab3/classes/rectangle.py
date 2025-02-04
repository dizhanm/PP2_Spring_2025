class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Enter length: "))

        self.width = int(input("Enter width: "))
    
    def area(self):
        return self.length * self.width

rectangle = Rectangle()

print(rectangle.area())



