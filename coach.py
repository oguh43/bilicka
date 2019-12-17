






def nope():
    a = list(input())
    for i in a:
        if i.isalpha()==True or i==" " or i.isdigit():
            print(i, end="")


backwards = ["z","y","x","w","v","u","t","s","r","q","p","o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
normal = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
"""
print(backwards[-1])
print(backwards[-2])
print(backwards[-0])
print(normal[5])
"""
ls = []

inp = list(input("inp???"))

for i in inp:
    n = normal.index(i)
    ls.append(backwards[n-1])
print("".join(ls))






















