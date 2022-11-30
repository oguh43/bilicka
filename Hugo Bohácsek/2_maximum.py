from random import randint

ls = [randint(1,100) for _ in range(100)]

mx = 0
mx2 = 0

for i in ls:
    if mx < i:
        mx = i
for i in ls:
    if mx2 < i < mx:
        mx2 = i

print(f'Maximun je: {mx}\nDruhé maximum je: {mx2}')
