inp = [{"on":int(input("Nástup? > ")), "off":int(input("Výstup? >")), "name":input("Meno zastávky?")} for _ in range(4)]

highest = 0
def printTravelers(inp, highest):
    p = 0
    for z in inp:
        buf = f"Pred zastávkou \"{z['name']}\"\n"
        buf += f"Pred nástupom: {p}\nPo nástupe: {p+z['on']}\nPo výstupe: {p+z['on']-z['off']}\n####################################"
        if p > highest:
            highest = p
        p = p+z['on']-z["off"]
        print(buf)
    return highest
highest = printTravelers(inp, highest)

def recommend(highest):
    smol = 20
    normal = 30
    print("Odporúčaný typ električky: ", end="")
    if highest <= smol:
        print("Smol")
    elif highest <= normal:
        print("Normal")
    else:
        print("Biž")
recommend(highest)

def ticket(inp):
    buf = ""
    for z in inp:
        if z["on"] >= 10:
            buf += f"Zastávka \"{z['name']}\" potrebuje automat.\n"
    if buf == "":
        print("Automaty nie sú potrebné")
    else:
        print(buf)
ticket(inp)

def znamenie(inp):
    buf = ""
    for z in inp:
        if z["on"] < 3 and z["off"] < 3:
            buf += f"Zastávka \"{z['name']}\" by mala byť na znamenie.\n"
    if buf == "":
        print("Zastávky na znamenie nie sú potrebné.")
    else:    
        print(buf)

znamenie(inp)
