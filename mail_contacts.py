real = open("real.txt","r",encoding="utf-8")

#print(real.read())
to_transpose = (":").join(real.read().split("\n")).split(":")
real.close()

print(to_transpose)

for i in to_transpose:
    print(i)

def add_to_db(name,subject,suffix_of_subject,email):
    real = open("real.txt","a",encoding="utf-8")
    real.write("\n%s:%s:%s:%s" %(name,subject,suffix_of_subject,email))
    real.close()

if str(input("Add? ")) == "1":
    ask = input("Oddelte znakom \":\"").split(":")
    add_to_db(ask[0],ask[1],ask[2],ask[3])

def index_del():
    real = open("real.txt","r",encoding="utf-8")
    data = real.read().split("\n")
    real.close()
    for i in range(len(data)):
        print("%i) %s"%(i,data[i]))
    index = int(input("Index na vymazanie? "))
    real = open("real.txt","w",encoding="utf-8")
    for i in range(len(data)):
        if i != index and i != len(data)-1:
            real.write("%s\n"%(data[i]))
        elif i != index and i == len(data)-1:
            real.write("%s"%(data[i]))
    real.close()


index_del()

