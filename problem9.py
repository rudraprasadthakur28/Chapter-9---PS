with open("this8.txt") as f:
    data1 = f.read()
with open("this8_copy.txt") as f:
    data2 = f.read()

first = data1
second = data2

if (data1 == data2):
    print("Both files are same.")
else:
    print("Both files are different.")