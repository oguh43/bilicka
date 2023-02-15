from random import choice

nums = list(map(str,list(range(1,10))))
code = [choice(nums)]
nums.insert(0,"0")
code = code + [choice(nums) for _ in range(7)]

print(code)

cc = ""

cc += str(sum(list(map(int, code[:4]))) % 2)
cc += str(sum(list(map(int, code[2:6]))) % 2)
cc += str(sum(list(map(int, code[4:]))) % 2)
code.append(str(int(cc, base=2)))

print("".join(code))

with open("kod_a.txt", "r") as f:
    data = [list(line) for line in f.read().splitlines()]


print(data)

for line in data:
    cc = ""
    cc += str(sum(list(map(int, line[:4]))) % 2)
    cc += str(sum(list(map(int, line[2:6]))) % 2)
    cc += str(sum(list(map(int, line[4:8]))) % 2)
    cc = str(int(cc, base=2))
    if cc != line[-1]:
        print(f'{"".join(line)} is invalid :( {cc=}')