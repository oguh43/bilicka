zaklad = int(input("Základ? > "))
pridavok = int(input("Prídavok? > "))
t = 52

s = 0
for i in range(0, t):
    s += zaklad + (pridavok * i)
    print(zaklad + (pridavok * i))
print(f"Celkovo {s}")


