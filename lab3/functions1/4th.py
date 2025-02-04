def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def filter_prime(numbers):
    result = []
    for num in numbers:
        if is_prime(num):
            result.append(num)
    return result

nums = list(map(int, input().split()))
print(filter_prime(nums))