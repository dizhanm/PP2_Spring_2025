def divisible_by_3_4():
    n = int(input())
    for i in range(1, n):
        if i % 3 == 0 and i % 4 == 0:
            yield str(i)

dv = divisible_by_3_4()
print(", ".join(dv))