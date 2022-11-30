inp = list(input("Číselko? > "))
print(f'Najväčšia cifra je {max(inp)}!')

mx = 0
inp = map(int,inp)
for c in inp:
    if c > mx:
        mx = c
print(f'Najväčšia cifra je {mx}!')

