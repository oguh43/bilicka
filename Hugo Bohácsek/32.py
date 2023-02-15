
with open("skoky.txt", "r") as f:
    data = f.read().splitlines()

print(data[0])

win = {}

mx = -100
for line in data:

    tmp = line.split(" ")
    if tmp[1] == "-1":
        continue
    for amm in tmp[1:]:
        if int(amm) > mx:
            mx = int(amm)

for line in data:
    tmp = line.split(" ")
    if tmp[1] == "-1":
        continue
    if str(mx) in tmp:
        win[tmp[0]] = " ".join(tmp[1:])

print(win)
