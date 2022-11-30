from random import choice
kola = int(input("Počet kôl? > "))

t = ["k","p","n"]

stat = [0,0]

for i in range(1, kola + 1):
    print(f"Kolo {i}")
    tah = input("(K)ameň, (P)apier, (N)ožnice? > ")[0].lower()
    pc = choice(t)
    if pc == tah:
        print("Draw!")
        stat[0] += 1
        stat[1] += 1
    elif (pc == "k" and tah == "p") or (pc == "p" and tah == "n") or (pc == "n" and tah == "k"):
        print("PC prehral!")
        stat[0] += 1
    elif (pc == "k" and tah == "n") or (pc == "p" and tah == "k") or (pc == "n" and tah == "p"):
        print("PC vyhral!")
        stat[1] += 1
    print(f"PC: {pc}\nUSER: {tah}") 

print("\nŠtatistiky:")
print(f"PC: {stat[1]}\nUSER: {stat[0]}")








