from random import choice

word = list(choice(["lorem", "ipsum", "dolor", "sit", "amet"]))

empty = ["_" for _ in range(len(word))]

max_guesses = len(word) + 2
past = []
print(f'Maximálny počet pokusov: {max_guesses}')

while max_guesses > 0:
    print(f'Pokus: {max_guesses}. Hľadané slovo: {" ".join(empty)}. Zoznam pokusov: {" ".join(past)}')
    guess = input("Zadajte svoj tip: ")
    max_guesses -= 1
    if guess in past:
        print("Tento tip už ste použili. Zadajte iný.")
        max_guesses += 1
        continue
    past.append(guess)
    if len(guess) > 1:
        if guess != "".join(word):
            print("Nesprávne")
            continue
        else:
            print("Vyhrali ste!")
            break
    else:
        if guess not in word:
            print("Nesprávne")
            continue
        empty = [guess if empty[i] == "_" and guess == word[i] else empty[i] for i in range(len(word))]
        if "_" not in empty:
            print("Vyhrali ste!")
            break

print(f'Počet chybných pokusov: {(len(word) - 2) - max_guesses}')
