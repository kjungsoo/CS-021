#Jung Kim
#CS-21
#Project 4 - Merge Sort and Binary Search

confirm = ["yes", "yeah", "y", "yea", "Yes", "Yeah", "Y", "Yea", "1", "YES"] #global confirm variable
def gradebook(textfile):
	roster = [] #empty list which will hold the unsorted roster of students
	roster_data = [] #a list to hold the data from textfile which will be parsed into the roster list
	gradebook_text = textfile #codes read then parse text from designated .txt file
	open_gradebook = open(gradebook_text, "r")
	for line in open_gradebook:
		roster_data.append([line.replace('%','.0').strip('\n')])
	open_gradebook.close()
	for student in roster_data:
		student[0] = student[0].split('; ')
	for student in roster_data:
		for n in range(0,len(student[0])):
			if ',' in student[0][n]:
				student[0][n] = student[0][n].split(', ')
	for student in roster_data:
		student[0][2] = student[0][2].strip("Midterm ")
	for student in roster_data:
		student[0][3] = student[0][3].strip("Final ")
	for student in roster_data:
		student[0][4] = student[0][4].strip("Group project ")
	for student in roster_data:
		student[0][5][0] = student[0][5][0].strip("Quizzes ")
	for student in roster_data:
		student[0][6][0] = student[0][6][0].strip("Labs ")
	for student in roster_data:
		student[0][7][0] = student[0][7][0].strip("Individual projects ")
	for student in roster_data: #after parsing the string in roster data, data is organized into dictionaries in the list, roster.
		roster.append([{"first":student[0][0][0], "last":student[0][0][1], "id":student[0][1], "grades":{"midterm":student[0][2], "final":student[0][3], "group_project":student[0][4], "quizzes":student[0][5], "labs":student[0][6], "individual_projects":student[0][7]}, "overall_grades":{"course_grade":"", "letter_grade":""}, "total_points":{"total_quiz":"", "total_lab":"", "total_indiv_proj":""}}])
	for student in roster_data:
		for quiz in range(0,len(student[0][5])):
			student[0][5][quiz] = float(student[0][5][quiz])
	for student in roster_data:
		for labs in range(0,len(student[0][6])):
			student[0][6][labs] = float(student[0][6][labs])
	for student in roster_data:
		for indiv_proj in range(0,len(student[0][7])):
			student[0][7][indiv_proj] = float(student[0][7][indiv_proj])
	for student in roster: #adds 0 for every missing item in quizzes, labs and individual projects for every student so there is an equal amount of items in each category
		while len(roster[0][0]["grades"]["quizzes"]) < 10:
			student[0]["grades"]["quizzes"] = student[0]["grades"]["quizzes"] + [0.0]
		while len(student[0]["grades"]["quizzes"]) < len(roster[0][0]["grades"]["quizzes"]):
			student[0]["grades"]["quizzes"] = student[0]["grades"]["quizzes"] + [0.0]
		while len(roster[0][0]["grades"]["labs"]) < 10:
			student[0]["grades"]["labs"] = student[0]["grades"]["labs"] + [0.0]
		while len(student[0]["grades"]["labs"]) < len(roster[0][0]["grades"]["labs"]):
			student[0]["grades"]["labs"] = student[0]["grades"]["labs"] + [0.0]
		while len(roster[0][0]["grades"]["individual_projects"]) < 5:
			student[0]["grades"]["individual_projects"] = student[0]["grades"]["individual_projects"] + [0.0]
		while len(student[0]["grades"]["individual_projects"]) < len(roster[0][0]["grades"]["individual_projects"]):
			student[0]["grades"]["individual_projects"] = student[0]["grades"]["individual_projects"] + [0.0]
	calculate_individual_grade(roster)
	return roster

def calculate_individual_grade(roster): #this code calculates the grades of each student, both letter and percent grade
	for student in roster: #goes through every student in the roster

		sorted_quiz_sum = sorted(student[0]["grades"]["quizzes"]) #uses the built in sorted function then removes the lowest two quiz scores
		quiz_sum = (int(sum(sorted_quiz_sum)) - int(sorted_quiz_sum[0]) - int(sorted_quiz_sum[1]))/(len(student[0]["grades"]["quizzes"]) - 2)
		student[0]["total_points"]["total_quiz"] = quiz_sum

		sorted_lab_sum = sorted(student[0]["grades"]["labs"]) #uses built in sorted function then removes the lowest two lab scores
		lab_sum = (int(sum(sorted_lab_sum)) - int(sorted_lab_sum[0]) - int(sorted_lab_sum[1]))/(len(student[0]["grades"]["labs"]) - 2)
		student[0]["total_points"]["total_lab"] = lab_sum

		sorted_proj_sum = sorted(student[0]["grades"]["individual_projects"]) #uses built in sorted function then removes the lowest project score
		indiv_proj_sum = (int(sum(sorted_proj_sum)) - int(sorted_proj_sum[0]))/(len(student[0]["grades"]["individual_projects"]) - 1)
		student[0]["total_points"]["total_indiv_proj"] = indiv_proj_sum

		student[0]["overall_grades"]["course_grade"] = int((float(student[0]["grades"]["midterm"]) * 1.5 + float(student[0]["grades"]["final"]) * 1.5 + float(student[0]["grades"]["group_project"]) + quiz_sum + lab_sum + indiv_proj_sum * (len(student[0]["grades"]["individual_projects"]) - 1)) / 10) #len(roster[0][0]['grades']
		#calculates the overall course grade for each student by adding weighted scores and dividing by total scores
		grade = student[0]["overall_grades"]["course_grade"] #assigns a letter grade according to percent grade
		if grade >= 94:
			letter = "A"
		elif grade >= 90:
			letter = "A-"
		elif grade >= 87:
			letter = "B+"
		elif grade >= 84:
			letter = "B"
		elif grade >= 80:
			letter = "B-"
		elif grade >= 77:
			letter = "C+"
		elif grade >= 74:
			letter = "C"
		elif grade >= 70:
			letter = "C-"
		elif grade >= 67:
			letter = "D+"
		elif grade >= 64:
			letter = "D"
		elif grade >= 60:
			letter = "D-"
		else:
			letter = "F"
		student[0]["overall_grades"]["letter_grade"] = letter
														
def calculate_class_avg(roster): #calculates the class average for each graded item
	class_midterm = [] #lists for each graded item
	class_final = []
	class_group_proj = []
	class_quizzes = []
	class_labs = []
	class_indiv_proj = []
	
	for student in roster: #goes through each of the students grades in the roster and adds them to the list
		class_midterm = class_midterm + [int(float(student[0]["grades"]["midterm"]))]
		class_final = class_final + [int(float(student[0]["grades"]["final"]))]
		class_group_proj = class_group_proj + [int(float(student[0]["grades"]["group_project"]))]
		for items in range(0,len(student[0]["grades"]["quizzes"])):
			class_quizzes = class_quizzes + [int(float(student[0]["grades"]["quizzes"][items]))]
		for items in range(0,len(student[0]["grades"]["labs"])):
			class_labs = class_labs + [int(float(student[0]["grades"]["labs"][items]))]
		for items in range(0,len(student[0]["grades"]["individual_projects"])):
			class_indiv_proj = class_indiv_proj + [int(float(student[0]["grades"]["individual_projects"][items]))]
			
	class_midterm_average = sum(class_midterm) / len(class_midterm) #sums every grade in the list and divide by total number of grades to get average
	class_final_average = sum(class_final) / len(class_final)
	class_group_proj_average = sum(class_group_proj)/len(class_group_proj)
	class_quizzes_average = sum(class_quizzes)/len(class_quizzes)
	class_labs_average = sum(class_labs)/len(class_labs)
	class_indiv_proj_average = sum(class_indiv_proj)/len(class_indiv_proj)
	overall_course_grade = (class_midterm_average + class_final_average + class_group_proj_average + class_quizzes_average + class_labs_average + class_indiv_proj_average) / 6 #averages all the averages to get class average grade
	
	graded_averages = [class_midterm_average, class_final_average, class_group_proj_average, class_quizzes_average, class_labs_average, class_indiv_proj_average, overall_course_grade]
	graded_ranges = [class_midterm, class_final, class_group_proj, class_quizzes, class_labs, class_indiv_proj]
	return [graded_averages, graded_ranges] #organizes every average and score into two lists and returns them for class_range(roster) function
	
def class_range(roster): #finds the lowest and highest scores for each graded item
	graded_avg_and_range = calculate_class_avg(roster)
	lowest_midterm = sorted(graded_avg_and_range[1][0]) #sorts every item in ascending order and finds the first item which is the lowest score
	lowest_midterm = lowest_midterm[0]
	
	lowest_final = sorted(graded_avg_and_range[1][1])
	lowest_final = lowest_final[0]
	
	lowest_group_proj = sorted(graded_avg_and_range[1][2])
	lowest_group_proj = lowest_group_proj[0]
	
	lowest_quizzes = sorted(graded_avg_and_range[1][3])
	lowest_quizzes = lowest_quizzes[0]
	
	lowest_labs = sorted(graded_avg_and_range[1][4])
	lowest_labs = lowest_labs[0]
	
	lowest_indiv_proj = sorted(graded_avg_and_range[1][5])
	lowest_indiv_proj = lowest_indiv_proj[0]
	
	highest_midterm = sorted(graded_avg_and_range[1][0]) #sorts every item in descending order and finds the first item which is the highest score
	highest_midterm = highest_midterm[-1]
	
	highest_final = sorted(graded_avg_and_range[1][1])
	highest_final = highest_final[-1]
	
	highest_group_proj = sorted(graded_avg_and_range[1][2])
	highest_group_proj = highest_group_proj[-1]
	
	highest_quizzes = sorted(graded_avg_and_range[1][3])
	highest_quizzes = highest_quizzes[-1]
	
	highest_labs = sorted(graded_avg_and_range[1][4])
	highest_labs = highest_labs[-1]
	
	highest_indiv_proj = sorted(graded_avg_and_range[1][5])
	highest_indiv_proj = highest_indiv_proj[-1]
	ranges = [lowest_midterm, highest_midterm, lowest_final, highest_final, lowest_group_proj, highest_group_proj, lowest_quizzes, highest_quizzes, lowest_labs, highest_labs, lowest_indiv_proj, highest_indiv_proj]
	return [graded_avg_and_range, ranges] #organizes highest and lowest items and returns it with the two lists returned by calculate_class_avg(roster) for the menu function to use
	
def add_student(roster): #this function adds students to the roster and does the initial calculations, the roster will need to be updated for averages and alphabetical sorting
	user_confirm = "yes"
	while user_confirm in confirm:
		roster.append([{"first":input("First name: "), "last":input("Last name: "), "id":input("Student ID: "), "grades":{"midterm":input("Midterm grade: "),"final":input("Final exam grade: "), "group_project":input("Group project grade: "), "quizzes":list(eval(input("Quiz grades: "))), "labs":list(eval(input("Lab grades: "))), "individual_projects":list(eval(input("Individual project grades: ")))}, "overall_grades":{"course_grade":"","letter_grade":""}, "total_points":{"total_quiz":"", "total_lab":"", "total_indiv_proj":""}}])
		#user will need to manually input every value for the key in the dictionaries
		for student in roster:
			if type(student[0]["grades"]["quizzes"]) != type([]): #this is a bit of a roundabout method to get the new student to match up to all the other students in the roster
				student[0]["grades"]["quizzes"] = [student[0]["grades"]["quizzes"]] #when users did not enter anything for the grades stored as lists, there were errors were the data types did not match up
			while len(roster[0][0]["grades"]["quizzes"]) < 10: #adds a 0 score for every missing item in categories with multiple grades stored
				student[0]["grades"]["quizzes"] = student[0]["grades"]["quizzes"] + [0.0]
			while len(student[0]["grades"]["quizzes"]) < len(roster[0][0]["grades"]["quizzes"]):
				student[0]["grades"]["quizzes"] = student[0]["grades"]["quizzes"] + [0.0]
			if type(student[0]["grades"]["labs"]) != type([]):
				student[0]["grades"]["labs"] = [student[0]["grades"]["labs"]]
			while len(roster[0][0]["grades"]["labs"]) < 10:
				student[0]["grades"]["labs"] = student[0]["grades"]["labs"] + [0.0]
			while len(student[0]["grades"]["labs"]) < len(roster[0][0]["grades"]["labs"]):
				student[0]["grades"]["labs"] = student[0]["grades"]["labs"] + [0.0]
			if type(student[0]["grades"]["individual_projects"]) != type([]):
				student[0]["grades"]["individual_projects"] = [student[0]["grades"]["individual_projects"]]
			while len(roster[0][0]["grades"]["individual_projects"]) < 5:
				student[0]["grades"]["individual_projects"] = student[0]["grades"]["individual_projects"] + [0.0]
			while len(student[0]["grades"]["individual_projects"]) < len(roster[0][0]["grades"]["individual_projects"]):
					student[0]["grades"]["individual_projects"] = student[0]["grades"]["individual_projects"] + [0.0]
		user_confirm = input("\nContinue?: ")

def bin_search(search, search_key, roster): #search is defined in the menu function, search_key sets what the function should search for
	user_confirm = "yes"
	while user_confirm in confirm: #to allow users to search infinite number of times
		if roster == []: 
		#since the function cuts the list index by half every time, at some point the list will become empty if the string user searches for is not in the list. When the list is empty it means student is not in the roster
			print("No matching student has been found.\n")
			user_confirm = input("Would you like to search for another student?:\n")
		else:
			mid = len(roster)//2 #floor division as there will be a approximation for odd numbers divided by 2, list indexes must be integers
			if roster[mid][0][search_key] == search:
					print("\nName: ", roster[mid][0]["last"], ", ", roster[mid][0]["first"], "\nStudent ID: ", roster[mid][0]["id"], "\nScores: ", int(float(roster[mid][0]["grades"]["group_project"])), "% Group Project, ", int(roster[mid][0]["total_points"]["total_indiv_proj"]), "% Individual Project, ", int(roster[mid][0]["total_points"]["total_lab"]), "% Labs, ", int(roster[mid][0]["total_points"]["total_quiz"]), "% Quizzes, ", int(float(roster[mid][0]["grades"]["midterm"])), "% Midterm, ", int(float(roster[mid][0]["grades"]["final"])), "% Final", "\nCourse grade: ", int(roster[mid][0]["overall_grades"]["course_grade"]), "%, ", roster[mid][0]["overall_grades"]["letter_grade"],"\n", sep='')
					break #without a break, the code will print endlessly due to my while loops
			elif roster[mid][0][search_key] > search: #cuts the list in half each time, allowing the code to run in log time
					answer = bin_search(search, search_key, roster[:mid])
					return answer
			elif roster[mid][0][search_key] < search:
					answer = bin_search(search, search_key, roster[mid+1:])
					return answer

def bin_search_for_deletion(search, search_key, roster): #the same as the binary search but very slight modification for front end and convenience
	user_confirm = "yes"
	move_on = False
	while user_confirm in confirm:
		if roster == []:
			print("No matching student has been found.\n")
			#user_confirm = input("Would you like to search for another student?:\n")
			return None
		else:
			mid = len(roster)//2
			if roster[mid][0][search_key] == search:
					print("\nName: ", roster[mid][0]["last"], ", ", roster[mid][0]["first"], "\nStudent ID: ", roster[mid][0]["id"], "\nScores: ", int(float(roster[mid][0]["grades"]["group_project"])), "% Group Project, ", int(roster[mid][0]["total_points"]["total_indiv_proj"]), "% Individual Project, ", int(roster[mid][0]["total_points"]["total_lab"]), "% Labs, ", int(roster[mid][0]["total_points"]["total_quiz"]), "% Quizzes, ", int(float(roster[mid][0]["grades"]["midterm"])), "% Midterm, ", int(float(roster[mid][0]["grades"]["final"])), "% Final", "\nCourse grade: ", int(roster[mid][0]["overall_grades"]["course_grade"]), "%, ", roster[mid][0]["overall_grades"]["letter_grade"],"\n", sep='')
					user_confirm = input("Would you like to remove all records of this student?:\n") #print is slightly different...
					if user_confirm in confirm:
						return roster[mid] #returns the student for deletion from the original roster as deleting it within this function would cause index errors 
					break
			elif roster[mid][0][search_key] > search:
					answer = bin_search_for_deletion(search, search_key, roster[:mid])
					return answer
			elif roster[mid][0][search_key] < search:
					answer = bin_search_for_deletion(search, search_key, roster[mid+1:])
					return answer

def delete_student(search, search_key, roster): #a linear time function that matches the returned student information from the search for deletion function and deletes the student from the roster
	student = bin_search_for_deletion(search, search_key, roster)
	if student == None:
		None
	else:
		roster.remove(student)

def merge_sort(roster, search_key): #sorting function that splits the list by half every time until there is only one in each list and builds the list back up while sorting
	if len(roster) == 1: #if there is only one item in the roster...it's already sorted
		return roster
	else:
		mid = len(roster)//2 #splits the list in half because two small lists are easier to manage than one giant list
		short_roster_1 = roster[:mid]
		short_roster_2 = roster[mid:]
		
		sorted1 = merge_sort(short_roster_1, search_key) #splits the small lists into even smaller lists
		sorted2 = merge_sort(short_roster_2, search_key)
		return merge(sorted1, sorted2, search_key)

def merge(sorted1, sorted2, search_key):
	merged = []
	while len(sorted1) > 0 and len(sorted2) > 0: #as long as there are items in the list
		if sorted1[0][0][search_key] < sorted2[0][0][search_key]: #it puts them back together after comparing which is bigger, the bigger one remains to be compared with the next item that shows up
			merged.append(sorted1[0])
			sorted1.remove(sorted1[0])
		elif sorted1[0][0][search_key] > sorted2[0][0][search_key]:
			merged.append(sorted2[0])
			sorted2.remove(sorted2[0])
		else: #if they are equal in value, put them back together regardless of order
			merged.append(sorted1[0])
			merged.append(sorted2[0])
			sorted1.remove(sorted1[0])
			sorted2.remove(sorted2[0])
	if len(sorted1) > 0:
		sortedlist = merged + sorted1 #returns them after putting it together
		return sortedlist
	else:
		sortedlist = merged + sorted2
		return sortedlist

def access_roster(roster): #a very long menu function that lets users utilize every function in this grade book project.
	user_confirm = "yes"
	menu_interface = eval(input("Please enter the digit corresponding to the action you would like performed:\n(1) Add students to grade book\n(2) Search for students by name or ID\n(3) Delete a student from records\n(4) Display roster in alphabetical order by last names\n(5) Print overall grade averages or grade ranges\n"))
	#a simple text menu screen which lets users access various things by typing in digits
	while user_confirm in confirm:
		if menu_interface == 1: #1 is for adding students
			add_student(roster)
			calculate_individual_grade(roster) #immediately updates the new student with grades
			calculate_class_avg(roster) #as well as the roster
		elif menu_interface == 2: #2 is for searching students
			if len(roster) > 0: #users can only search if there are things to be searched
				sub_menu_3 = eval(input("Please enter the digit corresponding to what you would like to search by:\n(1) Last name\n(2) First name\n(3) ID number\n")) 
				#the new recursive search functions make it a bit more complicated to allow users to be lazy, now users can't search for last, first or id; they must pick one to search by
				while user_confirm in confirm:
					if sub_menu_3 == 1: #1 is for last names
						search_key = "last" #the search_key determines what is to be searched for in the bin_search function
						search = input("\nPlease enter the last name of the student you wish to search for:\n")
					elif sub_menu_3 == 2: #2 is for first names 
						search_key = "first"
						search = input("\nPlease enter the first name of the student you wish to search for:\n")
					elif sub_menu_3 == 3: #3 is for ID numbers
						search_key = "id"
						search = input("\nPlease enter the ID number of the student you wish to search for:\n")
					else:
						print("\nPlease enter an integer from 1 to 3.\n") #please enter in a digit...

					sorted_roster = merge_sort(roster, search_key) #the binary search depends on the list being sorted in the first place
					bin_search(search, search_key, sorted_roster)

					if sub_menu_3 == 1: 
					#if the user wants to search for more students... they can also say no and go back to menu to search by something different (ie, searched for first name, now want to search for last name)
						user_confirm = input("Would you like to search for another student by last name?\n")
					if sub_menu_3 == 2:
						user_confirm = input("Would you like to search for another student by first name?\n")
					if sub_menu_3 == 3:
						user_confirm = input("Would you like to search for another student by ID number?\n")
			else:
				print("There are no students in the grade book.\n") #if there are none, there are none and searching for a student would be pointless
		elif menu_interface == 3: #this is for deleting a student, very similar to the search except with the added delete student function
			if len(roster) > 0:
				sub_menu_4 = eval(input("Please enter the digit corresponding to what you would like to search by:\n(1) Last name\n(2) First name\n(3) ID number\n"))
				if sub_menu_4 == 1:
					search_key = "last"
					search = input("\nPlease enter the last name of the student you wish to search for:\n")
				elif sub_menu_4 == 2:
					search_key = "first"
					search = input("\nPlease enter the first name of the student you wish to search for:\n")
				elif sub_menu_4 == 3:
					search_key = "id"
					search = input("\nPlease enter the ID number of the student you wish to search for:\n")
				else:
					None
				sorted_roster = merge_sort(roster, search_key)
				delete_student(search, search_key, roster)
			else:
				print("There are no students in the grade book.\n")
		elif menu_interface == 4: #this sorts the newest roster by last names and then prints them out in a nice format
			if len(roster) > 0:
				search_key = "last"
				sorted_roster = merge_sort(roster, search_key)
			else:
				print("There are no students in the grade book.\n") #as long as there are students in the roster...
			for student in sorted_roster:
				print("\nName: ", student[0]["last"], ", ", student[0]["first"], sep = '')
				print("Student ID: ", student[0]["id"], sep = '')
				print("Scores: ", int(float(student[0]["grades"]["group_project"])), "% Group Project, ", int(student[0]["total_points"]["total_indiv_proj"]), "% Individual Project, ", int(student[0]["total_points"]["total_lab"]), "% Labs, ", int(student[0]["total_points"]["total_quiz"]), "% Quizzes, ", int(float(student[0]["grades"]["midterm"])), "% Midterm, ", int(float(student[0]["grades"]["final"])), "% Final", sep = '')
				print("Course grade: ", int(student[0]["overall_grades"]["course_grade"]), "%, ", student[0]["overall_grades"]["letter_grade"],"\n", sep='')
		elif menu_interface == 5: #for all sorts of averages
			if len(roster) > 0:
				graded_avg_and_range = class_range(roster)
				sub_menu_0 = eval(input("Please enter the digit corresponding to the sub menu you wish you access:\n(1) Grade Averages\n(2) Grade Ranges\n")) #more menus for more averages
				while user_confirm in confirm:
					if sub_menu_0 == 1:
						sub_menu_1 = eval(input("Please enter the digit corresponding to the average you would like to view:\n(1) Group Projects\n(2) Individual Projects\n(3) Labs\n(4) Quizzes\n(5) Midterm Exam\n(6) Final Exam\n(7) Overall Course Grade\n"))
						#one more menu for more specific averages
						if sub_menu_1 == 1: #lots of printing functions for whatever the user wants
							print("The average score for the group project is: ", int(graded_avg_and_range[0][0][2]), "%", sep = '')
						elif sub_menu_1 == 2:
							print("The average score for the individual projects is: ", int(graded_avg_and_range[0][0][5]), "%", sep = '')
						elif sub_menu_1 == 3:
							print("The average score for the labs is: ", int(graded_avg_and_range[0][0][4]), "%", sep = '')
						elif sub_menu_1 == 4:
							print("The average score for the quizzes is: ", int(graded_avg_and_range[0][0][3]), "%", sep = '')
						elif sub_menu_1 == 5:
							print("\nThe average score for the midterm exam is: ", int(graded_avg_and_range[0][0][0]), "%", sep = '')
						elif sub_menu_1 == 6:
							print("The average score for the final exam is: ", int(graded_avg_and_range[0][0][1]), "%", sep = '')
						elif sub_menu_1 == 7:
							print("The average grade overall in the class is: ", int(graded_avg_and_range[0][0][6]), "%", sep = '')
						else:
							print("Please enter an integer from 1 to 7")
					elif sub_menu_0 == 2:
						sub_menu_2 = eval(input("Please enter the digit corresponding to the grade range you would like to view:\n(1) Group Projects\n(2) Individual Projects\n(3) Labs\n(4) Quizzes\n(5) Midterm Exam\n(6) Final Exam\n"))
						#the last sub menu, this time for ranges
						if sub_menu_2 == 1: #lots of printing functions for ranges
							print("The lowest recorded score for the group project is: ", int(graded_avg_and_range[1][4]), "%", sep = '')
							print("The highest recorded score for the group project is: ", int(graded_avg_and_range[1][5]), "%\n", sep = '')
						elif sub_menu_2 == 2:
							print("The lowest recorded score for the individual projects is: ", int(graded_avg_and_range[1][10]), "%", sep = '')
							print("The highest recorded score for the individual projects is: ", int(graded_avg_and_range[1][11]), "%\n", sep = '')
						elif sub_menu_2 == 3:
							print("The lowest recorded score for the labs is: ", int(graded_avg_and_range[1][8]), "%", sep = '')
							print("The highest recorded score for the labs is: ", int(graded_avg_and_range[1][9]), "%\n", sep = '')
						elif sub_menu_2 == 4:
							print("The lowest recorded score for the quizzes is: ", int(graded_avg_and_range[1][6]), "%", sep = '')
							print("The highest recorded score for the quizzes is: ", int(graded_avg_and_range[1][7]), "%\n", sep = '')
						elif sub_menu_2 == 5:
							print("The lowest recorded score for the midterm exam is: ", int(graded_avg_and_range[1][0]), "%", sep = '')
							print("The highest recorded score for the midterm exam is: ", int(graded_avg_and_range[1][1]), "%\n", sep = '')
						elif sub_menu_2 == 6:
							print("The lowest recorded score for the final exam is: ", int(graded_avg_and_range[1][2]), "%", sep = '')
							print("The highest recorded score for the final exam is: ", int(graded_avg_and_range[1][3]), "%\n", sep = '')
						else:
							print("Please enter an integer from 1 to 6")
					else:
						print("\nEnter either a '1' or a '2' (without the quotation marks).\n") #of course user needs to enter digits for these to work
					if sub_menu_0 == 1: #users can look for other averages
						user_confirm = input("Would you like to view another average?\n")
					elif sub_menu_0 == 2: #and other ranges
						user_confirm = input("Would you like to view the range of another category?\n")
					else:
						break #to end the loop if user types in something else
			else:
				print("There are no students in the grade book.\n") #there needs to be students for it to be a roster
		else:
			print("That feature is not implemented yet.") #if the user accidentally (or purposefully...) types in something that's not a digit or within the range set by the menu directions
		user_confirm = input("\nWould you like to return to the main menu?: \n") #go back to the menu to do more fun things
		if user_confirm in confirm:
			menu_interface = eval(input("Please enter the digit corresponding to the action you would like performed:\n(1) Add students to grade book\n(2) Search for students by name or ID\n(3) Delete a student from records\n(4) Display roster in alphabetical order by last names\n(5) Print overall grade averages or grade ranges\n"))
			#what else would you like to do?
			
def main():
	roster = gradebook("gradebooktest.txt")
	access_roster(roster)
main()