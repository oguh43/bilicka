from tkinter import *

with open("k2.txt") as f:
    data = [x.split(" ") for x in f.read().splitlines()]
mx = 0
for l in data:
    if int(l[0]) > mx:
        mx = int(l[0])

print(data,mx)

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="500", height="500")
canvas.pack()

x = 100
y = 100

for line in data:
    if int(line[0]) < mx:
        print(int(line[0]),line, mx)
        x += 15 * (mx-int(line[0]))
    for c in range(len(line[1])):
        char = line[1][c]
        if int(line[0]) == c+1:
            canvas.create_rectangle(x,y,x+15,y+15,fill="grey")
        else:
            canvas.create_rectangle(x,y,x+15,y+15,fill="white")
        x+=15
    x=100
    y+=15


x = 100
y = 350

for line in data:
    if int(line[0]) < mx:
        print(int(line[0]),line, mx)
        x += 15 * (mx-int(line[0]))
    for c in range(len(line[1])):
        char = line[1][c]
        if int(line[0]) == c+1:
            canvas.create_rectangle(x,y,x+15,y+15,fill="grey")
        else:
            canvas.create_rectangle(x,y,x+15,y+15,fill="white")
        canvas.create_text(x+8,y+8,text=char)
        x+=15
    x=100
    y+=15





root.mainloop()