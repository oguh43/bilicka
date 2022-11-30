
with open("subory/lipsum.txt", "r") as f:
    q = f.read()

o = ""
for i in q:
    if 65 <= ord(i) <= 90:
        o += chr(ord(i) + 1) if ord(i) != 90 else "A"
    elif 97 <= ord(i) <= 122:
        o += chr(ord(i) + 1) if ord(i) != 122 else "a"
    else:
        o += i
#z-122 a-97
#Z-90 A-65

with open("subory/out/o3.txt", "w+") as f:
    f.write(o)













