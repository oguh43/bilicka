
with open("subory/lipsum.txt", "r") as f:
    q = f.read()

e = " ".join(list(q)[::2])
o = " " + " ".join(list(q)[1::2])
with open("subory/out/o1.txt","w+") as f:
    f.write(e)
with open("subory/out/o2.txt","w+") as f:
    f.write(o)
