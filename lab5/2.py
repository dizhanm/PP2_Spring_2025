import re

def match(text):
    return bool(re.fullmatch(r'^ab{2,3}$', text))

text = input()
print(match(text))