from tkinter import *

with open("stanice_metra.txt", "r") as f:
    data = f.read().splitlines()
    color = data.pop(0)

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="700", height="500")
canvas.pack()

x = 20
y = 150

for i in range(0, len(data)):
    stanica = data[i]
    if i == 0 or i == len(data)-1:
        canvas.create_rectangle(x,y,x+10,y+10, fill=color, outline=color)
    elif "*" in stanica:
        canvas.create_oval(x,y,x+10,y+10, outline=color)
    else:
        canvas.create_oval(x,y,x+10,y+10, fill=color, outline=color)
    canvas.create_text(x+40, y-40, text=stanica.replace("*",""), angle=45)
    if i != len(data) - 1:
        canvas.create_rectangle(x+10,y+3,x+30,y+8,fill=color,outline=color)
    x+=30

root.mainloop()
