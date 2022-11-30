with open("subory/mocniny.txt", "r") as f:
    print("\n".join(map(str,[int(x) * int(x) for x in f.read().split("\n")])))