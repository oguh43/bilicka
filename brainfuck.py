import time
def interpret():
    program = input("Zadajte program ")
    memory, memory_view, pointer,  std_out= [0], True, 0, []
    for i in program:
        if i == ">":
            memory.append(0)
    i = 0
    while i < len(program):

        if program[i] == "<":
            pointer -= 1
        elif program[i] == ">":
            pointer += 1
        elif program[i] == "-":
            if memory[pointer] > 0:
                memory[pointer] -= 1
            else:
                memory[pointer] = 255
        elif program[i] == "+":
            if memory[pointer] < 255:
                memory[pointer] += 1
            else:
                memory[pointer] = 0
        elif program[i] == ".":
            if memory_view == False:
                print(chr(memory[pointer]), end = "")
            std_out.append(chr(memory[pointer]))
        elif program[i] == ",":
            memory[pointer] = ord(input("Charakter? "))
        elif program[i] == '[':
            if memory[pointer] == 0:
                open_braces = 1
                while open_braces > 0:
                    i += 1
                    if program[i] == '[':
                        open_braces += 1
                    elif program[i] == ']':
                        open_braces -= 1
        elif program[i] == ']':
            open_braces = 1
            while open_braces > 0:
                i -= 1
                if program[i] == '[':
                    open_braces -= 1
                elif program[i] == ']':
                    open_braces += 1
            i -= 1
        i += 1
        if memory_view == True:
            print(f"{memory}\r", end = "")
            #time.sleep(0.01)
    if memory_view == True:
        print("")
        print("".join(std_out))
interpret()
