from tkinter import *

from random import randint


def change(num: int) -> None:
    globals()["buttons"][1]["text"] = str(int(globals()["buttons"][1]["text"]) + num)
    canvas.coords(hint, 25+25*(int(globals()["buttons"][1]["text"])-1)*2, 160)

def render_plate(x: int, y: int) -> None:
    canvas.create_oval(x, y, x+50, y+50, fill="blue")
    canvas.create_oval(x+10, y+10, x+40, y+40, fill="blue")

def check() -> None:
    corr = globals()["correct"]
    print(corr)
    if corr + 1 == int(globals()["buttons"][1]["text"]):
        canvas.itemconfig(hnt,text="Správne", fill="green")
        canvas.itemconfig(hint, fill="green")
        for b in buttons:
            b["state"] = "disabled"
    else:
        canvas.itemconfig(hnt,text="Vľavo" if corr < int(globals()["buttons"][1]["text"]) else "Vpravo")
        


root = Tk()
root.title("Pome")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

buttons = [Button(root,text="<",command=lambda: change(-1)), Button(root,text="1",command=check), Button(root,text=">",command=lambda: change(1))]
for i, e in enumerate(buttons):
    canvas.create_window(225 + i*20,450,window=e)

correct = randint(0,9)
offset = randint(0,10)
canvas.create_rectangle(correct * 50 + offset,100,20 + correct * 50 + offset,140, fill="green")


def a() -> None:
    for i in range(10):
        render_plate(i*50, 100)

canvas.after(1000,a)

print(correct)

hint = canvas.create_text(25,160,text="^", fill="red")
hnt = canvas.create_text(100,180,text=f'',fill="red")

root.mainloop()