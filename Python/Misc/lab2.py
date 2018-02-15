def reversal():
	word=eval(input("What word will you like to reverse?: ")) #the word the user wants to reverse
	type(word) == str #checking the type of input; need to improve exception handling error
	reverse = "" #setting variable for reversed word
	length = len(word) #length of word
	for letter in range(length,0,-1): #counting the letters of the word and rewriting them backwards
		reverse = reverse + word[letter - 1]
	print(reverse)

def Palindrome():
	word=eval(input("Palindrome?: ")) #same code as reversal
	type(word) == str
	reverse = ""
	length = len(word) #length of word
	for letter in range(length,0,-1):
		reverse = reverse + word[letter - 1]
	if reverse == word: #if statement to check if the word is a palindrome by comparison
		print("True,", reverse, "is a palindrome of ", word)
	else:
		print("False, ", reverse, "is not a palindrome of ", word)
		
def main():
	roster = [{}] #a list of dictionaries each containing name and age
	counter = 0 #position counter for dictionaries in list
	for counter in range (0,10): #a for loop to add a new dictionary for new entry up to 10 people
		roster.append({}) #creates a new blank dictionary within the list
		roster[counter]["first"] = input("First name: ")   #Asks the user to input a variety of information
		roster[counter]["last"] = input("Last name: ")
		roster[counter]["age"] = eval(input("Date of birth (age): "))
		counter = counter + 1 #Moves counter forward by one
	oldest = roster[0]["age"] #the oldest age in the list called roster
	record = 0 #counter for the dictionary entry of the oldest person
	for counter1 in range (0,10): #for loop to compare ages for oldest
		if (oldest < roster[counter1]["age"]): #if loop to input oldest age value into 'oldest'
			oldest = roster[counter1]["age"]
			record = counter1
	youngest = roster[0]["age"] #the youngest age
	record1 = 0 #counter for the dictionary entry for the youngest person
	for counter2 in range (0,10): #for loop to compare ages for youngest
		if (youngest > roster[counter2]["age"]): #if loop to input youngest age value into 'youngest'
			youngest = roster[counter2]["age"]
			record1 = counter2
	print("The oldest person is ", roster[record]["first"], ", s/he is ", oldest, "years old. " "And the youngest person is ", roster[record1]["first"], ",s/he is ", youngest, "years old.")
	

def anagram():
	word = input("Anagram, word one: ")
	anagram = input("Word two: ")
	if sorted(word) == sorted(anagram):
		print("True")
	else:
		print("False")

def main():
	listed_numbers = eval(input("Please enter a set of numbers separated by commas: "))
	target_number = eval(input("What sum are you looking for?: "))
	for augend in range(0,len(listed_numbers)-1):
		for addend in range(augend+1,len(listed_numbers)):
			if listed_numbers[augend] + listed_numbers[addend] == target_number:
				print(listed_numbers[augend], " + ", listed_numbers[addend], " = ", target_number)

		
def main():
	anagram()
main()