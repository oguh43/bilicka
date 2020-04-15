from random import *

def pos(test):    
    postupka = []
    temp = []
    dlzka = 0
    for i in test:
        if str(i).isdigit() == True:
            dlzka = dlzka +1
            temp.append(i)
        elif str(i).isdigit() == False and dlzka >= 3:
            dlzka = 0
            postupka.append(temp.copy())
            temp.clear()
        elif str(i).isdigit() == False and dlzka < 3:
            dlzka = 0
            temp.clear()
    if dlzka >= 3:
        postupka.append(temp)
    return postupka

def check_straight(test):
    test.sort()
    pl = test[0]
    for i in range(len(test)+8):
        try:
            if test[i] != pl:
                test.insert(i," ")
            pl = pl + 1
        except Exception:
            pass
    return pos(test)

def longest(test):
    ln = []
    for i in test:
        ln.append(len(i))
    if len(set(ln)) > 1:
        return test.index(max(test, key=len))
    else:
        return -1

def winner(after_ai,after_player):
    lon_ai = longest(after_ai)
    lon_pl = longest(after_player)
    if len(after_ai) > len(after_player) or len(after_ai[lon_ai]) > len(after_player[lon_pl]):
        return "ai"
    elif len(after_player) > len(after_ai) or len(after_player[lon_pl]) > len(after_ai[lon_ai]):
        return "player"
    mx_ai = after_ai[lon_ai][-1]
    mx_pl = after_player[lon_pl][-1]
    if mx_ai > mx_pl:
        return "ai"
    elif mx_pl > mx_ai:
        return "player"
    elif mx_pl == mx_ai:
        return "tie"

# Tu sa nachádza program na testovanie. Cyklus for je rozbitý, snaží sa odstraňovať neexistujúce indexy.
# Ako vidíme, netreba list dopredu sortovať, je to spravené za nás. Program môže dostať aj negatívne hodnoty,
# a aj hodnoty vyššie ako 12. Objekt ktorý sa vráti je list v liste, napr.: [[3, 4, 5, 6, 7], [9, 10, 11]].
# Prvú postupku vieme vybrať pomocou: check_straight(ai)[0] (viď. index). ak chceme najvyššiu, dáme index -1,
# Keďže program dáva najvyššie postupky na koniec.

ai = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(3):
    try:
        ai.pop(randint(0,len(ai)))
    except Exception:
        pass
shuffle(ai)
after = check_straight(ai)
print("check",after)

# Funkcia longest() vráti index najdlhšej postupky. Ak sú dve rovnaké, vráti tú väčšiu.
print(longest(after))

pl = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(3):
    try:
        pl.pop(randint(0,len(pl)))
    except Exception:
        pass
shuffle(pl)
aftr = check_straight(pl)
print(aftr)
print(winner(after,aftr))
# Funkcia winner určuje víťaza. Na konci jej programovania som zabudol čo robí, ale vyzerá že funguje,
# ak ju chcete použiť, radšej si ju sami odtestujte.

# Posledné. Kód používa import *, tzn.: nepoužívam random.shuffle() ale len shuffle. Ak máte import :
# from random import randint   jednoducho pridajte: from random import randint, shuffle
