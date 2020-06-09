import keyboard
import os
import psutil
import pyautogui
import pytesseract
import sqlite3
import sys
import time
import tkinter
from win10toast import ToastNotifier
from tkinter.filedialog import askdirectory
from PIL import Image

class Database(object):
    def __init__(self,db = "data.db"):
        self.db = db
        if not os.path.exists(self.db):
            with open(self.db, "w"):
                pass
        self._conn = sqlite3.connect(self.db)
        self._cursor = self._conn.cursor()

    #def struct_pull(self,db,)


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def read_xp(image):
    return pytesseract.image_to_string(image)

def tst(fail = True, xp = None):
    if fail == True:
        notif = "Failed"
        bdy = "XP not found"
    elif fail == False and xp == None:
        notif = "Success"
        bdy = "XP was found"
    elif fail == False and xp != None:
        notif = "Success"
        bdy = "XP with the value of %s was found" %(str(xp))
    toast = ToastNotifier()
    toast.show_toast(notif,bdy,duration=5,threaded=True)


def get_x(width):
    left_border = width // 3
    right_border = (width // 3) * 2
    return left_border, right_border

def get_y(height):
    upper_border = 0
    lower_border = height - upper_border
    print(upper_border,lower_border)
    return upper_border, lower_border

def main():
    width, height = pyautogui.size()
    left_border, right_border = get_x(width)
    upper_border, lower_border = get_y(height)
    crop = pyautogui.screenshot("crop.png",region=(left_border,upper_border,right_border,lower_border))
    #crop = pyautogui.screenshot("crop.png",region=(upper_border,left_border,lower_border,right_border))
    crop_img = Image.open("crop.png")
    img_val = read_xp(crop_img)
    img_val = img_val.split("\n")
    sys.exit()
    for line in img_val:
        if "XP" in line:
            xp = "".join([int(s) for s in line.split() if s.isdigit()])
            tst(False,xp)
#root = tkinter.Tk()
#dirname = askdirectory(parent=root, initialdir="/",title="Please select directory.")

#main()
"""
try:
    if "Apex.exe" in (p.name() for p in psutil.process_iter()):
        waiting()
except:
    sys.exit()
"""


def waiting():
    try:
        if keyboard.is_pressed("q"):
            main()
    except:
        time.sleep(0.001)
        waiting()

#TODO: saving, graphs, testing
