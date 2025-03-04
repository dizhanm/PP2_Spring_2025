import os

source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")

if not os.path.exists(source_file):
    print(f"Error: File '{source_file}' does not exist.")
else:
    with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()

    with open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(content)

    print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
