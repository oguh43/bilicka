import os
filename = str(input("Meno súboru? "))
if filename.split(".")[-1] != "htm":
    filename += ".htm"

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
path = os.path.join(__location__, filename)
with open(path,"r") as f:
    data = f.read()
data = data.replace("Math.floor(j  *  Math.random())","0")

with open(path,"w") as f:
    f.write(data)

