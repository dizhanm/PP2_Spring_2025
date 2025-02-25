import re

def match(text):
    return re.fullmatch(r'ab*', text)

print(bool(match("a")))     
print(match("ab"))    
print(bool(match("abb")))   
print(match("b"))     
print(bool(match("abc")))  
