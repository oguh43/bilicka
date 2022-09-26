inp = input("Číselko? > ")
flag = True
for i in range(0,len(inp)//2):
    if inp[i] != inp[-(i+1)]:
        flag = False

if flag:
    print("Je palindróm")
else:
    print("Nie je palindróm")
