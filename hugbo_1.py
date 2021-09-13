from __future__ import annotations

import re
import turtle

def get_color() -> str:
    while True:
        color = input("Color? (hex)> ")
        if re.match("^#(?:[0-9a-fA-F]{3}){1,2}$",color) is not None:
            return color

class Shape(object):
    def __init__(self, points: int, line_length: int, color: str) -> None:
        self.screen = turtle.getscreen()
        turtle.title("hugbo_1")
        self.points = points
        self.line_length = line_length
        self.deg = 360 // points
        self.color = color
        turtle.pencolor(color)
        self.draw()
    def draw(self) -> None:
        for _ in range(0,self.points):
            turtle.forward(self.line_length)
            turtle.left(self.deg)
        turtle.exitonclick()

points = int(input("How many points?> "))
line_length = int(input("Line length?> "))
color = get_color()

Shape(points,line_length,color)
