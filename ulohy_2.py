import re
import sys
import time
from random import randint
from itertools import permutations
def ask():
    x = str(input("\n1) Pankrac\n2) Tajna sprava\n3) Sedi mucha na stene\n4) Alergia\n5) Rigorozka\n6) Statisticky urad\nPre ukoncenie stlacte ENTER\n>"))
    if x == "1":
        pankrac()
    elif x == "2":
        tajna()
    elif x == "3":
        mucha()
    elif x == "4":
        alergia()
    elif x == "5":
        rigorozka()
    elif x == "6":
        statistika()
    elif x == "":
        sys.exit()
    else:
        print(x,"is not a valid character, please try again")
        ask()


def pankrac():
    y = str(input("Veta?\n>")).split(" ")
    ls = []
    ls1 = []
    nn = 0
    for i in range(0, len(y)):
        if y[i].istitle() == True: ls.append(y[i].swapcase())
        elif y[i].isupper() == True:
            sp = list(y[i])
            for n in sp:
                if nn == 0:
                    ls1.append(n.swapcase())
                    nn = nn + 1
                else: ls1.append(n)
            ls.append("".join(ls1))
        else: ls.append(y[i])
    print(" ".join(ls))
    print(" ".join([word[0].lower()+word[1:].upper() if word[0].isupper() else word for word in input("Sentence?\n>>> ").split(" ")]))
    time.sleep(1)
    ask()


def tajna():
    x = list(str(input("Veta?\n>")))
    count = -1
    popls = []
    for i in x:
        count = count + 1
        if i == " ": popls.append(count)
    plusindex = 0
    for i in popls:
        x.pop(i + plusindex)
        plusindex = plusindex-1
    append_num = len(popls)
    for i in range(0,append_num): x.insert(randint(1,len(x)-1)," ")
    print("".join(x))
    time.sleep(1)
    ask()


def mucha():
    p = str(input("Pismeno?\n>"))
    x = list(str(input("Veta?\n>")))
    for i in x:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u": print(p, end = "")
        elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U": print(p.upper(), end = "")
        else: print(i, end = "")
    time.sleep(1)
    ask()


def alergia():
    a = list(str(input("Veta?\n>")))
    for n in a:
        if n.isalpha() == True or n == " ": print(n, end = "")
    time.sleep(1)
    ask()


def rigorozka():
    x = permutations(str(input("Text?\n>")).split(" "))
    for i in x: print(" ".join(i))
    time.sleep(1)
    ask()


def statistika():
    text = str(input("Veta?\n>")).upper()
    letters = {}
    for i in re.findall(r"\w", text):
        if i not in letters: letters[i] = 1
        else: letters[i] += 1
    SortedByCount = dict(sorted(letters.items(), key = lambda x: x[1], reverse = True))
    print(" ".join(SortedByCount.keys()))
    time.sleep(1)
    ask()


ask()
