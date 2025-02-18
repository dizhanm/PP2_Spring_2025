def squares():
    a = int(input())
    b = int(input())
    for i in range(a, b + 1):
        yield i ** 2

sqr = squares()
for num in sqr:
    print(num)