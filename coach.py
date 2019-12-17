






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

    ls1 = []
    for i in inp:
        f = normal.index(i)
        ls1.append(normal[-f-1])
    print("".join(ls1))



ls = []
a = str(input("???").lower()).split("/")
if len(a) == 3:
    for i in a:
        if a.index(i) == 0:
            ls.append(i)
        elif a.index(i) == 1:
            ls.insert(0,i)
        else:
            ls.append(i)
    print("/".join(ls))
else:
    a = a.split(" ")
    a = a.split(",")
    for i in a:
        if a.index(i) == 0:
            if i == "january":
                ls.append("1")
            elif i == "february":
                ls.append("2")
            elif i == "march":
                ls.append("3")
            elif i == "april":
                ls.append("4")
            elif i == "may":
                ls.append("5")
            elif i == "juny":
                ls.append("6")
            elif i == "july"
                ls.append("7")
            elif i == "august":
                ls.append("8")
            elif i == "september":
                ls.append("9")
            elif i == "october":
                ls.append("10")
            elif i == "november":
                ls.append("11")
            else:
                ls.append("12")
        elif a.index(i) == 1:
            ls.insert(0,i)
        else:
            ls.append(i) 
    print("/".join(ls))
        