mp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
inp = input("Veta? >")
out = ""
for char in inp:
    if char == " ":
        out += "0 "
    else:
        out += str((mp.index(char)//3)+1) * (mp.index(char)%3 + 1) + " "
print(out)

from collections import Counter
print(Counter("".join(out.split(" "))))