from random import randint

ls = [randint(1,5) for _ in range(100)]
mxk = []
mx = 0
for i in range(len(ls)):
    if mx == 5:
        continue
    if ls[i] > mx:
        mx = ls[i]

for i in range(len(ls)):
    if ls[i] == mx:
        mxk.append(i)

print(f'Maximum je: {mx}\nJe ich: {len(mxk)}\nNa indexoch: {", ".join(map(str,mxk))}')
