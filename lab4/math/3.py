import math
def polygon():
    sides = int(input("Input number of sides: "))
    length = float(input("Input the length of a side: "))
    area = round(0.25 * sides * pow(length, 2) * ( math.cos(math.pi / sides) / math.sin(math.pi/ sides)))
    return area

print(polygon())