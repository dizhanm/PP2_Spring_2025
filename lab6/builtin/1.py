def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num  
    return result


nums = [2, 3, 4, 5]
print("Product of all numbers:", multiply_list(nums))
