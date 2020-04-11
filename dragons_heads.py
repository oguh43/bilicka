ls = [2,3]
days = int(input("Number of days? "))
for i in range(days):
    ls.append((ls[-2]*ls[-1])+(abs(ls[-2]-ls[-1])))
print(ls[-1])
