from random import shuffle
veta = input("Vetník? > ")

num1 = 0
num2 = 0

while num1 * num2 < len(veta):
    num1 += 1
    num2 += 1

print(f"Size: {num1=}; {num2}, {len(veta)}")

fin = [["" for _ in range(0, num2)] for _ in range(0, num1)]
for i in range(0, num1):
    for j in range(0, num2):
        try:
            fin[i][j] = veta[i * num1 + j]
        except IndexError:
            print(i*num1+j)
            pass

if len(set(fin[-1])) == 1:
    fin.pop()

for i in fin:
    print(i)
shuffle(fin)
print("\n", end="")
for i in fin:
    print(i)




















