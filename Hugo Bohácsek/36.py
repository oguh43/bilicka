from tkinter import *

with open("vytazenost_autobus.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()
    capacity = int(data.pop(0))

index = 0
fl = 0
x = 50
y = 10

def render(evt: Event) -> None:
    global fl, y, index
    if index == len(data):
        return

    current = data[index].split(" ")
    plus = int(current[0])
    minus = int(current[1])
    fl += plus
    fl -= minus
    amm = ((capacity / 100) * fl) * 4

    canvas.create_text(x,y+10,text=current[2])
    if index != len(data) - 1:
        canvas.create_rectangle(x+50,y,x+150,y+25)
        canvas.create_rectangle(x+51,y+1,x+51+amm,y+24,fill="green" if amm < capacity*2 else "red")
    y += 30
    index += 1

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="700", height="500")
canvas.pack()

root.bind("<space>", render)

root.mainloop()
