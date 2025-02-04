def toOunces():
    gramm = float(input())
    return gramm * 28.3495231 


def fToc():
    f = float(input())
    return round((5 / 9) * (f - 32), 1)


def solve(numheads, numlegs):
    r = (numlegs - 2 * numheads) // 2
    c = numheads - r
    return c, r


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


def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        i = l
        while i <= r:
            s[l], s[i] = s[i], s[l]  
            permute(s, l + 1, r)     
            s[l], s[i] = s[i], s[l]  #
            i += 1

def print_permutations(string):
    s = list(string)
    permute(s, 0, len(s) - 1)


def reverse_words():
    s = input()
    print(" ".join(s.split()[::-1]))    


def has_33(nums):
    for i in range(len(nums) - 1): 
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


def spy_game(nums):
    code = [0, 0, 7]  
    for num in nums:
        if num == code[0]:  
            code.pop(0)
        if not code:  
            return True
    return False


import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)


def unique_elements(lst):
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list


def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    return s == s[::-1]  


def histogram(nums):
    for i in range(len(nums)):
        print('*' * nums[i])



import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    number_to_guess = random.randint(1, 20)
    attempts = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break


