import re

def lowercase(text):
    return bool(re.search(r'[a-z]+_[a-z]+', text))

print(lowercase("hello_world"))  
print(lowercase("helloworld"))   
print(lowercase("hello_world_")) 
print(lowercase("Hello_world")) 
print(lowercase("hello__world"))
print(lowercase("test hello_world")) 
