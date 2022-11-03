with open("subory/smsky.txt", "r") as f:
    smsky = f.read().split("\n")

with open("subory/vypadli.txt", "r") as f:
    vypadli = f.read().split("\n")

tot = {}
for c in smsky:
    if c not in tot.keys():
        tot[c] = 0
    tot[c] += 1
tot = dict(sorted(tot.items(), key=lambda item: item[1], reverse=True))
print(f"Bez vyradenia: {tot=}")
print(f'Najmenej dostal: {list(tot.keys())[-1]} -> {tot[list(tot.keys())[-1]]}')

for b in vypadli:
    try:
        del tot[b]
    except KeyError:
        pass
print(f"S vyradením: {tot=}")
print(f'Najmenej dostal: {list(tot.keys())[-1]} -> {tot[list(tot.keys())[-1]]}')

















