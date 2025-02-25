import re

def find(text):
    return bool(re.search(r'[A-Z][a-z]+', text))

print(find("Aii"))    
print(find("Aii"))       
print(find("B_test"))    
print(find("hello_World")) 
print(find("Z_abcd Zaxx"))    
print(find("sdfj Asdd"))
print(find("AAaaa"))