def down(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("Enter a number: "))

down = down(n)

for num in down:
    print(num)
