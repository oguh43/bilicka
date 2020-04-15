import sys
def dragon():
    ls = [2,3]
    days = int(input("Number of days? "))
    for i in range(days):
        ls.append((ls[-2]*ls[-1])+(abs(ls[-2]-ls[-1])))
    print(ls[-2])

def sentence():
    sys.exit()
    words = str(input("Medzerami oddelené slová: ")).split(" ")
    word_len = len(words)

    even = 0
    odd = 0
    for i in range(0,word_len,2):
        even = even + len(words[i])
    print("Even: %i"%(even))
    for i in range(1,word_len,2):
        odd = odd + len(words[i])
    print("Odd: %i"%(odd))

    if even >= odd:
        print("Max len() is: %i"%(even))
    else:
        print("Max len() is: %i"%(odd))

def r_dragon():
    def stuff(days):
        if days != 0:
            ls.append((ls[-2]*ls[-1])+(abs(ls[-2]-ls[-1])))
            days = days-1
            return stuff(days)
        else: return ls[-2]
    ls = [2,3]
    print(stuff(int(input("Days? "))))

#####################################
"""def copy():
    a = words
    cpy = 1
    return a

def around_index(use,count):
    if cpy == 0:
        use = copy()
    print(use)
    ind = use.index(max(use,key=len))
    print("chose: ",use[ind])
    ind_left = ind-1
    ind_right = ind+1
    count = count +len(use[ind])
    #try:
    if ind_left < 0:
        ind_left = 0
    del use[ind_left:ind_right+1]
        #use.remove(use[ind_left]:use[ind_right])
        #use.remove(use[ind_left])
        #use.remove(use[ind_right+1])
    #except Exception:
    #    pass

    if len(use) != 0:
        print("hey",use)
        return around_index(use,count)
    else:
        print("end",use)
        return count

count = 0
cpy = 0
words = input("ye: ").split(" ")
print(around_index(words,count))
#print(max(words, key = len))

# ahoj ako sa pozdravis predvcerom ibazeby nie"""
###############################################
"""def wordCounter(cena,t,sucet):
    for j in cena:
        if cena[t - 1] > cena[t]:
            sucet = sucet + cena[t - 1]
            t += 2
            if t<=(len(cena)-1):
                wordCounter(cena,t,sucet)
            else:
                if (t-1)<=(len(cena)-1):sucet = sucet + cena[t-1]
                return sucet
        if cena[t - 1] < cena[t]:
            sucet = sucet + cena[t]
            t += 3
            if t<=(len(cena)-1):
                wordCounter(cena,t,sucet)
            else:
                if (t-1)<=(len(cena)-1):sucet = sucet + cena[t-1]
                return sucet
        if cena[t - 1] == cena[t]:
            if t+2 > (len(cena)-1) or t+1 > (len(cena)-1):
                sucet = sucet+cena[t]
                return sucet
            else:
                if cena[t + 1] < cena[t + 2]:
                    sucet = sucet + cena[t]
                    t += 3
                    if t <= (len(cena) - 1):
                        wordCounter(cena, t, sucet)
                    else:
                        if t - 1 <= (len(cena) - 1): sucet = sucet + cena[t - 1]
                        return sucet
                else:
                    sucet = sucet + cena[t-1]
                    t += 2
                    if t <= (len(cena) - 1):
                        wordCounter(cena, t, sucet)
                    else:
                        return sucet

slova = input("Zadaj zoznam slov:").split(" ")
suma = []
index = 1
sucet = 0
print(slova)
for i in range(0,len(slova)):
    suma.append(len(slova[i]))

print("Maximalny počet písmen:",(wordCounter(suma,index,sucet)))
"""





import random

def show():
    print("Karty sú: %i; %i"%(ls[0],ls[1]))
    used.append(ls[0])
    used.append(ls[1])
    del ls[0:2]

def choice(kolo):
    if starter == 0:
        mode = "ai"
    else:
        mode = "user"

    if mode == "user":
        show() 
        if int(input("Pick a card, 1 or 2? ")) == 1:
            player.append(used[-2])
            ai.append(used[-1])
            mode == "ai"
            kolo = kolo + 1
        else:
            player.append(used[-2])
            ai.append(used[-1])
            mode == "ai"
            kolo = kolo + 1

    else:
        show()
        if kolo == 1:
            temp1 = used[-2]
            temp2 = used[-1]
            if temp1 > temp2 and temp1 != 12:
                player.append(used[-1])
                ai.append(used[-2])
                print("ai chose %i"%(temp1))
            elif temp2 > temp1 and temp2 != 12:
                player.append(used[-2])
                ai.append(used[-1])
                print("ai chose %i"%(temp2))


    print(ai)
    print(player)

used,player,ai,temp1,temp2 = [],[],[],None,None
ls = [1,2,3,4,5,6,7,8,9,10,11,12]
random.shuffle(ls)
#starter = random.randint(0,1)
starter = 0
print(starter)
kolo = 1
#choice(kolo)

ls = [1,2,3,4,5,6,7,8,9,10,11,12]
test = [1,2,3,4,6,7,9]
te = []
print(test[0] and test[1] in ls)
"""for i in range(0,len(test)):
    print(i)
    try:
        if test[i] and test[i+1] and test[i+2] in ls:
            te.append(test[i])
            te.append(test[i])
            print(te)
    except Exception:
        pass
"""
for i in range(len(test)):
    print(i)
    if test[i] != ls[i]:
        ind = test.index(test[i])
        test.insert(ind," ")
        print(test)

print(test)
print(ls)

print(test[0]==ls[0])




"""def copy():
    a = words
    cpy = 1
    return a

def around_index(use,count,override):
    if cpy == 0:
        use = copy()
    print(use)
    
    ind = use.index(max(use,key=len))
    if worth(ind) == 0:
        
    print("chose: ",use[ind])
    ind_left = ind-1
    ind_right = ind+1
    count = count +len(use[ind])
    #try:
    if ind_left < 0:
        ind_left = 0
    del use[ind_left:ind_right+1]
        #use.remove(use[ind_left]:use[ind_right])
        #use.remove(use[ind_left])
        #use.remove(use[ind_right+1])
    #except Exception:
    #    pass

    if len(use) != 0:
        print("hey",use)
        return around_index(use,count)
    else:
        print("end",use)
        return count

count = 0
cpy = 0
words = input("ye: ").split(" ")
print(around_index(words,count,0))"""


# ahoj ako sa pozdravis predvcerom ibazeby nie
#print(max(words, key = len))



"""
words = str(input("Medzerami oddelené slová: ")).split(" ")
word_len = len(words)
mx = max()
"""
"""
def calculateHydra(firstday, secondday, days):
    newday = (firstday*secondday) + (abs(firstday-secondday))
    firstday = secondday
    secondday = newday
    if days > 1:
        days = days-1
        return calculateHydra(firstday,secondday, days)
    return firstday
    
    
    


daysinp = int(input("Počet dní:"))
day0 = 2
day1 = 3

print(calculateHydra(day0, day1, daysinp))


dragon()
"""


"""
n = int(input("Počet kociek:"))
m = int(input("Číslo, ktoré hádžeme:"))
solutions = 0

if n==1:
    if m>6: solutions = 0
    if m<6: solutions = 1
if n==2: solutions = m-1 + (6*n)-(n-(n-1))

possibility = solutions/(6**n)
print("Pravdepodobnosť:",(possibility*100), "%")
"""

"""
def probability_of_sum(x, n, sides=6)
  return 0 if x < n
  single_die_probs = Array.new(sides) { Rational(1,sides) }

  combined_probs = [1] # Represents chance of getting 0 when rolling 0 dice :-)

  # This is not the most efficient way to do this, but easier to understand
  n.times do
    start_probs = combined_probs
    combined_probs = []
    start_probs.each_with_index do |prob_a,i_a|  
        single_die_probs.each_with_index do |prob_b,i_b| 
          combined_probs[i_a + i_b] = ( combined_probs[i_a + i_b] || 0 ) + prob_a * prob_b
        end
    end
  end

  combined_probs[ x - n ] || 0
end

puts probability_of_sum(400, 100).to_f
# => 0.0003172139126369326
"""