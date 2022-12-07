
with open("./hlasovanie_1.txt", "r") as f:
    data = f.read().split("\n")
out = {}
for ind in range(len(data)):
    if data[ind] not in out.keys():
        out[data[ind]] = []
    out[data[ind]].append(ind)

for k,v in out.items():
    print(f'Číslo "{k}" dostalo {str(len(v))} hlasov')
    with open(f"{k}.txt","w+") as f:
        buf = ""
        for i in v:
            buf += f"{i}\n"
        f.write(buf)




