def confirming(): #a confirm function used throughout the code to increase efficiency
	user_confirm = "yes"
	confirm = ["yes"]
	return(user_confirm, confirm)

def add_players(): #still not fully debugged
	user_confirm, confirm = confirming()
	user_confirm = ""
	computers = []
	while user_confirm not in confirm:
		num_npcs = int(input("How many computer players?: "))
		print("\nThere are", num_npcs, "NPCs playing.\nIs that correct?")
		user_confirm = input("(Y/N): ")
		if (user_confirm in confirm):
			print("\nLet's get started")
	for npc in range(0,num_npcs):
		computers.append(npc)
		computers[npc] = "NPC" + str(npc + 1)
		computers[npc] = [computers[npc]]
	return computers
	
def poker_deck():
	deck_template = ["02a", "02b", "02c", "02d", "03a", "03b", "03c", "03d", "04a", "04b", "04c", "04d", "05a", "50b", "05c", "05d", "06a", "06b", "06c", "06d", "07a", "07b", "07c", "07d", "08a", "08b", "08c", "08d", "09a", "09b", "09c", "09d", "10a", "10b", "10c", "10d", "11a", "11b", "11c", "11d", "12a", "12b", "12c", "12d", "13a", "13b", "13c", "13d", "14a", "14b", "14c", "14d",]
	burn = []
	community_cards = []
	return(deck_template, burn, community_cards)
	
def deal_card(computers,deck):
	import random
	deck_template, burn, community_cards = deck
	playing_deck = deck_template[:]
	random.shuffle(playing_deck)
	new_deck = [] #append playing_deck.pop
	#loop to play over again
	n = 0
	player = []
	for deal in range(0,2):
		player.append([playing_deck.pop()])
		if int(player[deal][0][0] + player[deal][0][1]) > 13:
			player[deal].append("Ace")
		elif int(player[deal][0][0] + player[deal][0][1]) > 12:
			player[deal].append("King")
		elif int(player[deal][0][0] + player[deal][0][1]) > 11:
			player[deal].append("Queen")
		elif int(player[deal][0][0] + player[deal][0][1]) > 10:
			player[deal].append("Jack")
		else:
			player[deal].append(int(player[deal][0][0] + player[deal][0][1]))
	for card in player:
		if card[0][2] == "a":
			card.append("clubs")
		elif card[0][2] == "b":
			card.append("diamonds")
		elif card[0][2] == "c":
			card.append("hearts")
		else:
			card.append("spades")
	#print(player)
	#if int(player[0][0][0] + player[0][0][1]) > 13
	#elif player[0][0][0] + player[0][0][1] > 12
	#elif player[0][0][0] + player[0][0][1] > 11
	#player[0][0][0] + player[0][0][1] > 10
	#else:
	print(player)
	print("You have a", player[0][0][0] + player[0][0][1], "of", player[0][2], "and a", player[1][0][0]+player[1][0][1], "of", player[1][2])
	for deal in range(0,2):
		for n in range(0,len(computers)):
			computers[n].append([playing_deck.pop()])
	for n in range(0,len(computers)):  #try for player in players
		for i in range(1,len(computers[n])):
			if computers[n][i][0][2] == "a":
				computers[n][i].append("clubs")
			elif computers[n][i][0][2] == "b":
				computers[n][i].append("diamonds")
			elif computers[n][i][0][2] == "c":
				computers[n][i].append("hearts")
			else:
				computers[n][i].append("spades")
	#for npc in computers:
	#	print(npc[0], "has a", npc[1][0][0]+npc[1][0][1], "of", npc[1][1])
	#placeholder for betting; first betting round (pre-flop)
	dealer(playing_deck,deck)
	
def dealer(playing_deck,deck):
	deck_template, burn, community_cards = deck
	#placeholder for betting; second betting round (flop)
	burn.append(playing_deck.pop())
	for flop in range(0,3):
		community_cards.append([playing_deck.pop()])
	for n in range(0,len(community_cards)):
		if community_cards[n][0][2] == "a":
			community_cards[n].append("clubs")
		elif community_cards[n][0][2] == "b":
			community_cards[n].append("diamonds")
		elif community_cards[n][0][2] == "c":
			community_cards[n].append("hearts")
		else:
			community_cards[n].append("spades")
	#print(community_cards)
	#placeholder for bet function; third betting round (turn)
	burn.append(playing_deck.pop())
	community_cards.append([playing_deck.pop()])
	#for turn in range(3,len(community_cards)):
	if community_cards[3][0][2] == "a":
		community_cards[3].append("clubs")
	elif community_cards[3][0][2] == "b":
		community_cards[3].append("diamonds")
	elif community_cards[3][0][2] == "c":
		community_cards[3].append("hearts")
	else:
		community_cards[n].append("spades")
	#print(community_cards)
	#placeholder for betting; fourth betting round (river)
	burn.append(playing_deck.pop())
	community_cards.append([playing_deck.pop()])
	#for river in range(4,len(community_cards)):
	if community_cards[4][0][2] == "a":
		community_cards[4].append("clubs")
	elif community_cards[4][0][2] == "b":
		community_cards[4].append("diamonds")
	elif community_cards[4][0][2] == "c":
		community_cards[4].append("hearts")
	else:
		community_cards[4].append("spades")
	print(community_cards)
	
def hand_eval(computers,deck):
	deck_template, burn, community_cards = deck
	high_card = 1
	one_pair = 2
	two_pair = 3
	three_kind = 4
	straight = 5
	flush = 6
	full_house = 7
	four_kind = 8
	straight_flush = 9
	royal_flush = 10
	

def main():
	computers = add_players()
	deck = poker_deck()
	deal_card(computers,deck)
	hand_eval(computers,deck)
main()