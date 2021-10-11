# 3.9.4
from tkinter import *
from random import choice
window = Tk()
window.geometry("250x250")
canvas = Canvas(window)

colors = ["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]

for i in range(50,1,-1):
    canvas.create_line(20,20,200,200,width=i,fill=choice(colors))

canvas.pack()
window.mainloop()
