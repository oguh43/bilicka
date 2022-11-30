m, s, z = [[__import__("random").randint(1,100) for _ in range(10)] for q in range(10)], int(input()), int(input())
m[s], m[z] = m[z], m[s]