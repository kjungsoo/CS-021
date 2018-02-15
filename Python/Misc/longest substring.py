#Repeating substring Algorithim For Both Version A and B (Consecutive repeating letters as well as same letter appearing in a word multiple times)
#This is a general solution for figuring the longest substring in a string, if two consecutive repeating letters can not be allowed. 
#The pseudo-code for this algorithm has been rewritten and translated into a python code.
#By Eric Liu and Jung Kim
#Special mention to logitechfour for being our test subject.

def longest_substring():
	mainstring = input("Enter a word of your liking, we will find the longest part of the word without repeating letters. You have been warned: ")
	substring = [mainstring[0]] #the list for substring without repeating letters
	list_position = 0 #the position counter for the substring list
	conditional = False #if the code detects that there is a repeating letter, it will move to the next iteration
	initial_letter = 0 #first letter of substrings
	primary_letter = 1 #the letter being compared
	compare_letter = 0 #the comparing letter in substring
	while initial_letter < len(mainstring):  #the main loop that runs through all the initial letters of each substring
		primary_letter = initial_letter + 1  #sets primary letter always as one later than initial letter
		while primary_letter < len(mainstring): #the first secondary loop that checks for repeating letters
			compare_letter = initial_letter #ensuring that comparison isn't being made with previous initial letters
			for compare_letter in range(initial_letter, primary_letter): #setting the range of compare letter
				if mainstring[primary_letter] == mainstring[compare_letter]: #the comparison
					conditional = False
					break
				else:
					conditional = True
			if conditional == True:
				substring[list_position]=substring[list_position]+mainstring[primary_letter] #adds the letter to the current substring
			else:
				break
			primary_letter = primary_letter + 1 #increases counter for letter being compared by 1
		initial_letter = initial_letter + 1 #moves the counter to the first letter of the next substring
		if initial_letter < len(mainstring): #prevents index error during last iteration of the main loop
			substring.append(mainstring[initial_letter])
			list_position = list_position + 1 #moves counter to next substring
	longest = substring[0]
	for list_entry in range (1, len(substring)): #finding the longest substring in the list
		if len(longest) < len(substring[list_entry]):
			longest = substring[list_entry]
	print("The longest substring is ", longest, ".") #we warned you.
	return longest_substring

def main():
	longest_substring()
main()