with open("file6.txt") as f:
    data = f.read()

if ("Python" in data):
    print("Python is present in the file.")
else:
    print("Python is not present in the file.")