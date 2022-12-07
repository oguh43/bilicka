with open("meteo_stanice.txt", "r") as f:
    data = f.read().splitlines()

print(len(data))
for l in data:
    print(l.split(" ")[3])
mx = -999999
d = ""
for l in data:
    if float(l.split(" ")[3].replace(",",".") if l.split(" ")[3][0] == "-" else l.split(" ")[3].replace(",",".")[1:]) > mx:
        mx = float(l.split(" ")[3].replace(",",".") if l.split(" ")[3][0] == "-" else l.split(" ")[3].replace(",",".")[1:])
        d = f'{l.split(" ")[3]}:{l.split(" ")[4]}'

print(d)
avg = []
for l in data:
    avg.append(float(l.split(" ")[3].replace(",",".") if l.split(" ")[3][0] == "-" else l.split(" ")[3].replace(",",".")[1:]))
print(sum(avg)/len(avg))


