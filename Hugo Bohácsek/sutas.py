with open("sutas.txt", "r") as f:
    data = f.read().splitlines()

print(len(data))

mx = 0
for l in data:
    if len(l) > mx:
        mx = len(l)

print(mx)

fin = ""
buf = ""

c = 0
n = []

for line in data:
    for char in line:
        if buf == "":
            buf = char
            c += 1
            continue
        if char != buf:
            fin += f"{buf} {c} "
            c = 1
            buf = char
            continue
        
        c+=1
    n.append(fin)
    buf = ""
    fin  = ""
    c = 0
import json
with open("o.txt", "w+") as f:
    f.write(json.dumps(n))
