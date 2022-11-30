m = [[__import__("random").randint(1,100) for _ in range(3)] for q in range(3)]
o = [[0 for _ in range(len(m[0]))] for _ in range(len(m))]

for i in range(len(m)):
    for j in range(len(m[i])-1,-1,-1):
        print(i,j)
        o[j][i] = m[i][j]

def pprint(q):
    for i in q: print(i)
    print()

pprint(m)
pprint(o)

