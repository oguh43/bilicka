cislo = input("Číslo? > ")
cisla = [int(x) ** 3 for x in cislo]
if sum(cisla) == int(cislo):
    print("Číslo je Armstrongove!")
else:
    print("Číslo nie je Armstrongove!")
