import msvcrt
import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

def wait():
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getch()
            if chr == b"\x1b":
                print("ESCAPE")
                circle()

def circle():
    x,y = pyautogui.position()
    pyautogui.mouseDown()
    action = 0
    while True:
        if msvcrt.kbhit():
            chr = msvcrt.getch()
            if chr == b"\x1b":
                pyautogui.mouseUp()
                print("ESCAPE")
                return
        if action == 0:
            pyautogui.moveRel(0,100,.5)
            action += 1
        elif action == 1:
            pyautogui.moveRel(100,0,.5)
            action += 1
        elif action == 2:
            pyautogui.moveRel(0,-100,.5)
            action += 1
        else:
            pyautogui.moveRel(-100,0,.5)
            action = 0
    
wait()
"""
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
>> pyautogui.moveTo(100, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds
"""