from random import randint
pc = randint(1,100)
pokus = 0
while True:
    inp = int(input("Číslo? > "))
    pokus += 1
    if inp == pc:
        break
    elif inp < pc:
        print("Väčšie")
    else:
        print("Menšie")
print(f"Hádané číslo bolo: {pc}\nTrvalo Vám to {pokus} pokusov.")
