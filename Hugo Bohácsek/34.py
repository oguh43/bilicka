with open("sub.txt", "r") as f:
    data = [x.split(" ") for x in f.read().splitlines()]

fin = {
    "januar":[],
    "februar":[],
    "marec":[],
    "april":[],
    "maj":[],
    "jun":[],
    "jul":[],
    "august":[],
    "september":[],
    "oktober":[],
    "november":[],
    "december":[]
}
mp = ["januar","februar","marec","april","maj","jun","jul","august","september","oktober","november","december"]


for person in data:
    m = int(person[0][2:4])
    if m > 12:
        m -= 50
    fin[mp[m-1]].append(f'{person[0][4:]}. {m}. 19{person[0][:2]} {person[1]} {person[2]}')

for k,v in fin.items():
    val = "\n".join(v)
    print(f'{k}:\n{val}' if len(val) > 0 else f"{k}:")
