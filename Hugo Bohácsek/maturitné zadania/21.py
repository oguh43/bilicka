with open("pretekari.txt", "r") as f:
    data = [x.split(" ") for x in f.read().splitlines()]

with open("stanovistia.txt", "r") as f:
    stn = f.read().splitlines()

for line in data:
    if sorted(line[2:]) != sorted(stn):
        print(f"{line[0]} podvádzal")
        line.append(99999999)
    else:
        
        line.append(int(line[1].split(":")[0]) * 60 + int(line[1].split(":")[1]))

data.sort(key=lambda x: x[-1])

for i in range(0, len(data)):
    print(f"{i+1}.", data[i])
