[globals().update({"inp": input("Num?> ").split(" "), "res": 0})] + [globals().update({"res": globals()["res"] + int(globals()["inp"][0][-1-i] if globals()["inp"][0][-1-i] in list(map(str, range(0, 10))) else (ord(globals()["inp"][0][-1-i]) - 55)) * (int(globals()["inp"][1]) ** i)}) for i in range(0, len(globals()["inp"][0]))] + [print(f'({globals()["inp"][0]}){globals()["inp"][1]} = ({globals()["res"]})10')]