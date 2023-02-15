from tkinter import *
import random
from copy import deepcopy

colors = ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(14)]
colors = ["blue"] + colors

def numIslands(grid):
    count = 0
    sizes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "#":
                if grid[i][j] > 0:
                    sizes.append(dfs(grid, i, j))
                    count += 1
    return [count, sizes]

def dfs(grid, i, j):
    
    if grid[i][j] == "#":
        return 0
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] < 1:
        return 0
    area = 1
    grid[i][j] = "#"
    
    area += dfs(grid, i + 1, j)
    area += dfs(grid, i - 1, j)
    area += dfs(grid, i, j + 1)
    area += dfs(grid, i, j - 1)
    return area

with open("./mapa.txt", "r") as f:
    mp = [list(map(int, line.split(" "))) for line in f.read().splitlines()]

dta = numIslands(deepcopy(mp))

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="300", height="300")
canvas.pack()

x = 0
y = 0
for l in mp:
    for i in l:
        canvas.create_rectangle(x, y, x+20, y+20, fill=colors[i])
        x+=20
    y+=20
    x=0

canvas.create_text(100,250,text=f"Number of islands: {dta[0]}\nMax area: {max(dta[1])}")


root.mainloop()