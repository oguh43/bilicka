from re import sub
c = {}
with open("subory/lipsum.txt", "r") as f:
    q = sub(r" |\.|,","","".join(f.read().split("\n")))
for i in q:
    if i not in c.keys():
        c[i] = 0
    c[i] += 1
print(c)