import time  
import math 

n = int(input("Enter a number: "))  
t = int(input("Enter delay in milliseconds: ")) 

time.sleep(t / 1000)  
result = math.sqrt(n)
print(f"Square root of {n} after {t} milliseconds is {result}")