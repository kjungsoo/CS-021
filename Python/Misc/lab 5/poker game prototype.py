def confirming(): #a confirm function used throughout the code to increase efficiency
	user_confirm = "yes"
	confirm = ["yes"]
	return(user_confirm, confirm)

def add_players(): #still not fully debugged
	user_confirm, confirm = confirming()
	user_confirm = ""
	players = []
	npcs = []
	while user_confirm not in confirm:
		num_players = int(input("How many players?: "))
		num_npcs = int(input("How many computers?: "))
		print("\nThere are", num_players, "players and", num_npcs, "NPCs playing.\nIs that correct?")
		user_confirm = input("(Y/N): ")
		if (user_confirm in confirm):
			print("\nLet's get started")
	for player in range(0,num_players):
		players.append(player)
		players[player] = "Player" + str(player + 1)
		players[player] = [players[player]]
	return players

def poker_deck():
	deck_template = ["02a", "02b", "02c", "02d", "03a", "03b", "03c", "03d", "04a", "04b", "04c", "04d", "05a", "50b", "05c", "05d", "06a", "06b", "06c", "06d", "07a", "07b", "07c", "07d", "08a", "08b", "08c", "08d", "09a", "09b", "09c", "09d", "10a", "10b", "10c", "10d", "11a", "11b", "11c", "11d", "12a", "12b", "12c", "12d", "13a", "13b", "13c", "13d", "14a", "14b", "14c", "14d",]
	burn = []
	community_cards = []
	return(deck_template, burn, community_cards)
	
def deal_card(players,deck):
	import random
	deck_template, burn, community_cards = deck
	playing_deck = deck_template[:]
	random.shuffle(playing_deck)
	new_deck = [] #append playing_deck.pop
	#loop to play over again
	print(len(playing_deck))
	for deal in range(0,2):
		for n in range(0,len(players)):
			players[n].append(playing_deck.pop())
			print(players)
	print(len(playing_deck))
	#placeholder for betting; first betting round (pre-flop)
	dealer(playing_deck,deck)

def dealer(playing_deck,deck):
	deck_template, burn, community_cards = deck
	#placeholder for betting; second betting round (flop)
	burn.append(playing_deck.pop())
	for flop in range(0,3):
		community_cards.append(playing_deck.pop())
	print(burn)
	print(community_cards)
	#placeholder for bet function; third betting round (turn)
	burn.append(playing_deck.pop())
	community_cards.append(playing_deck.pop())
	print(burn)
	print(community_cards)
	#placeholder for betting; fourth betting round (river)
	burn.append(playing_deck.pop())
	community_cards.append(playing_deck.pop())
	print(burn)
	print(community_cards)
	
def hand_eval(players,deck):
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
	players = add_players()
	deck = poker_deck()
	deal_card(players,deck)
	hand_eval(players,deck)
main()