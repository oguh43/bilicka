
"""
a)	vypíše zoznam všetkých kníh, na ktoré treba poslať upomienku
b)	vypíše knihu, ktorá sa najviac požičiava 
c)	a zoradí knihy podľa dĺžky doby vypožičania

"""
data = {}

with open("knihy.txt", "r") as f:
    tmp = f.read().splitlines()

for i in range(0, len(tmp), 2):
    data[tmp[i]] = tmp[i + 1].split(" ")

#ddmm



mx = -1
sv = ""
for k,v in data.items():
    if len(v) > mx:
        mx = len(v)
        sv = k
    elif len(v) == mx or len(v)+1 == mx:
        sv += f" a {k}"
    v.append(k)
    v.append(0)
    for i in range(0, len(v) - 2, 2):
        if i + 1 == len(v) - 2:
            d1 = int(v[i][:2])
            m1 = int(v[i][2:])
            print(f"Nevrátené: {k}")
            v[-1] += 99
            continue
        d1 = int(v[i][:2])
        m1 = int(v[i][2:])
        d2 = int(v[i+1][:2])
        m2 = int(v[i+1][2:])
        if (d2 - d1) + ((m2 - m1) * 30) > 30:
            print(f"Mala byť pokuta: {k}")
        v[-1] += (d2 - d1) + ((m2 - m1) * 30)
        if m1!=m2 and d1>d2:
            v[-1] -= d1


print(f"Najpožičiavanejšia kniha je: {sv}")

val = list(data.values())
val.sort(key=lambda x: x[-1], reverse=True)
for l in val:
    print(str(val.index(l)+1)+".",l)

