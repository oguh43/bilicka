import tkinter as tk

class MainWindow:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Exit', width = 25, command = self.close_windows)
        self.button1.pack()
        self.frame.pack()
        self.classes = [
            Nemocnica,
            Polícia,
            l_80,
            Réservé,
            l_6_t
        ]

        self.new_window()

    def new_window(self) -> None:
        for i in self.classes:
            self.newWindow = tk.Toplevel(self.master)
            self.app = i(self.newWindow)

    def close_windows(self) -> None:
        self.master.destroy()

class Nemocnica:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()
    
    def draw(self, canvas: tk.Canvas) -> None:
        canvas.create_rectangle(20, 20, 120, 120, fill="#27166C")
        canvas.create_text(70, 65, text="H", font="Arial 65 bold", fill="white")
        canvas.create_text(70, 110, text="NEMOCNICA", font="Arial 12 bold", fill="white")

class Polícia:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()
    
    def draw(self, canvas: tk.Canvas) -> None:
        canvas.create_rectangle(20, 20, 100, 120, fill="#27166C")
        canvas.create_rectangle(35, 35, 85, 90, fill="white")
        canvas.create_text(60, 65, text="Polícia", font="Arial 11 bold")

class l_80:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()
    
    def draw(self, canvas: tk.Canvas) -> None:
        canvas.create_oval(20,20,120,120,fill="white")
        canvas.create_oval(22,22,118,118,fill="#D42615")
        canvas.create_oval(32,32,108,108,fill="white")
        canvas.create_text(70, 70, text="80", font="Arial 45 bold")

class Réservé:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()
    
    def draw(self, canvas: tk.Canvas) -> None:
        canvas.create_rectangle(20, 20, 100, 120, fill="#27166C")
        canvas.create_text(60, 55, text="P", font="Arial 65 bold", fill="white")
        canvas.create_text(60, 110, text="RÉSERVÉ", font="Arial 12 bold", fill="white")

class l_6_t:
    def __init__(self, master: tk.Tk) -> None:
        self.master = master
        self.master.geometry("150x150")
        self.canvas = tk.Canvas(self.master)
        self.draw(self.canvas)
        self.canvas.pack()
    
    def draw(self, canvas: tk.Canvas) -> None:
        canvas.create_oval(20,20,120,120,fill="white")
        canvas.create_oval(22,22,118,118,fill="#D42615")
        canvas.create_oval(32,32,108,108,fill="white")
        canvas.create_text(70, 70, text="6 t", font="Arial 41 bold")

def main(): 
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()