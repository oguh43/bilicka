while not ((x:=[]) if "x" not in globals().keys() else "") and (i:=input("Dáta? > ")) != "" and not x.append(float(i.split(" ")[-2].replace(",", "."))):
    pass
print(len(x),max(x))

# M01 2005.02.10 06:00 +10,3 PO
