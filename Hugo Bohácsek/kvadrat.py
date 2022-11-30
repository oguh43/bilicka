from math import sqrt
a = float(input("a> "))
b = float(input("b> "))
c = float(input("c> "))

d = (b**2) - 4 * a * c

if d < 0:
    print("Rovnica nemá riešenie")
elif d == 0:
    print(f"Rovnica má 1 riešenie: {(-b)/(2 * a)}")
else:
    print("Rovnica má 2 riešenia:")
    print(f"\tKoreň 1: {((-b)+sqrt(d))/2*a}")
    print(f"\tKoreň 1: {((-b)-sqrt(d))/2*a}")






