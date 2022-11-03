ls = []
while True:
    inp = int(input("Známka? > "))
    if inp == 0:
        break
    ls.append(inp)

mn = 100000000000000
mx = 0
for i in ls:
    if i > mx:
        mx = i
    if mn > i:
        mn = i


print(f"Priemer: {(sum(ls)-mx-mn)/(len(ls)-2)}")

