from tkinter import *

occupied = []

with open("./lodicky.txt", "r") as f:
    mp = f.read().split("\n")
    mp.pop(0)



def loťka(event):
    for y in range(0, len(mp)):
        for x in range(0,len(mp[0].split(" "))-2):
            
            if mp[y].split(" ")[x] == "1" or mp[y].split(" ")[x+1] == "1" or mp[y].split(" ")[x+2] == "1": continue
            if [x,y] not in occupied:
                canvas.create_rectangle(x*20+5,y*20+5,x*20+55,y*20+15,fill="yellow")
                occupied.append([x-1,y])
                occupied.append([x,y])
                occupied.append([x+1,y])
                occupied.append([x+2,y])
                occupied.append([x+3,y])
                return
    canvas.create_text(50,200,text="Plnô je")
root = Tk()
root.title("Pome")

canvas = Canvas(root, width="300", height="300")
canvas.pack()

x = 0
y = 0
for l in mp:
    for i in l.split(" "):
        canvas.create_rectangle(x, y, x+20, y+20, fill=["blue","grey"][int(i)])
        x+=20
    y+=20
    x=0


root.bind("<space>",loťka)


root.mainloop()

