with open("pacienti.txt", "r") as f:
    data = [x.split(" ") for x in f.read().splitlines()]

for i in range(len(data)):
    data[i][2] = input(f'{data[i][0]} hmotnosť? > ')

for i in range(len(data)):
    data[i][4] = str(int(data[i][2]) / (float(data[i][3].replace(",",".")) ** 2))

ob = 0
žen = 0
for line in data:
    if float(line[-1]) > 30:
        ob +=1
    elif float(line[-1]) < 18.5:
        if int(line[1][2]) > 2:
            žen += 1

print(f'Obéznych: {ob}\nPodváha: {žen}')
