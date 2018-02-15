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
	
main()