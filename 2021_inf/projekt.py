grid = [["#" for _ in range(5)] if _ < 5 else "\nNa rade je hrac R\n" if _ == 5 else ["0"] if _ == 6 else list(" 12345") for _ in range(8)]
print(grid)
while [print(str(i)+"".join(grid[i])) if i>0 and i<5 else print("".join(grid[i])) if i == -1 else print(grid[i].replace("R",grid[-2][-1])) if i == -3 else "" for i in range(-3,len(grid))] and (True if input("Vyhra? (a/n): ") == "n" else print(f'-------> Vyhral {grid[-2][-2] } <-------')) if len(grid[-2]) > 2 else True and [print(str(i)+"".join(grid[i])) if i>0 and i<5 else print("".join(grid[i])) if i == -1 else print(grid[i].replace("R",grid[-2][-1])) if i == -3 else "" for i in range(-3,len(grid))]: grid[int(input("Zadaj x-ovu suradnicu: "))][int(input("Zadaj y-ovu suradnicu: "))-1] = grid[-2][-2] if not bool(grid[-2].append("X" if grid[-2][-1] == "0" else "0")) else ""



#2,2 -> 1,2




"""
grid = [["#" for _ in range(5)] if _ < 5 else "\nNa rade je hrac R\n" if _ == 5 else ["0"] if _ == 6 else list(" 12345") for _ in range(8)]
print(grid)
while [print(str(i)+"".join(grid[i])) if i>0 and i<5 else print("".join(grid[i])) if i == -1 else print(grid[i].replace("R",grid[-2][-1])) if i == -3 else "" for i in range(-3,len(grid))] and (True if input("Vyhra? (a/n): ") == "n" else print(f'-------> Vyhral {grid[-2][-2] } <-------')) if len(grid[-2]) > 2 else True and [print(str(i)+"".join(grid[i])) if i>0 and i<5 else print("".join(grid[i])) if i == -1 else print(grid[i].replace("R",grid[-2][-1])) if i == -3 else "" for i in range(-3,len(grid))]:
    grid[int(input("Zadaj x-ovu suradnicu: "))][int(input("Zadaj y-ovu suradnicu: "))-1] = grid[-2][-2] if not bool(grid[-2].append("X" if grid[-2][-1] == "0" else "0")) else ""
"""