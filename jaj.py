def wish():
    print("Rad by som bol za: \n 1) Steam Controller(da sa objednat iba cez amazon/ebay, vyroba bola ukoncena 3.12.) \n 2) Nejake tie peniaze na tu vec na ktoru si setrim :) \n 3) Lego+ cokolvek :) \n"  )
    input("Stlac ENTER pre ukoncenie programu")

def klam():
    print("Sice mi to lichoti ale obaja vieme ze to nieje pravda :D \nSkusim sa polepsit. Asi mi to kazi moja \"zavislost na pc\", travenie malo casu s rodinou...")
    input("Stlac ENTER pre ukoncenie programu")

x = str(input("Bol som tento rok zly? (ano/ nie)")).upper()
if x == "ANO":
    print("Je mi to luto, skusim sa polepsit. Asi to mohlo byt mojou \"zavislostou na pc\", travenim malo casu s rodinou... ")
    oA = str(input("Ospravedlnenie akceptovane? (ano/ nie)")).upper()
    if oA == "ANO":
        print("Dakujem, budem sa snazit zlepsit sa ;) ")
        wish()
    if oA == "NIE":
        print(":( \n skoda, odkazte Hugovi co tam este chybalo, Dakujem :) \n")
        input("Stlac ENTER pre ukoncenie programu")
if x == "NIE":
    klam()

