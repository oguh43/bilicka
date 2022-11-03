from random import randint
pocet = int(input("Počet? > "))
d = 0

for i in range (pocet):
    r1 = randint(1,10)
    r2 = randint(1,10)
    if int(input(f"{r1}*{r2}? > ")) == r1 * r2:
        d += 1

print(f'Úspešnosť: {(d/pocet)*100}%')



