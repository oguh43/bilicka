
from tkinter import *



with open("./spokojnost_1.txt", "r") as f:
	dt = f.read().splitlines()
data = {}
for l in dt:
	l = l.split(" ")
	if l[1] == "nie":
		if l[0][0:2] not in data.keys():
			data[l[0][0:2]] = 0
		data[l[0][0:2]] += 1
	
print(sum(data.values()))
most = -999
ind = -999

for k, v in data.items():
	if v > most:
		most = v
		ind = k

print(ind,":",most)
print(data)
nums = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","13","14","15","16","17","18","19","20","21","22","23"]
for i in nums:
	if i not in data.keys():
		data[i] = 0

root = Tk()
root.title("Pome")

canvas = Canvas(root, width="480", height="520")
canvas.pack()

canvas.create_text(240,510,text="  ".join(nums))

for k, v in data.items():
	canvas.create_rectangle(int(k)*20+5,500,(int(k)+1)*20-5,500-(int(v)*50),fill="red")


root.mainloop()








