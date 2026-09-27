words = ["Donkey","stupid","idiot"]

with open("file4.txt") as f:
    data = f.read()
for word in words:
    data = data.replace(word, "#####")
with open("file4.txt", "w") as f:
    f.write(data)