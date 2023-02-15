


from collections import Counter


a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

inp = input("Vetník? > ")


new = ""

for char in inp:
    if char == " ":
        new += "0 "
        continue
    print(char, a.index(char)//3)
    new += str(a.index(char)//3+1)+str(a.index(char)//3+1)*(a.index(char)%3)+" "
print (new)

c = Counter(new.replace(" ",""))
print(c)



























