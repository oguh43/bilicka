nosnost = int(input("Nosnosť? > "))
veci = []
while True:
    item = int(input("Vec? > "))
    if sum(veci) + item > nosnost:
        break
    veci.append(item)

print(f"Dosiahnutá hmotnosť: {sum(veci)}/{nosnost}\nPočet vecí: {len(veci)}\nVeci: {', '.join(map(str,veci))}")
