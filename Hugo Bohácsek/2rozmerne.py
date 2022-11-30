from random import randint

i = int(input())
j = int(input())

f = [[randint(1,100) for _ in range(i)] for q in range(j)]

print(f)