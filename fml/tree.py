import sys
import atexit

from time import sleep
from random import choice
from math import ceil, floor

from colorama import Fore, Back, Style, init

init()

def clear_style() -> None:
    print(Style.RESET_ALL)
    
atexit.register(clear_style)

def pad(tree: list[str]) -> list[str]:
    longest = ceil(len(max(tree, key=len)) / 2)
    res = []
    for row in tree:
        length = longest - ceil(len(row) / 2)
        res.append(" "*length+row)
    return res

def render_tree(tree: list[str], frame: int) -> None:
    styles = {
        "i": [
            Style.BRIGHT + Fore.YELLOW + Back.RED,
            Style.BRIGHT + Fore.RED + Back.YELLOW
            ],
        "/": Style.DIM + Fore.GREEN,
        "\\": Style.DIM + Fore.GREEN,
        " ": Style.BRIGHT + Back.GREEN,
        "O": [
            Style.BRIGHT + Fore.BLUE,
            Style.BRIGHT + Fore.MAGENTA,
            Style.BRIGHT + Fore.CYAN
        ],
        "=": Style.DIM + Fore.GREEN,
        "A": Style.DIM + Fore.GREEN,
        "*": Style.BRIGHT + Fore.WHITE
    }
    out = ""
    flag = False
    for line in tree:
        for char in line:
            if tree.index(line) < 2:
                out += Style.BRIGHT + Fore.YELLOW + char
            elif tree.index(line) == len(tree) - 1:
                out += Style.DIM + Fore.RED + char
            else:
                if char not in ["i","O"," "]:
                    flag = True
                    out += styles[char] + char
                else:
                    if char == "i":
                        out += styles[char][frame] + char
                    elif char == "O":
                        out += choice(styles[char]) + char
                    else:
                        if flag == True:
                            out += styles[char] + char
                        else:
                            out += char
            out += Style.RESET_ALL
        out += "\n"
        flag = False
    sys.stdout.write("\r"+out)
    sys.stdout.flush()

size = int(input("Size?> "))

if size < 6:
    if size == 1:
        print("A")
        sys.exit()
    else:
        print("Too smol")
        sys.exit()

if size % 3 != 0:
    print("Frig off! Im only doing numbers divisible by 3.")
    while size % 3 != 0:
        size += 1

tree = [
    "|",
    "-+-",
    "A",
    "/=\\",
    "i/ * \\i",
    "/=====\\"
]

for i in range(len(tree)+3,size+1,3):
    tree.append("/"+" "*(floor((len(tree)+1-3)/2))+"i"+" "*(floor((len(tree)+1-3)/2))+"\\")
    tree.append("i/"+" "*(ceil((len(tree)+1-5)/4))+"O"+" "*(ceil((len(tree)+1-5)/4))+"*"+" "*(ceil((len(tree)+1-5)/4))+"O"+" "*(ceil((len(tree)+1-5)/4))+"\\i")
    tree.append("/"+"="*(len(tree)+1)+"\\")
tree.append("|___|")

frame = 0
while True:
    render_tree(pad(tree),frame)
    frame = abs(frame - 1)
    sleep(1)
