# input: hand (list of strings, the last character of each string representing the suite)
# return: boolean value representing whether or not a pair was found
def pair(hand):
    # first we build a list of the values of the cards in the hand, i.e. forget the suite
    list_of_values = []
    for card in hand:
    	value = card[:-1].lower() # strips the suite from the card. E.g. "As" become "A".
                                  # also converts the value of the card to lower case for easy comparison
    	list_of_values.append(value) # add value for the card to the list of values
		
    # a fast way to do the above is through a Python "list comprehension":
    # list_of_values = [card[:-1].lower() for card in hand]
	
    if len(list_of_values) == len(set(list_of_values)): 
    # set(list) turns a list into a set, in particular,
    # it removes duplicates in a list!
    	return False 
    	# if the size of hand stays the same after 
    	# removing duplicates then there were no dupicates!
    else:
    	return True

# input: hand (list of strings, the last character of each string representing the suite)
# return: boolean value representing whether or not three of a kind was found
def three_of_a_kind(hand):
    # see the comments and code in the "pair" function for explanation
    # and the long way of doing this
    list_of_values = [card[:-1].lower() for card in hand]
	
    # removes duplicates from the list of values
    list_of_distinct_values = list(set(list_of_values)) 
	
    # makes a list of the number of times each distinct value is duplicated in the hand
    # e.g. a 3 in list_of_duplicates means that there were 3 cards with the same value
    # in the hand
    list_of_duplicates = [list_of_values.count(value) for value in list_of_distinct_values]
	
    # checks if there were 3 cards with the same value in the hand
    if 3 in list_of_duplicates:
    	return True
    else:
    	return False


# input: hand (list of strings, the last character of each string representing the suite)
# return: boolean value representing whether or not four of a kind was found
def four_of_a_kind(hand):
    # see the comments and code in the "pair" function for explanation
    # and the long way of doing this
    list_of_values = [card[:-1].lower() for card in hand]
	
    # removes duplicates from the list of values
    list_of_distinct_values = list(set(list_of_values)) 
	
    # makes a list of the number of times each distinct value is duplicated in the hand
    # e.g. a 4 in list_of_duplicates means that there were 4 cards with the same value
    # in the hand
    list_of_duplicates = [list_of_values.count(value) for value in list_of_distinct_values]
	
    # checks if there were 4 cards with the same value in the hand
    if 4 in list_of_duplicates:
    	return True
    else:
    	return False


# input: hand (list of strings, the last character of each string representing the suite)
# return: boolean value representing whether or not two pairs was found
def two_pair(hand):
    # see the comments and code in the "pair" function for explanation
    # and the long way of doing this
    list_of_values = [card[:-1].lower() for card in hand]
	
    # removes duplicates from the list of values
    list_of_distinct_values = list(set(list_of_values)) 

    # makes a list of the number of times each distinct value is duplicated in the hand
    # e.g. a 4 in list_of_duplicates means that there were 4 cards with the same value
    # in the hand
    list_of_duplicates = [list_of_values.count(value) for value in list_of_distinct_values]
	
    # checks if there were more than 1 value that is duplicated in the hand
    if list_of_duplicates.count(2) > 1:
    	return True
    else:
    	return False


# input: hand (list of strings, the last character of each string representing the suite)
# return: boolean value representing whether or not a full house was found
def full_house(hand):
    # see the comments and code in the "pair" function for explanation
    # and the long way of doing this
    list_of_values = [card[:-1].lower() for card in hand]
	
    # removes duplicates from the list of values
    list_of_distinct_values = list(set(list_of_values)) 
	
    # makes a list of the number of times each distinct value is duplicated in the hand
    # e.g. a 4 in list_of_duplicates means that there were 4 cards with the same value
    # in the hand
    list_of_duplicates = [list_of_values.count(value) for value in list_of_distinct_values]
	
    # checks if there were 3 cards with the same value and 2 others with the same value in the hand
    if 3 in list_of_duplicates and 2 in list_of_duplicates:
    	return True
    else:
    	return False
		

# input: hand (list of strings, the last character of each string representing the suite)
# return: boolean value representing whether or not a flush was found
def flush(hand):
    # first we build a list of the suites represented in the hand
    # see the comments and code in the "pair" function for explanation
    # and the long way of doing this
    list_of_suites = [card[-1].lower() for card in hand]
	
    # removes duplicates from the list of suites
    list_of_distinct_suites = set(list_of_suites)
	
	
    # if there are more than one suite in the hand, then it's not a flush
    if len(list_of_distinct_suites) > 1:
    	return False
    else:
    	return True		
