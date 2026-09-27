with open("this8.txt") as f:
    data = f.read()
with open("this8_copy.txt", "w") as f:
    f.write(data)