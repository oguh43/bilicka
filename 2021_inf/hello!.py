import msvcrt

from io import StringIO

def get_input(r_type: type, hint: str) -> type:
    display(hint)
    ret = StringIO()
    while True:
        if msvcrt.kbhit:
            key = msvcrt.getwche()
            if str(key) != "\r":
                ret.write(key)
            else:
                display("\n")
                ret.seek(0)
                return r_type(ret.read())

def display(buffer: str) -> None:
    for char in buffer:
        msvcrt.putwch(char)

number = get_input(int,"Číslo> ")

for i in range(get_input(int,"Od> "),stop:=get_input(int,"Do> ")+1):
    buffer = f"{number*i} {number*(stop-i)}\n"
    display(buffer)
