c = int(input("Čísielko? > "))
flag = True
for i in range(2, c // 2 + 1):
    if c % i == 0:
        flag = False

if flag:
    print("Je prvočíslo.")
else:
    print("Nie je prvočíslo.")


mn = int(input("Začiatok? > "))
mx = int(input("Konec? > "))
ls = []
cur = mn
while True:
    flag = True
    for i in range(2, cur // 2 + 1):
        if cur % i == 0:
            flag = False
    if flag:
        ls.append(cur)
    cur += 1
    if cur > mx:
        break
print(f'Prvočísielka v intervale sú: {", ".join(map(str,ls))}')