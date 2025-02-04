import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


p1 = Point(x1, y1)
p2 = Point(x2, y2)


p1.show()
p2.show()


print(f"distance: {p1.dist(p2)}")


new_x = float(input())
new_y = float(input())
p1.move(new_x, new_y)


p1.show()