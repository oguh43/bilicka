
from random import *

ls = [1,2,3,4,5,6,7,8,9,10,11,12]
test = [1,2,3,4,6,7,9]
sec = []
pl = 0

for i in range(len(test)):
    try:
        if test[i+pl] == ls[i+pl]:
            sec.append(test[i])
        else:
            sec.append("")
            pl = pl + 1
    except Exception:
        pass


print(sec)



ls = [1,2,3,4,5,6,7,8,9,10,11,12]
test = [1,2,3,4,6,7,9]
sec = []
pl = 1

for i in range(len(test)+20):
    try:
        print(test[i],pl)
        if test[i] != pl:
            test.insert(i," ")
        pl = pl + 1
    except Exception:
        pass
print(test)

postupka = []
temp = []
dlzka = 0
for i in test:
    if str(i).isdigit() == True:
        dlzka = dlzka +1
        temp.append(i)
    elif str(i).isdigit() == False and dlzka >= 3:
        postupka.append(temp)
        temp.clear()
        dlzka = 0
    

print(postupka)


t = " "
if str(t).isdigit():
    print("int")
else:
    print("str")

def check_straight(test):
    pl = 1
    
    for i in range(len(test)+20):
        try:
            print(test[i],pl)
            if test[i] != pl:
                test.insert(i," ")
            pl = pl + 1
        except Exception:
            pass
    return test
    
ai = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(3):
    ai.pop(randint(0,len(ai)))

shuffle(ai)
ai.sort()
#print(check_straight(ai))











