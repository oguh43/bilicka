def isRetarded(n):
    for i in range(len(str(n))-1):
      if int(str(n)[i])<int(str(n)[i+1]):
        return False
    return True

def isPrime(n):
    if n<2:
        return False
    for i in range(2, n//2+1):
      if n%i==0:
        return False
    return True


p = int(input("Pocet cifier: "))
d = 0
h = 0
ls = []
for i in range(10**(p-1), int(str(9)*p)):
    if isPrime(i):
        if isRetarded(i):
            ls.append(i)
print(ls)