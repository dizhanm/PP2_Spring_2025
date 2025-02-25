import re

def change(text):
    return re.sub(r'[ ,.]', ':', text)

input_text = "Hello, world. How are you?"

print(change(input_text))
