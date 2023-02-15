from random import randint

otazky = [i for i in range(1, int(input("Počet otázok?> ")) + 1 )]
ziaci = [i for i in range(1, int(input("Počet žiakov?> ")) + 1 )]

if len(ziaci) > len(otazky):
    print("Neni dobrô :(")
    __import__("sys").exit()

for ziak in ziaci:
    el = otazky.pop(randint(0, len(otazky) - 1))
    print(f'Ziak {ziak}: {el}')
