from random import shuffle


with open("poprehadz.txt", "r") as f:
    data = [x.split(" ") for x in f.read().splitlines()]

for line in data:
    for word in line:
        endI = len(word)-1
        if not word[-1].isalpha():
            endI -= 1 
        base = list(word[1:endI])

        shuffle(base)

        buf = f'{word[0]}{"".join(base)}{word[endI]}'
        if endI == -2:
            buf += word[-1]
        if len(word) == 1:
            buf = word
        print(buf, end=" ")










