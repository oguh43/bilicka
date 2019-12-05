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

pankrac()