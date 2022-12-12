from random import randint, choice
from tkinter import *

color = ["#67E66B","#51732A","#009B60","#709E11","#7C9E5A","#659E8D","#939E2C"]

def draw(event):
    print("here")
    if randint(0,1):
        x = randint(0,600)
        y = 400 - randint(0,300)
        co = [0,400]
        step = randint(0, 1)
        for i in range(0,601):
            if i % 10 == 0:
                step = randint(0, 1)
            if i <= x:
                y -= step
            else:
                y += step
            co.append(i)
            co.append(y)
        co.append(600)
        co.append(400)
        canvas.create_polygon(co,outline="green", fill=choice(color))
    else:
        x = randint(0,600)
        y = 400 - randint(0,300)
        co = [0,400]
        step = randint(0, 1)
        for i in range(0,601):
            if i % 10 == 0:
                step = randint(0, 1)
            if i <= x:
                y += step
            else:
                y -= step
            co.append(i)
            co.append(y)
        co.append(600)
        co.append(400)
        canvas.create_polygon(co,outline="green", fill=choice(color))

root = Tk()
root.title("Kopčok")

canvas = Canvas(root, width="600", height="400")
canvas.pack()

root.bind("<space>",draw)

root.mainloop()
