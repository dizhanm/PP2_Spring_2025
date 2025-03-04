import string

for letter in string.ascii_uppercase:
    open(letter + ".txt", "w").close()  

print("26 text files (A.txt to Z.txt) have been created.")
