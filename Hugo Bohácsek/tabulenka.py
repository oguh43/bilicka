a = []
b = []
for i in range(1,11):
    for j in range (1,11):
        b.append(i*j)
    a.append(b)
    b = []
print(a)
a = [list(map(str,x)) for x in a]
