cislo = int(input("Číslo? > "))
delitele = []

for i in range(1, cislo):
    if cislo % i == 0:
        delitele.append(i)
if sum(delitele) == cislo:
    print("Číslo je perfektné!")
else:
    print("Číslo nie je perfektné!")