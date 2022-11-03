from random import randint
from copy import deepcopy
def u1():
    ls = [randint(0,100)]

    for _ in range(9):
        temp = randint(0,100)
        flg = False
        for i in range(0,len(ls)):
            if flg: continue
            if temp <= ls[i]:
                flg = True
                ls.insert(i,temp)
        if not flg:
            ls.append(temp)

    inp = int(input("Číselko? > "))

    for i in range(0,len(ls)):
        if len(ls) > 10: continue
        if inp <= ls[i]:
            ls.insert(i, inp)
    if len(ls) == 10:
        ls.append(inp)

    print(", ".join(map(str,ls)))

def u2():
    ls = [f'Dieťa č.{x+1}' for x in range(int(input("Počet detí? > ")))]
    org = deepcopy(ls)
    vypadnut = int(input("Koľko detí vypadne? > "))
    zaciatok = int(input("Od koľkého dieťaťa? > "))
    pk = int(input("Po koľko ideme? > "))
    vypadnute = []

    c = zaciatok
    for i in range(vypadnut):
        vypadnute.append(ls.pop(c))
        c += pk

    print(f'Originálne pole: {", ".join(org)}\nPole teraz: {", ".join(ls)}\nVypadnuté deti: {", ".join(vypadnute)}')

def u3():
    ls = []
    while len(ls) < 10:
        tmp = randint(1,80)
        if tmp not in ls:
            ls.append(tmp)

    hadane = [int(input("Číselko? > ")) for _ in range(10)]
    vklad = int(input("Výška vkladu? > "))

    c = 0
    for i in hadane:
        if i in ls:
            c += 1

    v = {
        0: 1,
        5: 3,
        6: 10,
        7: 20,
        8: 500,
        9: 10000,
        10: 200000
    }

    if c in v.keys():
        vklad *= v[c]

    print(f"Vaša výhra: {vklad}\nPočet uhádnutých: {c}")

def u4():
    ls = []
    while len(ls) < 10:
            tmp = randint(1,20)
            if tmp not in ls:
                ls.append(tmp)

    for i in ls:
        flg = True
        for q in range(ls.index(i), len(ls)):
            j = ls[q]
            if i > j:
                pass
            else:
                if i != j:
                    flg = False
        if flg:
            print(f'Čísleko: {i}\nNa indexe: {ls.index(i)}')
    print(f'List bol: {", ".join(map(str,ls))}')

def u5():
    ls = []
    while len(ls) < 10:
        tmp = randint(1,20)
        if tmp not in ls:
            ls.append(tmp)

    n = 0
    mp = {}

    for i in range(0,len(ls)):
        flag = True
        n = 0
        for j in range(i, len(ls)-1):
            if not flag: continue
            if ls[j] < ls[j+1]:
                n += 1
            else:
                flag = False
        mp[i] = n

    for k,v in mp.items():
        print(f'Index: {k}\tDĺžka: {v}')

    print(f'List: {", ".join(map(str,ls))}')

def u6():
    ls1 = [randint(0,10) for _ in range(15)]
    ls2 = [randint(0,10) for _ in range(15)]

    s1 = 0
    s2 = 0
    for i in range(0, 10):
        s1 += ls1[i]
        s2 += ls2[i]

    print("Družstvo1:")
    for i in ls1:
        print(i)

    print("Družstvo2:")
    for i in ls2:
        print(i)

    print(f'Priemer družstva1: {s1/10}\nPriemer družstva1: {s2/10}\nVyhráva družstvo: {1 if s1>s2 else 2}')

def u7():
    ls = [randint(0,50) for _ in range(15)]
    print(f'List: {", ".join(map(str,ls))}')
    for i in ls:
        if str(i)[-1] in ["0","5"]:
            print(ls.index(i))
            break

def u8():
    ls1 = [randint(0,50) for _ in range(randint(15,30))]
    ls2 = [randint(0,50) for _ in range(randint(15,30))]
    p = 0
    for i in ls2:
        if i not in ls1:
            p += 1

    print(f'Počet je: {p}')


u = int(input("Ktorá úloha? > "))
if u == 1:
    u1()
elif u == 2:
    u2()
elif u == 3:
    u3()
elif u == 4:
    u4()
elif u == 5:
    u5()
elif u == 6:
    u6()
elif u == 7:
    u7()
elif u == 8:
    u8()
