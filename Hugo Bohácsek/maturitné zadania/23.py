cif = list(map(int, list(input("Ciferník> ")[:-1])))
veta = input("Vetník> ")

out = ""

ind = 0

for char in veta:
    if not char.isalnum():
        out += " "
        continue
    if ind == len(cif):
        ind = 0
    if ord(char) + cif[ind] > 122:
        out += chr(ord(char) + cif[ind] - 26)
    else:
        out += chr(ord(char) + cif[ind])
    ind += 1


print(out)

