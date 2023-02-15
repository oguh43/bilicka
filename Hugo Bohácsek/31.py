
with open("kamosi.txt", "r") as f:
    tmp = f.read().splitlines()
    data = [[tmp[i], tmp[i + 1]] for i in range(0, len(tmp)-1, 2)]

data.sort(key=lambda x: x[0])

print(data)

nar = input("Mešec? > ")

acc = []

for pepol in data:
    if pepol[1].split(" ")[2] == nar:
        pepol.append(f" {2023-int(pepol[1].split(' ')[-1])}")
        acc.append(pepol)

if len(acc):
    print(acc)
else:
    print("Nikto nemnarodil :(")



