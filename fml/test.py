from os import listdir
from os.path import isfile, join

def compress() -> None:
    source_file = open("fml/source.txt","r")

    chars = [line.replace("\n","") for line in source_file.readlines()]

    def map_line(line: str)-> str:
        result = ""
        count = 0
        curr_char = ""
        for char in line:
            if curr_char == "":
                curr_char = char    
            if curr_char != char:
                result += curr_char if count == 1 else f"{count}{curr_char}"
                count = 0
                curr_char = char
            count += 1
        result += char if count == 1 else f"{count}{char}"
        return result

    def remove_duplicates(lines: list[str]) -> list[str]:
        count = 0
        last_line = ""
        for line in lines:
            if last_line == "":
                last_line = line
            if last_line != line:
                if count > 1:
                    lines[lines.index(last_line)] = f"{last_line}+{count}"
                    while last_line in lines:
                        lines.remove(last_line)
                last_line = line
                count = 0
            count += 1
        return lines

    res = []
    for i in chars:
        res.append(map_line(i))

    res = remove_duplicates(res)

    source_file.close()
    target_file = open("fml/"+"n".join(res)+".txt","w+")
    target_file.close()
    
def decompress() -> None:

    files = [f for f in listdir("fml/") if isfile(join("fml", f))]
    print("Pick a file to decode\n")
    for i in range(len(files)):
        print(f"File number-> {i}; File name-> \"{files[i]}\"")        
    file = "".join(files[int(input("File number? > "))].split(".")[:-1]).split("n")
    for line in file:
        if "+" in line:
            file[file.index(line)] = eval("n\"*".join(("(\""+line).split("+")) + ").split(\"n\")[:-1]")
    flatten = lambda *n: (e for a in n for e in (flatten(*a) if isinstance(a, (tuple, list)) else (a,)))
    file = list(flatten(file))
    
    res = ""
    number = ""
    for line in file:
        for char in line:
            try:
                int(char)
                number += char
            except ValueError:
                res += str(eval(f"'{char}'*{int(number) if number != '' else 1}"))
                number = ""
        res += "\n"
        number = ""
    print(res)  
        
if __name__ == '__main__':
    if input("Compress/ Decompress? C||D -> ").upper() == "C":
        compress()
    else:
        decompress()