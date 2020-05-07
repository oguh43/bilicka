import sys
def dragon():
    ls = [2,3]
    days = int(input("Number of days? "))
    for i in range(days):
        ls.append((ls[-2]*ls[-1])+(abs(ls[-2]-ls[-1])))
    print(ls[-2])

def r_dragon():
    def stuff(days):
        if days != 0:
            ls.append((ls[-2]*ls[-1])+(abs(ls[-2]-ls[-1])))
            days = days-1
            return stuff(days)
        else: return ls[-2]
    ls = [2,3]
    print(stuff(int(input("Days? "))))
