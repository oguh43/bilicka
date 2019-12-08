from random import randint
def ask():
    x = str(input("1) Pankrac\n2) Tajna sprava\n3) Sedi mucha na stene\n4) Alergia\n"))
    if x == "1":
        pankrac()
    elif x == "2":
        tajna()
    elif x == "3":
        mucha()
    elif x == "3":
        alergia()

def pankrac():
    y = str(input("Veta? ")).split(" ")
    ls = []
    ls1 = []
    nn = 0
    for i in range(0, len(y)):
        if y[i].istitle() == True: ls.append(y[i].swapcase())
        elif y[i].isupper() == True:
            sp = y[i] #make list()
            sp = list(sp)
            for n in sp: #remove nn
                if nn == 0:
                    ls1.append(n.swapcase())
                    nn = nn + 1
                else: ls1.append(n)
            ls.append("".join(ls1))
        else: ls.append(y[i])
    print(" ".join(ls))



def tajna():

    x = list(str(input("Veta?")))
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


def mucha():
    p = str(input("Pismeno?"))
    x = list(str(input("Veta?")))
    ls = []
    for i in x:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u": print(p, end = "")
        elif i == "A" or i == "E" or i == "I" or i == "O" or i == "U": print(p.upper(), end = "")
        else: print(i, end = "")


def alergia():
    a = list(str(input("Veta?")))
    for n in a:
        if n.isalpha() == True or n == " ": print(n, end = "")




ask()



