inp = input("Num?> ").split(" ")
res = 0
for i in range(0, len(inp[0])):
    res +=  int(inp[0][-1-i] if inp[0][-1-i] in list(map(str, range(0, 10))) else (ord(inp[0][-1-i]) - 55)) * (int(inp[1]) ** i)
print(f'({res}){inp[1]} = ({res})10')
org = res
num = res
res = ""

while num:
    if num % int(inp[2]) < 10:
        res += str(num % int(inp[2]))
    else:
        res += chr(num % int(inp[2]) + 55)
    num = num // int(inp[2])

res = res[::-1]

print(f'({org})10 = ({res}){inp[2]}')

