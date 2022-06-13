plocha = "#" * 25
kola = 0
hrac = "0"
while True:
    print("\n 12345")
    for i in range(0,25,5):
        print(str(i//5+1)+plocha[i:i+5])
    if kola >= 2:
        vyhra = input("Vyhra? (a/n): ")
        if vyhra == "a":
            break
    print("Na rade je hrac "+hrac)
    x = int(input("Zadaj x-ovu suradnicu: "))
    y = int(input("Zadaj y-ovu suradnicu: "))
    plocha = plocha[:(y*5-(5-x))-1] + hrac + plocha[(y*5-(5-x)):]
    kola = kola + 1
    if hrac == "0":
        hrac = "X"
    else:
        hrac = "0"
        
if hrac == "0":
    hrac = "X"
else:
    hrac = "0"
print("-------> Vyhral "+hrac+" <-------")
