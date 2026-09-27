with open("file4.txt") as f:
    data = f.read()
    newdata = data.replace("Donkey","#####")
with open("file4.txt", "w") as f:
        f.write(newdata)