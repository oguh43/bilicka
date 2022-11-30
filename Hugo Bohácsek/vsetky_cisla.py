mx = int(input("Max? > "))

perf = []
zvl = []
arm = []

for cislo in range(1,mx):

    delitele = []

    for i in range(1, cislo):
        if cislo % i == 0:
            delitele.append(i)
    if sum(delitele) == cislo:
        perf.append(cislo)
    
    cislo = str(cislo)
    if len(str(cislo)) == 4:
        p = int(cislo[0]+cislo[1])
        v = int(cislo[2]+cislo[3])

        if (p+v) ** 2 == int(cislo):
            zvl.append(cislo)

    cisla = [int(x) ** 3 for x in cislo]
    if sum(cisla) == int(cislo):
        arm.append(cislo)

print(f"Perfektné: {', '.join(map(str,perf))}")
print(f"Zvláštne: {', '.join(map(str,zvl))}")
print(f"Armstrongove: {', '.join(map(str,arm))}")
