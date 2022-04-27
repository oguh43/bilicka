from random import randint
players = {}
for i in range(1, int(input("Počet hráčov: ")) + 1):
    players[i] = {
        "name": input(f"Zadajte meno hráča {i}: "),
        "type": input("Zadajte typ hráča (ai/person): ").lower(),
        "pokusy": 0,
        "ai_max": 0,
        "ai_min": 0,
        "guesses": []
    }

range_from = int(input("Zadajte začiatok rozsahu: "))
range_to = int(input("Zadajte koniec rozsahu: "))

tries = ((range_to - range_from + 1) // 2) // len(players.keys())

for k in players.keys():
    players[k]["pokusy"] = tries
    players[k]["ai_max"] = range_to
    players[k]["ai_min"] = range_from

target = randint(range_from, range_to)

def ai(key):
    if players[key]["pokusy"] == 0:
        return False
    players[key]["pokusy"] -= 1
    guess = randint(players[key]["ai_min"], players[key]["ai_max"])
    players[key]["guesses"].append(guess)
    print(f'{players[key]["name"]} háda číslo {guess}')
    if guess == target:
        print(f'{players[key]["name"]} vyhral! Jeho typ: {players[key]["type"]}. Jeho tip: {guess}')
        return True
    else:
        if guess > target:
            print("Hľadám menšie číslo")
            for k in players.keys():
                players[k]["ai_max"] = range_to
        else:
            print("Hľadám väčšie číslo")
            for k in players.keys():
                players[k]["ai_min"] = range_to
        return False

def player(key):
    if players[key]["pokusy"] == 0:
        return False
    players[key]["pokusy"] -= 1
    guess = int(input(f"{players[key]['name']}, zadajte svoj tip: "))
    players[key]["guesses"].append(guess)
    if guess == target:
        print(f'{players[key]["name"]} vyhral! Jeho typ: {players[key]["type"]}. Jeho tip: {guess}')
        return True
    else:
        if guess > target:
            print("Hľadám menšie číslo")
            for k in players.keys():
                players[k]["ai_max"] = range_to
        else:
            print("Hľadám väčšie číslo")
            for k in players.keys():
                players[k]["ai_min"] = range_to
        return False

while tries > 0:
    print(f'Pokus: {tries}')
    for k in players.keys():
        if players[k]["type"] == "ai":
            if ai(k):
                tries = -1
                break
        else:
            if player(k):
                tries = -1
                break
    tries -= 1

if tries == 0:
    print("Remíza!")

print("Štatistiky:")
print(f'Základný rozsah: {range_from} - {range_to}')
print(f'Počet pokusov: {tries}. Počet hráčov: {len(players.keys())}')
print(f'Hľadané číslo: {target}')
print("Hráči:")
for k in players.keys():
    print(f'{players[k]["name"]} - {players[k]["type"]} - {", ".join(map(str, players[k]["guesses"]))} - {str(players[k]["pokusy"])}')



