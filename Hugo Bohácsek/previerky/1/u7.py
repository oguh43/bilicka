ls = []

for c in range (1,1000):
    flag = True
    for i in range(2, c // 2 + 1):
        if c % i == 0:
            flag = False
    if flag:
        ls.append(c)

fl = []

for i in range(len(ls)-1):
    if ls[i] + 2 == ls[i+1]:
        fl.append([ls[i],ls[i+1]])
    if i + 2 == len(ls):
        continue
    if ls[i] + 2 == ls[i+2]:
        fl.append([ls[i],ls[i+2]])

print(fl)