ls=[]
for i in range(0,10): ls.append(int(input(str(i+1) +". Skore:")))
ls.sort(reverse=True)
ls.pop(0) and ls.pop(8)
print("Vysledne skore je: " +str(sum(ls)/float(len(ls))))
