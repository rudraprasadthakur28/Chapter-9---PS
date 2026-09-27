import os
os.makedirs("tables", exist_ok=True)

for n in range(2, 21):
    with open(f"tables/table{n}.txt", "w") as f:
        for i in range(1, 11):
            print(f"{n} * {i} = {n * i}")
            f.write(f"{n} * {i} = {n * i}\n")