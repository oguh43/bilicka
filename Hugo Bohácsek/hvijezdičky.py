size = int(input("Veľkosť? > "))
buf = ""
for _ in range (size):
    buf += "*" * size + "\n"

print(buf)
buf = ""

for i in range (size):
    if i in [0, size - 1]:
        buf += "*" * size + "\n"
    else:
        buf += "*" + " " * (size - 2) + "*\n"

print(buf)
buf = ""

sizeX = int(input("Veľkosť? > "))
for _ in range(size):
    buf += "*" * sizeX + "\n"

print(buf)
buf = ""

for i in range(size):
    buf += "*" * (i + 1) + "\n"
print(buf)
buf = ""

for i in range(size):
    buf += " " * (size - i - 1) + "*" * (i + 1) + "\n"
print(buf)
buf = ""

for i in range(size):
    buf += " " * (size // 2 - i + 1) + "* " * (i + 1) + "\n"
print(buf)
buf = ""

for i in range(size):
    buf += " " * (i * (sizeX - 1)) + "*" * sizeX + "\n"
print(buf)
buf = ""

for i in range(size-1,-1,-1):
    buf += " " * (size // 2 - i + 1) + "* " * (i + 1) + "\n"
for i in range(1,size):
    buf += " " * (size // 2 - i + 1) + "* " * (i + 1) + "\n"
print(buf)
buf = ""

for i in range(size):
    buf += " " * (i * (sizeX - 2)) + "*" * sizeX + "\n"
print(buf)
buf = ""

