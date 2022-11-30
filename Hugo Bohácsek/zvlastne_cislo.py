c = input("Číslo? > ")
p = int(c[0]+c[1])
v = int(c[2]+c[3])

if (p+v) ** 2 == int(c):
    print("Číslo je zvláštne")
else:
    print("Číslo nie je zvláštne")
