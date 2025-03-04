def is_palindrome(s):
    return s == s[::-1]  

text = input("Enter string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not palindrome")
