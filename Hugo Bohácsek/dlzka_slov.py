c = {}
with open("subory/lipsum.txt", "r") as f:
    q = (" ".join(f.read().split("\n"))).split(" ")
for i in q:
    if len(i) not in c.keys():
        c[len(i)] = 0
    c[len(i)] += 1
print(c)
print(f'{max(c.keys())}: {c[max(c.keys())]}')