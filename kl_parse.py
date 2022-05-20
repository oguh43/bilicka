import re

numLock = re.compile("\[\dN\]")
num = re.compile("\d")

fPath = input("File path: ")
with open(fPath, "r") as f:
    data = f.read().split("\n")

out = []
buffer = ""
stack = ""
scanning = False
caps = False

for line in data:
    for char in line:
        if char not in ["[","]"]:
            if not scanning:
                stack += char.upper() if caps else char
                continue
            else:
                buffer += char
        if char == "[":
            scanning = True
            buffer += char
            continue
        if char == "]":
            scanning = False
            buffer += char
            if buffer == "[Cap]":
                caps = not caps
            elif buffer == "[Tab]":
                stack += buffer
            elif buffer == "[Bck]":
                stack = stack[0:-1]
            elif numLock.match(buffer):
                stack += num.search(buffer).group(0)
            buffer = ""
            continue
    out.append(stack)
    scanning = False
    buffer = ""
    stack = ""
    caps = False

outPath = "\\".join(fPath.split("\\")[0:-1]) + "\\out.txt"

with open(outPath, "w+") as f:
    f.write("\n".join(out))

#C:\Users\agent\Desktop\dumps\LOG.txt