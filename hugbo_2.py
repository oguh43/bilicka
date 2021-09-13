from __future__ import annotations

import re
import time

from tkinter import *

def get_color() -> str:
    while True:
        color = input("Color? (hex)> ")
        if re.match("^#(?:[0-9a-fA-F]{3}){1,2}$",color) is not None:
            return color

class Circle(object):
     def __init__(self, colors: dict[int,str], speed: float) -> None:
        self.speed = speed
        self.root = Tk()
        self.root.title("hugbo_2")
        self.canvas = Canvas(self.root, width=400, height = 400)
        self.canvas.pack()
        self.circle1 = self.canvas.create_oval(20, 260, 120, 360, outline='white',fill=colors[1])
        self.circle2 = self.canvas.create_oval(2, 2, 40, 40, outline='white', fill=colors[2])
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

     def animation(self) -> None:
        left = False
        while True:
            x = 5
            y = 0
            if not left:
                for _ in range(0,55):
                    time.sleep(self.speed)
                    self.canvas.move(self.circle1, x, y)
                    self.canvas.move(self.circle2, x, y)
                    self.canvas.update()
                left = True
            else:
                for _ in range(0,55):
                    time.sleep(self.speed)
                    self.canvas.move(self.circle1, -x, y)
                    self.canvas.move(self.circle2, -x, y)
                    self.canvas.update()
                left = False
colors = {1:get_color(),2:get_color()}
speed = float(input("Animation speed? (delay) (optimal: 0.025)> "))
Circle(colors, speed)
