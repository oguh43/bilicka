from random import randint

c = 0
for i in range(1000):
    if randint(1,6)==6 and 6 == randint(1,6):
        c += 1
print(c)

print(c/1000*100)




