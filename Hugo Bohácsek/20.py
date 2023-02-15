
with open("inp.txt", "r") as f:
    data = f.read().splitlines()
for line in data:
    print(f'({line.split(" ")[0]}){line.split(" ")[1]} = {int(line.split(" ")[0], base=int(line.split(" ")[1]))}')
