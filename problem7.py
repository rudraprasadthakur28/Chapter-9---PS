line_number = 1
with open("file6.txt") as f:
    for line in f:
        if ("Python" in line):
            print(f"The word Python is present in line number: {line_number}")
        line_number +=1