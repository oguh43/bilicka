
with open("./skok_do_dialky.txt", "r") as f:
    data = f.read().split("\n")
states = {}
db = {}
mx = -999
for line in data:
    line = line.split(" ")
    db[line[0]] = {
        "state": line[1],
        "pokusy": list(map(int, line[2:]))
    }
    db[line[0]]["max"] = max(db[line[0]]["pokusy"])
    if line[1] not in states.keys():
        #states[line[1]] = []
        states[line[1]] = 0
    #states[line[1]].append(line[0])
    states[line[1]] += 1
    if db[line[0]]["max"] > mx:
        mx = db[line[0]]["max"]

winners = []
for k, v in db.items():
    if v["max"] == mx:
        winners.append(k)

print("States: ", states)
print("Winner(s):", winners)
