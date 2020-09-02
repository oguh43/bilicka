import sys

import pyautogui

from tkinter import *

screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth//2-100+75,screenHeight//2+75)
main=Tk()
main.wm_attributes("-transparentcolor", main["bg"])
main.title("Anti- afk")
main.geometry(str(screenWidth)+"x"+str(screenHeight))
main.resizable(0, 0)
canvas = Canvas()
canvas.create_rectangle(screenWidth//2-100, screenHeight//2, screenWidth//2, screenHeight//2+100, fill="#FF0000")
canvas.create_rectangle(screenWidth//2+100, screenHeight//2, screenWidth//2+200, screenHeight//2+100, fill="#FF0000")
canvas.pack(fill=BOTH, expand=1)
def my_mainloop():
    screenWidth, screenHeight = pyautogui.size()
    if pyautogui.position()[0] <= pyautogui.size()[0]//2:
        dimx1 = screenWidth//2-100
        dimy1 = screenHeight//2+50
        dimx2 = screenWidth//2
        dimy2 = screenHeight//2+100+50
        o_dimx1 = screenWidth//2+100
        o_dimy1 = screenHeight//2
    else:
        dimx1 = screenWidth//2+100
        dimy1 = screenHeight//2+50
        dimx2 = screenWidth//2+200
        dimy2 = screenHeight//2+100+50
        o_dimx1 = screenWidth//2-100
        o_dimy1 = screenHeight//2

    x,y = pyautogui.position()
    if dimx1 <= x <= dimx2 and dimy1 <= y <= dimy2:
        pyautogui.moveTo(o_dimx1+75,o_dimy1+75,duration=1.5)
    else:
        main.destroy()
    main.after(3000, my_mainloop)

main.after(3000, my_mainloop)
main.mainloop()
