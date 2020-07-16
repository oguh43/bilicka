import pyautogui
import cv2, keyboard, sys, time
from PIL import Image
"""
right_img = cv2.imread("babana10.png")
down_img = cv2.imread("babana11.png")
up_img = cv2.imread("babana12.png")
left_img = cv2.imread("babana13.png")
space_img = cv2.imread("babana14.png")
mt = ["right_img","down_img","up_img","left_img","space_img"]
method = cv2.TM_SQDIFF_NORMED
print("hi")
src = pyautogui.screenshot("crop.png",region=(3166,558,3222,654))
crop_img = Image.open("crop.png")
input()
sys.exit()
src = cv2.imread("src.png")
for i in range(6):
    print(cv2.matchTemplate(mt[i], src, method))


print(pyautogui.position())

while True:
    keyboard.wait("esc")
    print(pyautogui.position())
"""
#src = pyautogui.screenshot("crop.png",region=(3140,550,400,100))
src = pyautogui.screenshot("crop.png",region=(3035,550,810,100))
crop_img = Image.open("crop.png")
#crop_img.show()
controls = ["right_img.png","down_img.png","up_img.png","left_img.png","space_img.png"]
keys = ["right","down","up","left","space"]
index = 0
queue = {}
while 1==0:
    src = pyautogui.screenshot("crop.png",region=(3035,550,810,100))
    pos = pyautogui.locate(controls[index],"crop.png",confidence=0.80)
    if pos != None:
        pyautogui.press(keys[index])
        print("pressed: ",keys[index]," index:",index)
    if index != 4:
        index += 1
    else: 
        index = 0
    #time.sleep(0.3)


index = 0
queue = {}
while True:
    src = pyautogui.screenshot("crop.png",region=(3035,550,810,100))
    pos = pyautogui.locate(controls[index],"crop.png",confidence=0.80)
    if pos != None:
        print(pos[0])
        queue[pos[0]] = keys[index]
        #pyautogui.press(keys[index])
        print("pressed: ",keys[index]," index:",index)
    if index != 4:
        index += 1
    else: 
        index = 0
        queue = {k: v for k, v in sorted(queue.items(),key=lambda item: item[1])}
        for k, v in queue.items():
            pyautogui.press(v)
        queue = {}
    #time.sleep(0.3)

while 1==0:
    src = pyautogui.screenshot("crop.png",region=(3035,550,810,100))
    pos = list(pyautogui.locateAll(controls[index],"crop.png",confidence=0.80))
    if pos != None:
        for i in range(len(pos)):
            queue[pos[i][0]] = keys[index]
    if index != 4:
        index += 1
    else: 
        index = 0
        queue = {k: v for k, v in sorted(queue.items(),key=lambda item: item[1])}
        print(queue)
        for k, v in queue.items():
            pyautogui.press(v)
        queue = {}
    #time.sleep(0.3)


#queue = {k: v for k, v in sorted(queue.items(),key=lambda item: item[1])}