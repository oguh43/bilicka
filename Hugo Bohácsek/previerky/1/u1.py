inp = list(map(int,list(input("Číselko? > "))))
s = 0
for i in inp:
    if i % 2 == 0:
        s += i

print(f"Súčet je {s}")
