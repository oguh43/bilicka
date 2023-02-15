with open("cyklovylety.txt", "r") as f:
    data = [x.split(" ") for x in f.read().splitlines()]

for line in data:
    print(f'{line[0]} {line[1]} {str(int(line[2]) // 60)+":"+str(int(line[2]) % 60) if len(str(int(line[2]) % 60))>1 else str(int(line[2]) // 60)+":"+"0"+str(int(line[2]) % 60)} {float(line[1])/(int(line[2])/60)} {line[3]}')
