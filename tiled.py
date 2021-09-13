with open("C:\\Users\\agent\\OneDrive\\Documents\\brmbrmMap.csv","r") as f:
    a = f.read().split("\n")
print("\n".join(a))
print(a,type(a))
new = []
for element in a:
    element = element.replace(",","")
    element = element.replace("2","#")
    element = element.replace("5","r")
    element = element.replace("3","t")
    element = element.replace("0","d")
    element = element.replace("7","h")
    element = element.replace("4","l")
    element = element.replace("6","g")
    element = element.replace("8","u")
    element = element.replace("1","q")
    element = element.replace("9","x")
    new.append(element)
print("\n".join(new))
with open("D:\\brm_brm_sequel\\media\\l2.txt","w") as f:
    f.write("\n".join(new))