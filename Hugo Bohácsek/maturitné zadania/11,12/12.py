from random import randint

tp = [randint(1,49) for _ in range(6)]

with open("./loteria_2.txt", "r") as f:
    data = [map(int, x.split(" ")) for x in f.read().splitlines()]


res = {x:0 for x in range(0,7)}


for line in data:
    cor = 0
    for guess in line:
        if guess in tp:
            cor += 1
    res[cor] += 1
print(res)

inp = list(map(int, input("Čiselka? >").split(" ")))
correct = []
for i in inp:
    if i in tp:
        correct.append(i)
print(f'Správne: {correct=}')
