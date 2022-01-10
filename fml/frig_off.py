from __future__ import annotations
from random import randint

def insert(source_str: str, insert_str: str, pos: int) -> str:
    return source_str[:pos] + insert_str + source_str[pos:]

if input("(A)gressive || (S)ilent bypass?").lower() == "a":

    with open("manipulate.txt", "r", encoding="utf-8") as f:
        content = f.read()

    content = content.split(" ")

    for i in range(0, len(content)):
        if len(content[i]) > 3:
            content[i] = insert(content[i], "​", randint(1, len(content[i]) - 1))
            
    content = " ".join(content)

    with open("out.txt", "w+", encoding="utf-8") as f:
        f.write(content)

else:
    with open("manipulate.txt", "r", encoding="utf-8") as f:
        content = f.read()

    if input("Append invisible char to the (L)eft, or (R)ight?").lower() == "l":
        char = "​ "
    else:
        char = " ​"
    content = char.join(content.split(" "))

    with open("out.txt", "w+", encoding="utf-8") as f:
        f.write(content)
