import re

def camel_to_snake(s):
    return '_'.join(re.findall(r'[A-Za-z][a-z]*', s)).lower()

print(camel_to_snake("HelloWorldExample"))  