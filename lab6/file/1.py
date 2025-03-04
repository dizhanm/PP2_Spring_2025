import os

path = "."

if not os.path.exists(path):
    print(f"no '{path}'.")
else:
    print("Directories:")
    print(*[d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))], sep="\n")

    print("Files:")
    print(*[f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))], sep="\n")

    print("Elements:")
    print(*os.listdir(path), sep="\n")
