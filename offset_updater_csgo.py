import urllib.request, os
restart = False
try:
	import json
except:
	print("Skúšam nainštalovať jsonlib")
	try:
		os.system("python -m pip install jsonlib")
		restart = True
	except:
		raise Exception("Chýba knižnica jsonlib a nebolo možné ju automaticky aktualizovať")
if restart == True:
	raise Exception("Inštalácia prebehla úspešne, prosím spustite skript znova.")
def update(hx):
	try:
		hx = int(hx)
	except ValueError:
		raise ValueError("Program nedostal číslo int()/ str() ale",hx)
	with urllib.request.urlopen("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json") as url:
		offsets = json.loads(url.read().decode())["signatures"]
	if hx == 0: return offsets
	elif hx == 1: return {k:hex(v) for k,v in offsets.items()}
	elif hx != 0 and hx != 1:
		raise Exception("Očakávaný vstup 0 pre int() a 1 pre hex(), program dostal:",hx)