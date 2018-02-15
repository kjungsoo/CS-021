#Jung Kim
#CS-21
#Project #2 - Basic grade book

def gradebook(): #creates the grade book as an empty list
	roster = []
	return roster

def add_student(roster): #a function to add students to the roster created in gradebook()
	user_confirm, confirm = confirming() #local confirm feature to increase efficiency
	while user_confirm in confirm: #a loop that allows user to input any number of students into the grade book
		roster.append({"first":input("First name: "), "last":input("Last name: "), "id":input("Student ID: "), "test_grades":{"midterm":input("Midterm grade: "),"final":input("Final exam grade: ")}, "overall_grades":{"course_grade":"","letter_grade":""}})
		user_confirm = input("\nContinue?: ") #conditional to either stop or continue loop

def calculate_individual_grade(roster): #calculates students' grade in the class based on the two exams, grading scale taken from class syllabus
	for student in roster: #a loop that goes through all the students in roster
		student["overall_grades"]["course_grade"] = (int(student["test_grades"]["midterm"]) + int(student["test_grades"]["final"])) / len(student["test_grades"]) #calculates the course grade
		if student["overall_grades"]["course_grade"] >= 0: #used a nested conditional to give a letter representation of student's grade
			student["overall_grades"]["letter_grade"] = "F"
			if student["overall_grades"]["course_grade"] >= 60:
				student["overall_grades"][" letter_grade"] = "D-"
				if student["overall_grades"]["course_grade"] >= 64:
					student["overall_grades"]["letter_grade"] = "D"
					if student["overall_grades"]["course_grade"] >= 67:
						student["overall_grades"]["letter_grade"] = "D+"
						if student["overall_grades"]["course_grade"] >= 70:
							student["overall_grades"]["letter_grade"] = "C-"
							if student["overall_grades"]["course_grade"] >= 74:
								student["overall_grades"]["letter_grade"] = "C"
								if student["overall_grades"]["course_grade"] >= 77:
									student["overall_grades"]["letter_grade"] = "C+"
									if student["overall_grades"]["course_grade"] >= 80:
										student["overall_grades"]["letter_grade"] = "B-"
										if student["overall_grades"]["course_grade"] >= 84:
											student["overall_grades"]["letter_grade"] = "B"
											if student["overall_grades"]["course_grade"] >= 87:
												student["overall_grades"]["letter_grade"] = "B+"
												if student["overall_grades"]["course_grade"] >= 90:
													student["overall_grades"]["letter_grade"] = "A-"
													if student["overall_grades"]["course_grade"] >= 94:
														student["overall_grades"]["letter_grade"] = "A"
														
def calculate_class_avg(roster): #calculated the class average of each test and then calculated overall class grade
	class_midterm = [] #puts all the midterm scores in roster into a new list to allow easier calculation
	class_final = [] #same as above
	for student in roster: #loop to put every midterm and final score into the lists above
		class_midterm = class_midterm + [int(student["test_grades"]["midterm"])]
		class_final = class_final + [int(student["test_grades"]["final"])]
	class_midterm_average = sum(class_midterm) / len(class_midterm) #calculates the midterm by taking the sum of the list and dividing by the number of items in the list
	class_final_average = sum(class_final) / len(class_final) #same as above
	overall_course_grade = (class_midterm_average + class_final_average) / 2 #takes the average of midterm and final average for course average
	return (class_midterm_average, class_final_average, overall_course_grade) #returns the value to print later

def search(roster): #a search function that allows users to search by first name, last name or id number
	user_confirm, confirm = confirming()
	move_on = False #set conditional to False to allow loop to work as long as user wants to continue searching
	while user_confirm in confirm:
		search = input("\nPlease enter the first or last name of the student or the student's ID you wish to search:\n") #enter only the last name, first name or the id; the function to parse inputs has not yet been implemented
		for student in roster:
			if (search.lower() == student["first"].lower() #if user inputs matches a first name, last name or id anywhere in the roster, it will print the searched student's information
				or search.lower() == student["last"].lower() 
				or search == student["id"]):
					print("\nName: ", student["last"], ", ", student["first"], "\nStudent ID: ", student["id"], "\nScores: ", student["test_grades"]["midterm"], "% Midterm, ", student["test_grades"]["final"], "% Final", "\nCourse grade: ", int(student["overall_grades"]["course_grade"]), "%, ", student["overall_grades"]["letter_grade"],"\n", sep='')
					user_confirm = input("Would you like to search for another student?:\n")
					move_on = True
					break
			else: #if no one was found using the above method, the code will move on to the next conditional
				move_on = False
		if move_on == False: #if no one was found, the code will print necessary information and allow user to search again
			print("No matching student has been found.\n")
			user_confirm = input("Would you like to search for another student?:\n")
	
def confirming(): #a confirm function used throughout the code to increase efficiency
	user_confirm = "yes"
	confirm = ["yes"]
	return(user_confirm, confirm)

def access_roster(roster): #a menu function (idea credited to Eric Liu, code was done individually) to allow users to add, search and print test averages
	user_confirm, confirm = confirming()
	menu_interface = input("Please enter the digit corresponding to the action you would like performed:\n(1) Add students to grade book\n(2) Search for students by name or ID\n(3) Print overall test averages\n") #a menu interface using number values
	while user_confirm in confirm:
		if int(menu_interface) == 1: #1 allows users to add students and automatically calculates the grades for each student and all the averages of all the students added thus far; if new students are added, new calculations are made and immediately updated
			add_student(roster)
			calculate_individual_grade(roster)
			calculate_class_avg(roster)
		elif int(menu_interface) == 2: #2 allows users to search for any student so long as there is at least 1 entry in the roster
			if len(roster) > 0:
				search(roster)
			else:
				print("There are no students in the grade book.\n") #if there are no entries in the roster, the code will send user back to the main menu
		elif int(menu_interface) == 3: #3 allows users to print the midterm avg, final avg and course avg of the whole class so long as there is at least 1 entry in the roster
			if len(roster) > 0:
				class_midterm_average, class_final_average, overall_class_grade = calculate_class_avg(roster)
				print("\nThe average score for the midterm exam is: ", int(class_midterm_average), "%", sep = '')
				print("The average score for the final exam is: ", int(class_final_average), "%", sep = '')
				print("The average grade overall in the class is: ", int(overall_class_grade), "%", sep = '')
			else:
				print("There are no students in the grade book.\n")
		else:
			print("That feature is not implemented yet.") #if user input is anything other than 1,2 or 3, user will be returned to main menu
		user_confirm = input("\nWould you like to return to the main menu?: \n")
		if user_confirm in confirm:
			menu_interface = input("Please enter the digit corresponding to the action you would like performed:\n(1) Add students to grade book\n(2) Search for students by name or ID\n(3) Print overall test averages\n")

def main():
	roster = gradebook()
	access_roster(roster)
main()