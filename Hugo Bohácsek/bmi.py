vyska = float(input("Výška (m)> "))
vaha = float(input("Váha (kg)> "))

bmi = vaha/(vyska**2)

if bmi < 18.5:
    print("Podváha")
elif 18.5 <= bmi < 25:
    print("Normál")
elif 25 <= bmi < 30:
    print("Nadváha")
else:
    print("Obezita")


print(f"Vaše {bmi=}")








