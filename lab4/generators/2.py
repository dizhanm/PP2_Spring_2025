def even_numbers(n):
    for i in range(1, n):
        if i % 2 == 0:
            yield str(i)

n = int(input())
ev = even_numbers(n)
print(", ".join(ev))