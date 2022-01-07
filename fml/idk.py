#!/usr/bin/env python
# -*- coding: utf-8 -*-

#najdite si na internete, podla akeho vzorca pracuje bmi kalkulacka
#a naprogramujte takuto kalkulacku, ktora teda vypocita bmi
#pouzivatela podla nim zadanych hodnota vypise mu podla vypocitanej
#hodnoty, do ktorej kategorie patri (nadvaha, optimal, podvaha...)

"""
weight = int(input("Váha?> "))
height = int(input("Výška> ")) / 100

bmi = weight / (height**2)
print(bmi)
"""










#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = int(input("Zadaj prve cislo: "))
z = input("Zadaj znamienko: ")
b = int(input("Zadaj druhe cislo: "))

#print(eval(f"{a}{z}{b}"))
if b == 0 and z == "/":
    print("Error, delenie nulou")
else:
    if z == "+":
        print(a+b)
    elif z == "-":
        print(a-b)
    elif z == "*":
        print(a*b)
    else:
        print(a/b)



__import__("sys").exit()