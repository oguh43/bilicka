def u14():
    inp = str(input("> "))
    print(inp[::2])
    print(inp[1::2])

def u15():
    inp = str(input("> "))
    for i in range(0,len(inp)):
        print(inp[0:i+1].rjust(len(inp)+1,"."))

def u16():
    inp = str(input("> "))
    for i in range(0,len(inp)):
        print(inp[0:i+1].rjust(len(inp)+1,".")+inp[0:i+1].ljust(len(inp)+1,"."))

def u17():
    inp = str(input("> "))
    mail = {
        "meno": inp.split("@")[0],
        "domeny": inp.split("@")[1]
    }
    print(f"TLD: .{mail['domeny'].split('.')[-1]}")
    print(f"Server: {mail['domeny']}")
    print(f"User: {mail['meno']}")
    print("Domény:")
    for domena in mail["domeny"].split(".")[::-1]:
        print(f"Doména {mail['domeny'].split('.')[::-1].index(domena)+1}. úrovne je: {domena}")

def u18():
    inp = str(input("Rodné číslo: ")).split("/")[0]
    a = [inp[i:i+2] for i in range(0,len(inp),2)]
    print(f'Dátum narodenia: {a[-1]}.{a[-2] if int(a[-2])<13 else str(int(a[-2])-50)}.{str("19"+a[0]) if int(a[0])>22 else str("20"+a[0])}')
    print(f'Pohlavie: {"Žena" if int(a[-2])>13 else "Muž"}')

def u19():
    inp = str(input("> ")).replace("://","/").split("/")
    print(f'a) {inp[0]}')
    print(f'b) {inp[1].split(".")[-1]}')
    print(f'c) {inp[1]}')

def u20():
    small = [chr(i) for i in range(97,123)]
    for _ in range(8):
        print(__import__("random").choice(small),end="")

def u21():
    from random import choice
    small = [chr(i) for i in range(97,123)]
    big = [chr(i) for i in range(65,91)]
    num = [chr(i) for i in range(48,58)]
    for _ in range(3):
        print(choice(big),end="")
    for _ in range(2):
        print(choice(num),end="")
    for _ in range(3):
        print(choice(small),end="")

def u22():
    from random import randint, choice
    small = [chr(i) for i in range(97,123)]
    pasw = [choice(small) for _ in range(8)]
    for _ in range(randint(1,len(pasw))):
        temp = randint(0,len(pasw)-1)
        pasw[temp] = pasw[temp].upper()
    print("".join(pasw))

def u23():
    print(", ".join([chr(i) for i in range(97,123)]))

def u24():
    print(", ".join([chr(i) for i in range(48,58)]))
    for i in range(10):
        print(str(str(i)+", ") if i != 9 else i,end="")

def concat_names():
    name1 = input("> ")
    name2 = input("> ")
    if len(name1)!=len(name2):
        print("ERR! Names must be the same length!")
        __import__("sys").exit(1)
    print("".join([name1[i:i+1]+name2[i:i+1] for i in range(len(name1))]))
