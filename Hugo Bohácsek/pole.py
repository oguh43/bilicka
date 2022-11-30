from random import randint
ls = [randint(1,100) for _ in range(10)]
print(ls)

mx = 0
mn = 101
mxInd = 0
minInd = 0
for i in range(len(ls)):
    if ls[i] > mx:
        mx = ls[i]
        mxInd = i
    if ls[i] < mn:
        mn = ls[i]
        minInd = i

ls[minInd], ls[mxInd] = ls[mxInd], ls[minInd]




print(ls)
print(f'Maximum je: {mx}')
print(f'Minimum je: {mn}')

