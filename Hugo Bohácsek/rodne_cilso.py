import webbrowser


inp = str(input("Rodné číslo: "))
a = [inp[i:i+2] for i in range(0,len(inp),2)]
print(f'Dátum narodenia: {a[-1]}.{a[-2] if int(a[-2])<13 else str(int(a[-2])-50)}.{str("19"+a[0]) if int(a[0])>22 else str("20"+a[0])}')
print(f'Pohlavie: {"Žena" if int(a[-2])>13 else "Muž"}')

#webbrowser.open("https://calendar.zoznam.sk/zodiac-sk.php")

rok = int(str(int(str("19"+a[0]) if int(a[0])>22 else str("20"+a[0])))[-2::])

print(rok)

b = ["Krysa","Buvol","Tygr","Zajíc","Drak","Kúň","Koza","Opice","Kohout","Pes","Vepř"]


print(b[rok%12])

