f = open("file1.txt")
poem = f.read()
if("Twinkle" in poem):
    print("Twinkle is present.")
else:
    print("Twinkle is not present.")
f.close()