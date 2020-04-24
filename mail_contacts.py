real = open("contacts_db.txt","r",encoding="utf-8")
to_transpose = real.read().split("\n")
real.close()
def add_to_db(name,subject,suffix_of_subject,email):
    real = open("contacts_db.txt","a",encoding="utf-8")
    real.write("\n%s:%s:%s:%s" %(name,subject,suffix_of_subject,email))
    real.close()

def index_del():
    real = open("contacts_db.txt","r",encoding="utf-8")
    data = real.read().split("\n")
    real.close()
    for i in range(len(data)):
        print("%i) %s"%(i,data[i]))
    index = int(input("Index na vymazanie? "))
    real = open("contacts_db.txt","w",encoding="utf-8")
    for i in range(len(data)):
        if i != index and i != len(data)-1:
            real.write("%s\n"%(data[i]))
        elif i != index and i == len(data)-1:
            real.write("%s"%(data[i]))
    real.close()

modify_db = str(input("Pre pridanie do databázy stlačte \"1\", pre odobranie \"2\"")) == "1"
if modify_db == "1":
    ask = input("Oddelte znakom \":\"").split(":")
    add_to_db(ask[0],ask[1],ask[2],ask[3])
elif modify_db == "2":
    index_del()


resolved = open("resolved.txt","r",encoding="utf-8")
res = int(resolved.read())
resolved.close()
print("Current value of completed tasks is: %i"%(res),end=". ")
override = str(input("Do you wish to override this number? Yes/No/Correct ")).lower()
if override == "yes":
    res = res+int(input("+Number? "))
elif override == "correct":
    res = res-int(input("-Number? "))
else:
    res = res+1
resolved = open("resolved.txt","w",encoding="utf-8")
resolved.write(str(res))
resolved.close()


teacher, adr, sub_a, sub = [],[],[],[]
for i in range(len(to_transpose)):
    teacher.append(to_transpose[i].split(":")[0])
    sub_a.append(to_transpose[i].split(":")[1])
    sub.append(to_transpose[i].split(":")[2])
    adr.append(to_transpose[i].split(":")[3])
print("teacher",teacher)
print("adr",adr)
print("sub_a",sub_a)
print("sub",sub)