from random import randint

def insert(source_str, insert_str, pos):
    return source_str[:pos] + insert_str + source_str[pos:]

with open("manipulate.txt", "r", encoding="utf-8") as f:
    content = f.read()

content = content.split(" ")

for i in range(0, len(content)):
    if len(content[i]) > 3:
        content[i] = insert(content[i], "​", randint(1, len(content[i]) - 1))
        
content = " ".join(content)

with open("out.txt", "w+", encoding="utf-8") as f:
    f.write(content)
