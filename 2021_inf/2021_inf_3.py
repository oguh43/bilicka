import os
import sys
import random
import subprocess

import tkinter.font
import tkinter as tk

failed = False
path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

if os.path.isfile(path+"\\sources\\din1451alt.ttf"):
    try:
        import pyglet
    except ImportError:
        python = sys.executable
        subprocess.check_call([python, "-m", "pip", "install", "pyglet"], stdout=subprocess.DEVNULL)
        print("Please restart.")
        sys.exit()
else:
    failed = True
    print("Fonts won't load, they are not installed.")

class MainWindow:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Exit', width = 25, command = self.close_windows)
        self.button1.pack()
        self.frame.pack()
        self.classes = [
            l_80,
            h_l,
            v_l,
            odhad,
            alt,
            adam
        ]

        self.new_window()

    def new_window(self) -> None:
        for i in self.classes:
            self.newWindow = tk.Toplevel(self.master)
            self.app = i(self.newWindow)

    def close_windows(self) -> None:
        self.master.destroy()

class l_80:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("300x300")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()
    
    def draw(self, canvas: tk.Canvas) -> None:
        self.x = random.randrange(0,100,10)
        self.y = random.randrange(0,100,10)
        canvas.create_oval(self.x,self.y,self.x+100,self.y+100,fill="white")
        canvas.create_oval(self.x+2,self.y+2,self.x+98,self.y+98,fill="#D42615")
        canvas.create_oval(self.x+12,self.y+12,self.x+88,self.y+88,fill="white")
        if failed:
            canvas.create_text(self.x+50, self.y+50, text=str(random.randrange(0,100,10)), font="Arial 45 bold")
        else:
            canvas.create_text(self.x+50, self.y+50, text=str(random.randrange(0,100,10)), font=tk.font.Font(family="Alte DIN 1451 Mittelschrift",weight="bold",size=45))

class h_l:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()

    def draw(self, canvas: tk.Canvas) -> None:
        for i in range(5,25,5):
            canvas.create_line(5,i,70,i)
        for i in range(35,55,5):
            canvas.create_line(i-30,i,70,i)
        for i in range(65,85,5):
            canvas.create_line(5,i,70,i+5*((i-60)//2))
            
class v_l:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()

    def draw(self, canvas: tk.Canvas) -> None:
        for i in range(5,25,5):
            canvas.create_line(i,5,i,70)
        for i in range(35,55,5):
            canvas.create_line(i,i-25,i,70)
        for i in range(65,85,5):
            canvas.create_line(i,i-60,i,i-5)

class odhad:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()

    def draw(self, canvas: tk.Canvas) -> None:
        """
            a) odhad originálu: vedľa seba obdĺžniky
            b) prvý obdĺžnik (a aj všetky za ním) sa posunú
            c) predĺžia sa medzery medzi obdĺžnikmi
            d) obdĺžniky budú mať inú dĺžku
        """
        x = 0
        for _ in range(1,11):
            x = x+20
            canvas.create_rectangle(x, 10, x+15, 20)
        x = 20
        for _ in range(1,11):
            x = x+20
            canvas.create_rectangle(x, 30, x+15, 40)
        x = 0
        for _ in range(1,11):
            x = x+40
            canvas.create_rectangle(x, 50, x+15, 60)
        x = 0
        for _ in range(1,11):
            x = x+40
            canvas.create_rectangle(x, 70, x+30, 80)

class alt:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()

    def draw(self, canvas: tk.Canvas) -> None:
        for i in range(20,200,20):
            canvas.create_rectangle(i+5,10,i+20,20)
            
class adam:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()

    def draw(self, canvas: tk.Canvas) -> None:
        """
            Adamko nepripočítaval k `y` ale stále ho nastavoval na `5`
        """
        y = 5
        for _ in range(0, 6):
            canvas.create_rectangle(10, y, 30, y+10)
            y += 20

def main(failed: bool) -> None: 
    root = tk.Tk()
    if not failed:
        try:
            pyglet.font.add_file(path+"\\sources\\din1451alt.ttf")
        except Exception:
            failed = True
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main(failed)