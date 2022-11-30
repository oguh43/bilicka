s = []


for _ in range(3):
    s.append(float(input("Strana> ")))
s.sort()

if not s[0] + s[1] > s[2]:
    print("Nie je trojuholník!")
    __import__("sys").exit()

if len(set(s)) == 1:
    print("Je rovnostranný")
elif len(set(s)) == 2:
    print("Je rovnoramenný")
elif (s[0] ** 2) + (s[1] ** 2) == (s[2] ** 2):
    print("Je parvouhlý")
else:
    print("Je všeobecný")
