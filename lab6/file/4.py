import os

filename = input("Enter the filename: ")

file_path = os.path.join(os.getcwd(), filename)

if os.path.exists(file_path):  
    with open(file_path, "r", encoding="utf-8") as file:
        line_count = 0
        for line in file:
            line_count += 1

print(line_count)

