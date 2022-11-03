with open("subory/slovnik.txt", "r") as f:
    l = list(map(lambda x: x.replace("\n", ""), f.readlines()))

m = {}
for i in range(0,len(l),2):
    m[l[i]] = l[i+1]
print(m)

while True:
    inp = input("(P)reložiť/ p(r)idať/ (Q)uit? > ").lower()
    if inp == "p":
        s = input("Slovko? > ")
        if s in m.keys() or s in m.values():
            try:
                print(f'{s} = {m[s]}')
            except KeyError:
                print(f'{s} = {list(m.keys())[list(m.values()).index(s)]}')
        else:
            print("Nenachádza sa v slovníku!")
    elif inp == "r":
        sk = input("Slovenské slovko? > ")
        eng = input("Anglické slovko? > ")
        m[sk] = eng
        with open("subory/slovnik.txt", "a") as f:
            f.write(f"\n{sk}\n{eng}")
    else:
        break