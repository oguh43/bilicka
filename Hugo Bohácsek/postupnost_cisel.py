while True:
    if (inp:=int(input("Číslo? > "))) < 5:
        if inp == 0:
            print("Postupnosť bola dodržaná!")
        else:
            print("Postupnosť nebola dodržaná!")
        break