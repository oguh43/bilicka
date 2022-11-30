m = [[__import__("random").randint(1,100) for _ in range(5)] for q in range(10)]
c = int(input("Číselko? > "))
f = True
for i in range(0, len(m[c]) - 1):
    if m[c][i] >= m[c][i+1]:
        f = False
print(f)
