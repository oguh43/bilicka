f = open("1.txt","r")
inp = f.readlines()
f.close()

up = 1

for i in range(1,len(inp)):
    if inp[i] > inp[i-1]:
        up += 1
print(up)
