with open("financie.txt", "r") as f:
    data = [x.split(" ") for x in f.read().splitlines()]

mp = {
    1: ["","jeden","dva","tri","štyri","päť","šesť","sedem","osem","deväť"],
    10: ["","jede","dva","tri","štr","pät","šest","sedem","osem","devät"],
    20: ["","","dva","tri","štyri","päť","šesť","sedem","osem","deväť"],
    100: ["","","dve","tri","štyri","päť","šesť","sedem","osem","deväť"]
}

sm = ["0",0]

for line in data:
    sm[1] += int(line[-1])
    print(f'{line[0]} {line[1]} {((mp[1][int(line[1][1])]+"násť"+"tisíc") if line[1][0] == "1" else (mp[1][int(line[1][0])]+"dsať"+mp[1][int(line[1][1])]+"tisíc")) if len(line[1]) == 5 else ""}{mp[100][int(line[1][0])]+"tisíc" if 5 > len(line[1]) > 3 else ""}{mp[100][int(line[1][-3])]+("sto" if line[1][-3] != "0" else "") if len(line[1]) >= 3 else ""}{mp[20][int(line[1][-2])]+("dsať" if line[1][-2] in ["2","3","4"] else "desiat" if line[1][-2] not in ["0","1"] else "") if len(line[1]) >= 2 else ""}{((mp[1][int(line[1][-1])] if line[1][-2] == "0" else mp[10][int(line[1][-1])]+"násť") if line[1][-2] in ["0","1"] else mp[1][int(line[1][-1])]) if len(line[1]) > 1 else mp[1][int(line[1][0])]}')

sm[1] = str(sm[1])
sm = [sm]

for line in sm:
    print(f'Spolu: {line[1]} {((mp[1][int(line[1][1])]+"násť"+"tisíc") if line[1][0] == "1" else (mp[1][int(line[1][0])]+"dsať"+mp[1][int(line[1][1])]+"tisíc")) if len(line[1]) == 5 else ""}{mp[100][int(line[1][0])]+"tisíc" if 5 > len(line[1]) > 3 else ""}{mp[100][int(line[1][-3])]+("sto" if line[1][-3] != "0" else "") if len(line[1]) >= 3 else ""}{mp[20][int(line[1][-2])]+("dsať" if line[1][-2] in ["2","3","4"] else "desiat" if line[1][-2] not in ["0","1"] else "") if len(line[1]) >= 2 else ""}{((mp[1][int(line[1][-1])] if line[1][-2] == "0" else mp[10][int(line[1][-1])]+"násť") if line[1][-2] in ["0","1"] else mp[1][int(line[1][-1])]) if len(line[1]) > 1 else mp[1][int(line[1][0])]}')
