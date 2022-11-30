zac = input("Číselko? > ")
num = int(zac) + 1
while True:
    flag = True
    inp = str(num)
    for i in range(0,len(inp)//2):
        if inp[i] != inp[-(i+1)]:
            flag = False
    if flag:
        print(f'Vytachometroval som čísielko {num}')
        break
    num += 1


