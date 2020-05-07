from random import randint, shuffle

def winner(player_hand,ai_hand):
	player_hand = straight(player_hand)
	ai_hand = straight(ai_hand)
	if len(player_hand) == 0 and len(ai_hand) != 0:
		return "ai"
	elif len(player_hand) != 0 and len(ai_hand) == 0:
		return "you"
	elif len(player_hand) == 0 and len(ai_hand) == 0:
		return "tie"
	longest_player, longest_ai = longest(player_hand), longest(ai_hand)
	highest_player, highest_ai = player_hand[longest_player][-1], ai_hand[longest_ai][-1]
	if len(ai_hand[longest_ai]) > len(player_hand[longest_player]):
		return "ai"
	elif len(ai_hand[longest_ai]) < len(player_hand[longest_player]):
		return "you"
	if highest_player > highest_ai:
		return "you"
	elif highest_player < highest_ai:
		return "ai"
	elif highest_player == highest_ai:
		return "tie"
	else: return "err"
					
def longest(test):
	return test.index(max(test,key=len))
	
def straight(test):
	test.sort()
	temporary, straight = [], []
	for i in range(1,len(test)):
		if test[i-1] + 1 == test[i]:
			temporary.append(test[i-1])
			temporary.append(test[i])
		elif test[i-1] + 1 != test[i] and len(set(temporary)) >= 3:
			straight.append(list(set(temporary)).copy())
			temporary.clear()
		else:
			temporary.clear()
	if len(set(temporary)) >= 3:
		straight.append(list(set(temporary)).copy())
	return straight

cards = [1,2,3,4,5,6,7,8,9,10,11,12]
pl = cards.copy()
pl1 = cards.copy()
for i in range(3):
	try:
		pl.pop(randint(0,len(pl)))
	except Exception:
		pass
for i in range(3):
	try:
		pl1.pop(randint(0,len(pl1)))
	except IndexError:
		pass
print(winner(pl,pl1))
