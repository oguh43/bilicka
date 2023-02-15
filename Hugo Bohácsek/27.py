from random import randint

mp = [[randint(1,2) for __ in range(5)] for _ in range(5)]





while True:
    for line in mp:
        print(line)
    x = int(input("X>"))
    y = int(input("Y>"))
    z = int(input("Z>"))
    mp[y][x] += z
    if len(set([item for sublist in mp for item in sublist])) == 1:
        break


for line in mp:
    print(line)


print("Hotovo")