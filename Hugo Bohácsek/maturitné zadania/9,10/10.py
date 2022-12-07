from random import choice
inp = ["((xx)y(xx))", "(aa))bb(", "(((()"][0]
def check(inp):
    b = 0
    for c in inp:
        if c == "(":
            b += 1
        elif c == ")":
            b -= 1
        if b < 0:
            return False
    if b != 0:
        return False
    return True

def colorCode(inp):
    if not check(inp):
        return {}
    data = {}
    ls = []
    for i in range(0, len(inp)):
        char = inp[i]
        if char == "(":
            data[i] = -1
            ls.append(i)
        elif char == ")":
            data[ls.pop()] = i
    return data



from tkinter import *

data = colorCode(inp)

colors = ["red","green","blue","cyan","pink","orange","violet"]
cS = {}
cE = {}
for k,v in data.items():
    cl = colors.pop(colors.index(choice(colors)))
    cS[k] = cl
    cE[v] = cl

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="480", height="520")
canvas.pack()
x = 50
for i in range(0, len(inp)):
    char = inp[i]
    x += 30
    if i in cS.keys():
        canvas.create_text(x,50,text=char,font=("Purisa", 50),fill=cS[i])
    elif i in cE.keys():
        canvas.create_text(x,50,text=char,font=("Purisa", 50),fill=cE[i])
    else:
        canvas.create_text(x,50,text=char,font=("Purisa", 50))

root.mainloop()








