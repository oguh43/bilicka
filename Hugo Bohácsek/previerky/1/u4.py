ls = []
for i in range(1000,10000):
    flag = True
    for j in range(0,2):
        if str(i)[j] != str(i)[-(j+1)]:
            flag = False
           
    if flag:
        ls.append(i)
print(ls)