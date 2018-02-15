#Jung Kim
#CS-21 Finals, Section IV
#Problem 8
#String manipulation

def create_string(string):
	new_string = "" #this is the parsed string that contains every other letter starting from the first
	reversed_string = "" #the new string but in reverse
	for n in range(0, len(string), 2): #goes through every other letter in the input string
		if n == 0: #to capitalize the first letter
			new_string = new_string + string[n].upper()
		elif n == len(string) - 1: #to capitalize the last letter for odd numbered words
			new_string = new_string + string[-1].upper()
		elif n == len(string) - 2: #to capitalize the last letter for even numbered words
			new_string = new_string + string[-2].upper()
		else: #adds all the letters in between
			new_string = new_string + string[n]
	for letter in range(len(new_string),0,-1): #this reverses the word by going through each letter from last to first
		reversed_string = reversed_string + new_string[letter - 1] #adds backwards to create the reversed
	print(reversed_string)
	
def main():
	string = input("Type in whatever string here\n<If the first or last characters are not in the English alphabet then they won't be capitalized!>\n Enter here: ")
	create_string(string)
main()