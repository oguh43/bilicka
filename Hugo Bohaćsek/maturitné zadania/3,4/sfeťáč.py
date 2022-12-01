from tkinter import Tk  # Python 3
#from Tkinter import Tk # for Python 2.x
tk = Tk()
content = tk.clipboard_get()
tk.clipboard_clear()
out = f'[globals().update({{"{content.split("=")[0].strip()}": {content.split("=")[1].strip()}}})]'
tk.clipboard_append(out)
tk.update()
print(out)