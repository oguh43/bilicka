import math
import itertools

from sortedcontainers import SortedSet

def rsa() -> None:
    private_key=[]
    public_key=[]
 
    p=int(input("p?"))
    q=int(input("q?"))
 
    N=p*q
    f=(p-1)*(q-1)
 
    for e in range(1,f):
        if math.gcd(e,N)==1:
            if math.gcd(e,f)==1:
                private_key.append(tuple([e, N]))
                for d in range(50):
                    if (d*e)%f==1:
                        public_key.append(tuple([d, N]))
 
    print("Private key:")
    print(SortedSet(private_key))
    print("Public key:")
    print(SortedSet(public_key), end="\n\n")

    ask()
 
def xor() -> None:
    def bXor(*, msg: str, key: str) -> str:
        result = ""
        for m, k in zip(msg, itertools.cycle(key)):
            if m == k:
                result += "0"
            else:
                result += "1"
        return result
 
    msg = str(input("Message? "))
 
    key = str(input("Key? "))
 
    print(bXor(msg=msg, key=key), end="\n\n")
    ask()
 
def ask() -> None:
    a = str(input("1) XOR\n2) RSA\nCypher?"))
    if a=="1":
        xor()
    elif a=="2":
        rsa()
 
ask()
