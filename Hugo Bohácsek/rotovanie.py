ls = [__import__("random").randint(1,50) for _ in range(10)]
print(ls)
ls.insert(len(ls) if (inp:=input("Kam? L/R? > ").lower()) == "l" else 0, ls.pop(0 if inp == "l" else -1))
print(ls)