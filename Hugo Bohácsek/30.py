
with open("obr1.txt", "r") as f:
    data = f.read().splitlines()
    velkost = data.pop(0)
    data = [list(x) for x in data]


def spracuj_riadok(line: str) -> str:
    buf = "" if line[0] == "0" else "0 "
    cur = ""
    count = 1
    flag = False
    while line:
        cur = line[0]
        count = 1
        flag = False
        for i in range(len(line)):
            if flag:
                continue
            if line[i] == cur:
                count += 1
            else:
                flag = True
        if len(buf) == 0:
            count -= 1
        elif len(buf) == 2 and buf[0] == "0":
            count -= 1
        buf += f"{str(count)} "
        line = line[count:]
    return buf


data = [spracuj_riadok(x) for x in data]

with open("kom_o.txt", "w+") as f:
    f.write(velkost+"\n")
    f.write("\n".join(data))


