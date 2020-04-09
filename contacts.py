from datetime import date

today = date.today()

date = today.strftime("%d.%m.%Y")

teacher = ["Hugo Bohácsek","Jana Manczálová","Iveta Rybárová"]
adress = ["agenthugo43@gmail.com","amdmods@gmail.com","agentzoja43@gmail.com"]
subject_a = ["Informatika","Fyzika","Matematika"]
subject = ["Informatiky","Fyziky","Matematiky"]
r=0
for i in teacher:
    r+=1
    print(r,") ",i, sep="")
who = int(input("Číslo vybraného učiteľa:"))-1

print(teacher[who],adress[who],subject_a[who], sep="; ")

file_name = "%s_uloha" %subject_a[who].lower()
print(file_name)

a = "Riešenie príkladov z %s" %subject[who]
b = "Dobrý deň,\nPosielam vám vypracované úlohy z %s.\nHugo Bohácsek, Ki.B %s" %(subject[who],date)


print(a)
print(b)










