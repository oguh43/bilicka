from random import randint
matica = [[randint(1,100) for _ in range(10)] for q in range(10)]
mx = -1
mxI = {}
mnI = {}
mn = 9000
for i in range(len(matica)):
    for j in range(len(matica[i])):
        if matica[i][j] > mx:
            mx = matica[i][j]
            mxI = {i:j}
        if matica[i][j] < mn:
            mn = matica[i][j]
            mnI = {i:j}

for i in matica:
    print(i)
matica[list(mxI.items())[0][0]][list(mxI.items())[0][1]], matica[list(mnI.items())[0][0]][list(mxI.items())[0][1]] = matica[list(mnI.items())[0][0]][list(mxI.items())[0][1]], matica[list(mxI.items())[0][0]][list(mxI.items())[0][1]]


print("######################")
for i in matica:
    print(i)
print(mxI,mnI)

