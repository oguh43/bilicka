rok = 2022 - int(input("Rok narodenia?> "))
ls = ["dvadsiatnik","tridsiatnik","štyridstiatnik","päťdesiatnik","šesťdesiatnik"]

if rok < 0:
    print(":(")
elif rok < 20: print("Si týnedžer")
elif rok < 30: print(f"Si {ls[0]}")
elif rok < 40: print(f"Si {ls[1]}")
elif rok < 50: print(f"Si {ls[2]}")
elif rok < 60: print(f"Si {ls[3]}")
else: print("Si mŕtvy :(.")


print(rok)







