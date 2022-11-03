
inp = int(input("Číselko? > "))
p = 0
for i in range(inp+1, 2*inp-2):
    flag = True
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            flag = False
    if flag:
        p+=1

print(p)



