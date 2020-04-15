#Hugo
from random import *

def pos(test):    
    postupka = []
    temp = []
    dlzka = 0
    for i in test:
        if str(i).isdigit() == True:
            dlzka = dlzka +1
            temp.append(i)
        elif str(i).isdigit() == False and dlzka >= 3:
            dlzka = 0
            postupka.append(temp.copy())
            temp.clear()
        elif str(i).isdigit() == False and dlzka < 3:
            dlzka = 0
            temp.clear()
    if dlzka >= 3:
        postupka.append(temp)
    return postupka

def check_straight(test):
    test.sort()
    pl = test[0]
    for i in range(len(test)+8):
        try:
            if test[i] != pl:
                test.insert(i," ")
            pl = pl + 1
        except Exception:
            pass
    return pos(test)

def longest(test):
    ln = []
    for i in test:
        ln.append(len(i))
    if len(set(ln)) > 1:
        return test.index(max(test, key=len))
    else:
        return -1

def winner(after_ai,after_player):
    if len(after_ai) == 0 and len(after_player) > 0:
        return "player"
    elif len(after_player) == 0 and len(after_ai) > 0:
        return "ai"
    elif len(after_ai) == 0 and len(after_player) == 0:
        return "tie"
    lon_ai = longest(after_ai)
    lon_pl = longest(after_player)
    if len(after_ai[lon_ai]) > len(after_player[lon_pl]):
        return "ai"
    elif len(after_player[lon_pl]) > len(after_ai[lon_ai]):
        return "player"
    mx_ai = after_ai[lon_ai][-1]
    mx_pl = after_player[lon_pl][-1]
    if mx_ai > mx_pl:
        return "ai"
    elif mx_pl > mx_ai:
        return "player"
    elif mx_pl == mx_ai:
        return "tie"

#Štefan
def ai(cur1, cur2, ailist,current,player):
    no , pc = 0 , ailist
    if len(ailist) == 0:
        pc.append(max(current))
        current.remove(max(current))
        player.append(current[0])
    elif len(ailist) > 0:
        pc.sort(reverse=True)
        for x in range(1, len(pc)):
            if cur1 == pc[x] + 1 and no == 0 or cur1 == pc[x] - 1 and no == 0:
                current.remove(cur1)
                pc.append(cur1)
                player.append(current[0])
                no = 1
            elif cur2 == pc[x] + 1 and no == 0 or cur2 == pc[x] - 1 and no == 0:
                current.remove(cur2)
                pc.append(cur2)
                player.append(current[0])
                no = 1
        if no != 1:
            pc.append(max(current))
            current.remove(max(current))
            player.append(current[0])

def game(shuffled):
  shuffle(shuffled)
  player, pc , res = [] , [] ,[]
  for i in range(1, 12, 2):
      print("********************************")
      current = [shuffled[i - 1], shuffled[i]]
      print("These are the two cards: " + str(shuffled[i - 1]) + ", " + str(shuffled[i]))
      if i == 1:
          first = randint(0,1)
          if first == 0:
              print("***The player goes first***")
          elif first == 1:
              print("***The A.I. goes first***")
      else:
          if first == 0:
              first = 1
              print("***Its the A.I.s turn***")
          elif first == 1:
              print("***Its the players turn***")
              first = 0
      if first == 0:
          player.sort();pc.sort()
          if i != 1:
              print("You have:",str(player),"on your hand")
              print("Pc has:",str(pc),"on its \'hand\'")
          usrin = int(input("Pick one card: "))
          current.remove(usrin)
          player.append(usrin)
          pc.append(current[0])
      elif first == 1:
          ai(current[0], current[1], pc,current,player)
          print("The A.I. picked " + str(pc[-1]))
  return player,pc

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
res = game(ls)
print(winner(check_straight(res[1]),check_straight(res[0])))
