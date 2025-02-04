def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = []
while True:
    s = input("Enter numbers: ")
    if s == "":
        break
    numbers.append(int(s))

prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("Pime numbers: ", prime_numbers)