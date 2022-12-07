from json import dump
with open("./hada.txt", "r") as f:
    data = f.read().splitlines()

print(len(data))
print(max(data,key=len))
out = []
buf = ""
for line in data:
    out.append("")
    for char in line:
        if len(buf) > 0:
            if char == buf[-1]:
                buf += char
            else:
                out[-1] += f'{str(len(buf))}{buf[-1]}'
                buf = char
        else:
            buf = char
print(out)
with open("comp", "w+") as f:
    dump(out, f)