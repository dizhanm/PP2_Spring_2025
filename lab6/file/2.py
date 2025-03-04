import os

path = input("Enter the path to check: ")

if os.path.exists(path):
    print(f"\nPath '{path}' exists.")
    
    if os.access(path, os.R_OK):
        print("Readable: Yes")
    else:
        print("Readable: No")

    if os.access(path, os.W_OK):
        print("Writable: Yes")
    else:
        print("Writable: No")

    if os.access(path, os.X_OK):
        print("Executable: Yes")
    else:
        print("Executable: No")

else:
    print(f"\nPath '{path}' does not exist.")
