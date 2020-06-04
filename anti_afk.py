import pyautogui, keyboard, time

width, height = pyautogui.size()
mouse_x, mouse_y = pyautogui.position()
pyautogui.moveTo(width//2,height//2)
state = "right"
while True:
    break
    try:
        if keyboard.is_pressed("q"):
            break
    except:
        pass
    if state == "right":
        pyautogui.move(25,0)
        state = "left"
    elif state == "left":
        pyautogui.move(-25,0)
        state = "right"
    time.sleep(5)
