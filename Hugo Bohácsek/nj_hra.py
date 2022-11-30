cislo = int(input("Číslo? > "))

for i in range(1,101):
    if i == cislo or cislo % i == 0 or sum(map(int, list(str(i)))) == cislo or str(cislo) in list(str(i)):
        print("*")
    else:
        print(i)
