import re

def split_at_uppercase(s):
    return re.findall(r'[A-Z][a-z]*', s)

print(split_at_uppercase("HelloWorldExample"))  