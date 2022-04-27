import os
from random import choice

target = int(input("Zadaj cielové číslo: "))
p1 = 0
p2 = 0
p2_type = input("Zadaj typ hráča 2 (ai/person): ").lower()

win_map = {
    "r":{
        "p": False,
        "s": True
    },
    "p":{
        "r": True,
        "s": False
    },
    "s":{
        "r": False,
        "p": True 
    }
}

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    inp1 = input("(R)ock, (P)aper, (S)cissors: ").lower()
    cls()
    inp2 = input("(R)ock, (P)aper, (S)cissors: ").lower() if p2_type == "person" else choice(["r", "p", "s"])
    cls()
    
    if inp1 == inp2:
        print("Remíza")
    else:
        if win_map[inp1][inp2]:
            print("Vyhral hráč 1")
            p1 += 1
        else:
            print("Vyhral hráč 2")
            p2 += 1
    if p1 == target:
        print(f'Celkovo vyhral hráč 1 ({p1}:{p2})')
        break
    if p2 == target:
        print(f'Celkovo vyhral hráč 2 ({p1}:{p2})')
        break

