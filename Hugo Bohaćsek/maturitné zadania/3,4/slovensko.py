from tkinter import *

with open("./sr.txt", "r") as f:
    sr = f.read().split("\n")
with open("./sneh.txt", "r") as f:
    sneh = f.read().split("\n")
cur_index = 0

def render_next(event):
    global cur_index
    if cur_index >= len(sneh): return
    
    canvas.create_oval(int(sneh[cur_index].split(" ")[0]),int(sneh[cur_index].split(" ")[1])-100,int(sneh[cur_index].split(" ")[0])+5,int(sneh[cur_index].split(" ")[1])+5-100, fill="red")
    canvas.itemconfig(text, text=" ".join(sneh[cur_index].split(" ")[2:]))
    cur_index += 1

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="800", height="800")
canvas.pack()

for i in range(0,len(sr)):
    canvas.create_line(int(sr[i].split(" ")[0]),int(sr[i].split(" ")[1]),int(sr[i].split(" ")[0])+1,int(sr[i].split(" ")[1]))

text = canvas.create_text(500,500,text="Daj tot špejs na vyobrazenie")

root.bind("<space>",render_next)


root.mainloop()

