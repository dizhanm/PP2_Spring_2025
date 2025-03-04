filename = input("Enter the filename: ")

data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]  

with open(filename, "w", encoding="utf-8") as file:
    for item in data:
        file.write(item)  

print(f"List has been written to '{filename}'.")
