from tkinter import *

with open("ank.txt") as f:
    data = f.read().splitlines()

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

dt = list(map(int,data[1].split(" ")))

canvas.create_text(200,10,text=data[0])
canvas.create_text(70,25,text=f"1) Áno - {dt[0]}")
canvas.create_text(70,40,text=f"1) Nie - {dt[1]}")
canvas.create_text(70,55,text=f"1) Neviem - {dt[2]}")

canvas.create_rectangle(110, 25, 110+5*dt[0], 30, fill="green")

canvas.create_rectangle(110, 40, 110+5*dt[1], 45, fill="red")
canvas.create_rectangle(110, 55, 110+5*dt[2], 60, fill="red")

root.mainloop()