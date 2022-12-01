from tkinter import *

with open("./ciarovy_kod_1.txt", "r") as f:
    data = f.read().split("\n")
cur_index = 0

def render_set():
    global cur_index
    canvas.delete("all")
    button = Button(root,text="Dalej more",command=render_set)
    canvas.create_window(225,450,window=button)
    try:
        render(10,10,data[cur_index])
        render(100,10,data[cur_index+1])
        render(10,100,data[cur_index+2])
        render(100,100,data[cur_index+3])
    except IndexError:
        cur_index = 0
    cur_index += 4

def render(x,y,code):
    canvas.create_text(x+35,y+60,text=code)
    for ind in range(0,len(code)):
        canvas.create_line(x,y,x,y+50 if ind not in [0,len(code)-1] else y+70,width=int(code[ind]))
        x += 10
    

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

button = Button(root,text="Dalej more",command=render_set)
canvas.create_window(225,450,window=button)



root.mainloop()