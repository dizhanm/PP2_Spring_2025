def square_numbers():
    n = int(input())
    for i in range(n):
        yield i ** 2

sqr = square_numbers()
for num in sqr:
    print(num)