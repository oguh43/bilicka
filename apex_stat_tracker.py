import pyautogui, psutil, pytesseract, keyboard, sys, time
from win10toast import ToastNotifier
from PIL import Image

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
    toast.show_toast(notif,body,duration=5)


def get_x(width):
    left_border = width // 3
    right_border = (width // 3) * 2
    return left_border, right_border

def get_y(height):
    upper_border = (height // 4)
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
    if "XP" not in img_val:
        tst(True)
        waiting()
    else:
        for line in img_val:
            if "XP" in line:
                xp = "".join([int(s) for s in line.split() if s.isdigit()])
                tst(False,xp)

try:
    if "Apex.exe" in (p.name() for p in psutil.process_iter()):
        waiting()
except:
    sys.exit()


main()
def waiting():
    try:
        if keyboard.is_pressed("q"):
            main()
    except:
        time.sleep(0.001)
        waiting()

#TODO: saving, graphs, testing