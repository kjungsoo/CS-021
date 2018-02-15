#Jung Kim
#CS-21 Intro to programming
#Coding lab 4 - flagging suspicious e-mails
#It will output various information outlined in the lab instructions
#The program has been generalized for any text files written in standard e-mail format

def open_email(): #simple function to open e-mails
	textfile = input("") #please input a text file to test
	file = open(textfile, "r")
	return file #returns the text file it opened

def read_email(): #function reads and duplicates e-mail
	file = open_email() #sets variable for return value of open email function
	email_copy = [] #creates the template for the duplicate
	x = ['\n'] #step to get rid of the newlines; somewhat redundant as it could have been included in "special_characters" variable and removed all unwanted characters in email
	x = x[0].rstrip('\n')
	n = 0 #an arbitrary counter for the newline
	for line in file: #creates the duplicate email without newlines
		email_copy = email_copy + [line.rstrip('\n')]
	while x in email_copy: #deletes remaining newlines
		if (email_copy[n] == x):
			del email_copy[n]
		n = n + 1 #increasing counter to allow loop to cycle through the duplicate email line by line
	file.close() #closes original file as it is now unneeded
	return(email_copy) #returns the duplicate email for all the other functions to use	
	
def body_email(email): #this identifies the body of the email
	word_count = [] #creates a list to count words
	sentence_count = [] #creates a list to count sentences
	signature = ['Regards,', 'Best,', 'Sincerely,', 'Thank you,'] #common signatures people usually use; need manual input of various signatures, unnavoidable flaw(?)
	for n in range(0,len(email)): #the next two for loops identifies various "keywords" to help locate the body of the paragraph
		if (email[n].find('To:') != -1):
			receiver_index = n
	for n in range(0,len(email)):
		if (email[n] in signature):
			signature_index = n
	for n in range(receiver_index+2,signature_index): #uses the "keywords" to separate the body of the paragraph from rest of email
		word_count = word_count + email[n].rsplit(None) #the length of the entire body of the paragraph
		sentence_count = sentence_count + [email[n]]	
	return(word_count, sentence_count) #returns the body of the paragraph separated into words and sentences
	
def count_email(email): #this function counts the words and sentences in the email
	cleaned_sentence_count = {} #a dictionary to completely clean up the entire email of all unnecessary characters, could have been moved to read_email(), again somewhat redundant. will be revised later
	x = ['\n'] #same as read_email()
	x = x[0].rstrip('\n')
	word_count, sentence_count = body_email(email)
	annoying_delimiters = [',',' ','@','#','$','%','^'] #the annoying delimiters and special characters that will be removed except for '.', '!' and '?' as they signify the end of a sentence
	for n in range(0,len(annoying_delimiters)): #clean up
		cleaned_sentence_count[str(n)] = " ".join(sentence_count)
		cleaned_sentence_count[str(n)] = cleaned_sentence_count[str(n)].rsplit(annoying_delimiters[n])
		sentence_count = cleaned_sentence_count[str(n)]
	for n in range(0,len(sentence_count)): #gets a list of sentences in the body of the email
		sentence_count = sentence_count[n].replace('?','.').replace('!','.').rsplit('.') #the function returns errors when multiple '!' and/or '?' and/or ellipses are present. need help with revision
	for n in range(len(sentence_count)): #gets rid of the newline here as well, the clean up with the annoying delimiter left a '' character which was leftover from a newline character
		if (sentence_count[n] == x):
			del sentence_count[n]
	print("The length of the E-mail is", len(word_count),"words.") #reports the word count
	print("The E-mail contains", len(sentence_count),"sentences.") #and the sentence count
	
def extract_names(email): #a function to find the names & email of the sender/receiver, only took into account 1 receiver. multiple receiver would require further revision
	sender_email = ""
	sender = ""
	receiver_email = ""
	receiver = ""
	for n in range(0, len(email)): #sets multiple indicators for locating both sender and emails, will not work if email is not in standard format.
		if (email[n].find('<') != -1):
			if 'To' in email[n]:
				receiver_index = n
				receiver_email_index = email[n].index('<')
				receiver_email_end = email[n].index('>')
				receiver_indicator = email[n].index(':')
			else:
				sender_index = n
				sender_email_index = email[n].index('<')
				sender_email_end = email[n].index('>')
	for n in range(1, sender_email_end - sender_email_index): #sender's email
		sender_email = sender_email + email[sender_index][sender_email_index+n]
	for n in range(1, receiver_email_end - receiver_email_index): #receiver's email
		receiver_email = receiver_email + email[receiver_index][receiver_email_index+n]
	for n in range(0, sender_email_index - 1): #sender's name
		sender = sender + email[sender_index][n]
	for n in range(receiver_indicator + 2, receiver_email_index - 1): #receiver's name
		receiver = receiver + email[receiver_index][n]
	print("Sender's name: ",sender,"\nSender's e-mail address: ",sender_email)
	print("Recipient's name: ",receiver,"\nRecipient's e-mail address: ",receiver_email)

def extract_title(email): #simple function; however subject of email relies on email being in standard format. will require revision otherwise
	print("Subject: ",email[0])
	for n in range(0, len(email)): #locates time-stamp of the email using the ':' present in time of day and 'AM' or 'PM'
		if(email[n].find(':') != -1):
			if ('AM' in email[n] or 'PM' in email[n]):
				time_stamp = n
	print(email[time_stamp])

def flag_email(email): #flags the email for suspicious activity
	body_length, sentence_count = body_email(email) #calls the body_email functions to later determine what is "high frequency"
	email_vocab = [] #a list of all the words in the email
	flagged_term = [] #a list of all the words in the email that has been flagged as 'dangerous'
	unique_flagged_term = [] #unique flagged terms prevents the program from reporting duplicates (when there are multiple of the same flagged word, it would report each of them however many times they appeared in the email, ie it will report 'bomb appeared x times' x many times)
	cleaned_email = {} #clean up using same method as before, could probably make this a separate function
	total_flag_counter = 0
	flagged_term_index = 0
	priority = 0
	flag_terms = ["dolor", "bomb", "bombs", "arms", "explosives"] #volatile word list, requires manual input
	special_characters = [',','.','?','!','@','#','$','%','^']
	for n in range(0,len(special_characters)):
		cleaned_email[str(n)] = " ".join(email)
		cleaned_email[str(n)] = cleaned_email[str(n)].rsplit(special_characters[n])
		email = cleaned_email[str(n)]
	for n in range(0, len(email)): #adds every word in the email to the list
		email_vocab = email_vocab + email[n].rsplit(None)
	for n in range(0,len(email_vocab)): #adds to the flagged word counter each time it appears, used for determining high frequency
		if (email_vocab[n].lower() in flag_terms):
			total_flag_counter = total_flag_counter + 1
			for i in range (0,len(flag_terms)): #adds the flagged word into the list
				if (email_vocab[n].lower() == flag_terms[i]):
					flagged_term = flagged_term + [email_vocab[n].lower()]
	for n in range(0,len(flagged_term)): #determines how often a flagged term appears, the if/else statement is purely for grammatical correction
		if flagged_term[n] not in unique_flagged_term:
			unique_flagged_term = unique_flagged_term + [flagged_term[n]]
			if (flagged_term.count(flagged_term[n]) == 1):
				print("The word '",flagged_term[n],"' appeared once.", sep='')
			elif flagged_term.count(flagged_term[n]) == 2:
				print("The word '",flagged_term[n],"' appeared twice.", sep='')
			else:
				print("The word '",flagged_term[n],"' appeared ",flagged_term.count(flagged_term[n])," times", sep='')
	for n in range(0,3000): #equating priority to 'high frequency'
		if (total_flag_counter == n):
			priority = n
	if (priority <= len(body_length) * .02): #if the priority of the email (which is equal to the frequency of a flagged term) is only 2% the length of the body of the email then the email is tagged as low-priority (it is still necessary to check this email of suspicious activities!)
		print ("This E-mail has been flagged with low priority.")
	elif (priority <= len(body_length) * .05): #if the priority is 5% the length of the body of the email, then it is set to medium priority
		print ("This E-mail has been flagged with medium priority.")
	elif (priority <= len(body_length) * .9): #if the priority is 9% the length of the body of the email, then it is set to a high priority
		print ("This E-mail has been flagged with high priority.")
	else: #if the priority is greater than 9% of the body, then it requires immediate attention
		print ("This E-mail requires immediate attention.")

def main(): #yay for modularity!
	email = read_email()
	extract_title(email)
	extract_names(email)
	count_email(email)
	flag_email(email)
main()

#the volatile word list (in flag_email(email)) is somewhat short, I only added a few thus far for testing reasons only, likewise with the signatures in body_email(email).