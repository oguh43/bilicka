inp = ["((xx)y(xx))", "(aa))bb(", "(((()"]
def check(inp):
    b = 0
    for c in inp:
        if c == "(":
            b += 1
        elif c == ")":
            b -= 1
        if b < 0:
            return "Zle"
    if b != 0:
        return "Zle"
    return"Dobre"


for i in inp:
    print(check(i))