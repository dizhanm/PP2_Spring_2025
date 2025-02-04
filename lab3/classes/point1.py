class Point:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

    def show(self):
       
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
       
        self.x = new_x
        self.y = new_y

    def dist(self, other):
       
        return (((self.x - other.x) ** 2 + (self.y - other.y) ** 2)**0.5)


p1 = Point(float(input("Enter x1: ")), float(input("Enter y1: ")))
p2 = Point(float(input("Enter x2: ")), float(input("Enter y2: ")))

while True:
    print()
    print("Select Method:")
    print("show")
    print("move")
    print("dist")
    print("enter 'STOP' to exit")
    print()

    mthd = input()

    if mthd == "show":
        p1.show()
        p2.show()
    elif mthd == "move":
        p1.move(float(input("Enter new x1: ")), float(input("Enter new y1: ")))
        p2.move(float(input("Enter new x2: ")), float(input("Enter new y2: ")))
        p1.show()
        p2.show()
    elif mthd == "dist":
        print(p1.dist(p2))
    elif mthd == "STOP":
        print("OK")
        break
    else:
        print("ERROR")


