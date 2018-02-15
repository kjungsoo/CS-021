#Jung Kim
#CS-21 Finals, Section IV
#Problem 9
#Pokemon battle simulation

class MiniPokemon(object): #MiniPokemon (pokemon minigame) class creates the pokemon object and gives it randomized stats
	def __init__(self, nickname):
		self.name = nickname #players can decide on their pokemon name
		self.atkpwr = 0 #the attack power of the pokemon
		self.healpwr = 0 #the strength of the 'potion' the trainer can give the pokemon
		self.health = 0 #the total health of the pokemon
		
	def pokemon_stats(self): #randomizes each of the stats 
		import random
		self.atkpwr = random.randint(1, 10)
		self.healpwr = random.randint(1, 5)
		self.health = random.randint(1,20)
		
class Battle(object): #the battle class creates the battle environment (object) and also runs the battle simulation
	def __init__(self, pokemon1, pokemon2): #only 1 vs 1, no team battles
		self.contestant1 = pokemon1
		self.contestant2 = pokemon2
		self.winner = "" #winner TBA
		
	def print_winner(self): #this is when the winner is decided
		from time import sleep #for front-end aesthetics
		print("The winner is...!")
		sleep(1)
		print("\n...\n")
		sleep(1.5)
		print(self.winner, "!!!\n", sep = "")
		
	def match(self, pokemon1, pokemon2): #the battle
		from time import sleep #front-end aesthetics
		import random #to randomize who goes first and what each pokemon does...the trainer has no say.
		actions_1 = [pokemon1.atkpwr, pokemon1.healpwr] #each pokemon can either attack or heal
		actions_2 = [pokemon2.atkpwr, pokemon2.healpwr]
		pokemon1_max_health = pokemon1.health #no over-healing allowed
		pokemon2_max_health = pokemon2.health
		pokemon1_roll = random.randint(1,6) #whoever rolls highest with the 6-sided die wins
		pokemon2_roll = random.randint(1, 6)
		turn = 1 #just a counter for front-end reasons
		print(pokemon1.name, "vs", pokemon2.name, "\n") #each pokemon stats in display
		print(pokemon1.name, "\n-Health:", pokemon1.health, "\n-Attack Power:", pokemon1.atkpwr, "\n-Potion strength:", pokemon1.healpwr)
		print("")
		print(pokemon2.name, "\n-Health:", pokemon2.health, "\n-Attack Power:", pokemon2.atkpwr, "\n-Potion strength:", pokemon2.healpwr, "\n")
		if pokemon1_roll > pokemon2_roll: #the battle simulation if pokemon/player 1 rolls highest
			while pokemon1.health > 0 and pokemon2.health > 0: #battle only continues as long as both are conscious
				sleep(3) #a pause for fun
				print("\nTurn", turn) #and the turn number for fun
				action = random.randint(1, 2) #what will the pokemon do?
				if action == 1: #if it attacks
					pokemon2.health = pokemon2.health - actions_1[0] #the enemy pokemon loses health according to the first pokemon's attack power
					if pokemon2.health < 0: #if it faints then the round is over
						sleep(1.5)
						print(pokemon1.name, "atttacks!")
						print(pokemon2.name, "has taken", actions_1[0], "damage!")
						print(pokemon2.name, "has fainted!\n")
						pokemon2.health = 0
						break
					else: #if it doesn't, match continues
						sleep(1.5)
						print(pokemon1.name, "atttacks!")
						print(pokemon2.name, "has taken", actions_1[0], "damage!")
						print(pokemon2.name, "has", pokemon2.health, "health!\n")
				else: #if it heals
					pokemon1.health = pokemon1.health + actions_1[1] #you heal according to the heal power
					if pokemon1.health > pokemon1_max_health: #of course, no over-healing allowed
						sleep(1.5)
						print(pokemon1.name, "has healed for", actions_1[1] - (pokemon1.health - pokemon1_max_health), "health!") #so you only heal the amount up to your max health
						pokemon1.health = pokemon1_max_health #if you over-heal your set back to maximum health
						print(pokemon1.name, "has", pokemon1.health, "health!\n")
					else:
						sleep(1.5)
						print(pokemon1.name, "has healed for", actions_1[1], "health!") #otherwise, you heal for the full strength of the 'potion'
						print(pokemon1.name, "has", pokemon1.health, "health!\n")
				action = random.randint(1, 2) #now its pokemon/player 2's turn
				if action == 1: #and the same as it was for pokemon 1 except pokemon 2 is damaging/healing
					pokemon1.health = pokemon1.health - actions_2[0]
					if pokemon1.health < 0:
						sleep(1.5)
						print(pokemon2.name, "atttacks!")
						print(pokemon1.name, "has taken", actions_2[0], "damage!")
						print(pokemon1.name, "has fainted!\n")
						pokemon1.health = 0
						break
					else:
						sleep(1.5)
						print(pokemon2.name, "atttacks!")
						print(pokemon1.name, "has taken", actions_2[0], "damage!")
						print(pokemon1.name, "has", pokemon1.health, "health!\n")
				else: #now its player 1's turn
					pokemon2.health = pokemon2.health + actions_2[1]
					if pokemon2.health > pokemon2_max_health:
						sleep(1.5)
						print(pokemon2.name, "has healed for", actions_2[1] - (pokemon2.health - pokemon2_max_health), "health!")
						pokemon2.health = pokemon2_max_health
						print(pokemon2.name, "has", pokemon2.health, "health!\n")
					else:
						sleep(1.5)
						print(pokemon2.name, "has healed for", actions_2[1], "health!")
						print(pokemon2.name, "has", pokemon2.health, "health!\n")
				turn = turn + 1
		else: #the same as above but this is if player 2 rolled higher than player 1, making player 1 go first. A lot of copy-pasting and changing 1s to 2s and 2s to 1s
			while pokemon1.health > 0 and pokemon2.health > 0:
				sleep(2)
				print("Turn", turn)
				action = random.randint(1, 2)
				if action == 1:
					pokemon1.health = pokemon1.health - actions_2[0]
					if pokemon1.health < 0:
						sleep(1.5)
						print(pokemon2.name, "atttacks!")
						print(pokemon1.name, "has taken", actions_2[0], "damage!")
						print(pokemon1.name, "has fainted!\n")
						pokemon1.health = 0
						break
					else:
						sleep(1.5)
						print(pokemon2.name, "atttacks!")
						print(pokemon1.name, "has taken", actions_2[0], "damage!")
						print(pokemon1.name, "has", pokemon1.health, "health!\n")
				else:
					pokemon2.health = pokemon2.health + actions_2[1]
					if pokemon2.health > pokemon2_max_health:
						sleep(1.5)
						print(pokemon2.name, "has healed for", actions_2[1] - (pokemon2.health - pokemon2_max_health), "health!")
						pokemon2.health = pokemon2_max_health
						print(pokemon2.name, "has", pokemon2.health, "health!\n")
					else:
						sleep(1.5)
						print(pokemon2.name, "has healed for", actions_2[1], "health!")
						print(pokemon2.name, "has", pokemon2.health, "health!\n")
				action = random.randint(1, 2)
				if action == 1:
					pokemon2.health = pokemon2.health - actions_1[0]
					if pokemon2.health < 0:
						sleep(1.5)
						print(pokemon1.name, "atttacks!")
						print(pokemon2.name, "has taken", actions_1[0], "damage!")
						print(pokemon2.name, "has fainted!\n")
						pokemon2.health = 0
						break
					else:
						sleep(1.5)
						print(pokemon1.name, "atttacks!")
						print(pokemon2.name, "has taken", actions_1[0], "damage!")
						print(pokemon2.name, "has", pokemon2.health, "health!\n")
				else:
					pokemon1.health = pokemon1.health + actions_1[1]
					if pokemon1.health > pokemon1_max_health:
						sleep(1.5)
						print(pokemon1.name, "has healed for", actions_1[1] - (pokemon1.health - pokemon1_max_health), "health!")
						pokemon1.health = pokemon1_max_health
						print(pokemon1.name, "has", pokemon1.health, "health!\n")
					else:
						sleep(1.5)
						print(pokemon1.name, "has healed for", actions_1[1], "health!")
						print(pokemon1.name, "has", pokemon1.health, "health!\n")
				turn = turn + 1
		if pokemon1.health != 0: #who won? if pokemon 1 did not faint, player 1 wins!
			self.winner = pokemon1.name
		else: #otherwise, player 2 won the game
			self.winner = pokemon2.name

def main(): #modularized :)
	pokemon1 = MiniPokemon("Blastoise")
	pokemon1.pokemon_stats()
	pokemon2 = MiniPokemon("Charizard")
	pokemon2.pokemon_stats()
	fight1 = Battle(pokemon1, pokemon2)
	fight1.match(pokemon1, pokemon2)
	fight1.print_winner()
main()