from random import choice as čoice

with open("./obesenec.txt","r") as f:
    slouko = čoice(f.readlines()).replace("\n","")

uhadnuc = "."*len(slouko)
print(uhadnuc)
skore = 10
while skore >= 0 and uhadnuc != slouko:
    q = input("Pismenko veducko> ")
    if q in slouko:
        indices = [i for i, x in enumerate(list(slouko)) if x == q]
        for y in indices:
            print(y)
            if y == 0:
                uhadnuc = uhadnuc[0:0] + q + uhadnuc[y+1:]
            else:
                uhadnuc = uhadnuc[0:y] + q + uhadnuc[y+1:]
    else:
        skore -= 1
    print(uhadnuc)

if skore >= 0:
    print("Si zabiu")
else:
    print("Si bou zabity")

#1) šicke sa dojebe
#2) pojde ale musi uhadnuc medzeru
#3) šicke sa dojebe
