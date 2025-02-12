import math

def trapezoid():
    heigt, base1, base2 = int(input("Height: ")), int(input("Base, first value: ")), int(input("Base, second value: "))
    return f"The area of a trapezoid is {(heigt * (base1 + base2) / 2)}"

print(trapezoid())