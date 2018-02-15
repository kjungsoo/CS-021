#Jung Kim
#CS-21
#Project 3 - Full-featured grade book

confirm = ["yes", "yeah", "y", "yea", "Yes", "Yeah", "Y", "Yea", "1", "YES"] #global confirm variable
def gradebook(textfile):
	roster = []
	roster_data = []
	gradebook_text = textfile
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
	for student in roster_data:
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
	for student in roster:
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

def calculate_individual_grade(roster):
	for student in roster:

		sorted_quiz_sum = sorted(student[0]["grades"]["quizzes"])
		quiz_sum = (int(sum(sorted_quiz_sum)) - int(sorted_quiz_sum[0]) - int(sorted_quiz_sum[1]))/(len(student[0]["grades"]["quizzes"]) - 2)
		student[0]["total_points"]["total_quiz"] = quiz_sum

		sorted_lab_sum = sorted(student[0]["grades"]["labs"])
		lab_sum = (int(sum(sorted_lab_sum)) - int(sorted_lab_sum[0]) - int(sorted_lab_sum[1]))/(len(student[0]["grades"]["labs"]) - 2)
		student[0]["total_points"]["total_lab"] = lab_sum

		sorted_proj_sum = sorted(student[0]["grades"]["individual_projects"])
		indiv_proj_sum = (int(sum(sorted_proj_sum)) - int(sorted_proj_sum[0]))/(len(student[0]["grades"]["individual_projects"]) - 1)
		student[0]["total_points"]["total_indiv_proj"] = indiv_proj_sum

		student[0]["overall_grades"]["course_grade"] = int((float(student[0]["grades"]["midterm"]) * 1.5 + float(student[0]["grades"]["final"]) * 1.5 + float(student[0]["grades"]["group_project"]) + quiz_sum + lab_sum + indiv_proj_sum * (len(student[0]["grades"]["individual_projects"]) - 1)) / 10) #len(roster[0][0]['grades']
		grade = student[0]["overall_grades"]["course_grade"]
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
														
def calculate_class_avg(roster):
	class_midterm = []
	class_final = []
	class_group_proj = []
	class_quizzes = []
	class_labs = []
	class_indiv_proj = []
	
	for student in roster:
		class_midterm = class_midterm + [int(float(student[0]["grades"]["midterm"]))]
		class_final = class_final + [int(float(student[0]["grades"]["final"]))]
		class_group_proj = class_group_proj + [int(float(student[0]["grades"]["group_project"]))]
		for items in range(0,len(student[0]["grades"]["quizzes"])):
			class_quizzes = class_quizzes + [int(float(student[0]["grades"]["quizzes"][items]))]
		for items in range(0,len(student[0]["grades"]["labs"])):
			class_labs = class_labs + [int(float(student[0]["grades"]["labs"][items]))]
		for items in range(0,len(student[0]["grades"]["individual_projects"])):
			class_indiv_proj = class_indiv_proj + [int(float(student[0]["grades"]["individual_projects"][items]))]
			
	class_midterm_average = sum(class_midterm) / len(class_midterm)
	class_final_average = sum(class_final) / len(class_final)
	class_group_proj_average = sum(class_group_proj)/len(class_group_proj)
	class_quizzes_average = sum(class_quizzes)/len(class_quizzes)
	class_labs_average = sum(class_labs)/len(class_labs)
	class_indiv_proj_average = sum(class_indiv_proj)/len(class_indiv_proj)
	overall_course_grade = (class_midterm_average + class_final_average + class_group_proj_average + class_quizzes_average + class_labs_average + class_indiv_proj_average) / 6
	
	graded_averages = [class_midterm_average, class_final_average, class_group_proj_average, class_quizzes_average, class_labs_average, class_indiv_proj_average, overall_course_grade]
	graded_ranges = [class_midterm, class_final, class_group_proj, class_quizzes, class_labs, class_indiv_proj]
	return [graded_averages, graded_ranges]
	
def class_range(roster):
	graded_avg_and_range = calculate_class_avg(roster)
	lowest_midterm = sorted(graded_avg_and_range[1][0])
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
	
	highest_midterm = sorted(graded_avg_and_range[1][0])
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
	return [graded_avg_and_range, ranges]
	
def add_student(roster):
	user_confirm = "yes"
	while user_confirm in confirm:
		roster.append([{"first":input("First name: "), "last":input("Last name: "), "id":input("Student ID: "), "grades":{"midterm":input("Midterm grade: "),"final":input("Final exam grade: "), "group_project":input("Group project grade: "), "quizzes":list(eval(input("Quiz grades: "))), "labs":list(eval(input("Lab grades: "))), "individual_projects":list(eval(input("Individual project grades: ")))}, "overall_grades":{"course_grade":"","letter_grade":""}, "total_points":{"total_quiz":"", "total_lab":"", "total_indiv_proj":""}}])
		for student in roster:
			if type(student[0]["grades"]["quizzes"]) != type([]):
				student[0]["grades"]["quizzes"] = [student[0]["grades"]["quizzes"]]
			while len(roster[0][0]["grades"]["quizzes"]) < 10:
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

def del_student(roster):
	user_confirm = "yes"
	move_on = False
	while user_confirm in confirm:
		search = input("\nPlease enter the first or last name of the student or the student's ID you wish to remove from records:\n")
		for deletion_index in range(0,len(roster)):
			if (search.lower() == roster[deletion_index][0]["first"].lower()
				or search.lower() == roster[deletion_index][0]["last"].lower()				
				or search == roster[deletion_index][0]["id"]):
					print("\nName: ", roster[deletion_index][0]["last"], ", ", roster[deletion_index][0]["first"], "\nStudent ID: ", roster[deletion_index][0]["id"], "\nScores: ", int(float(roster[deletion_index][0]["grades"]["group_project"])), "% Group Project, ", int(roster[deletion_index][0]["total_points"]["total_indiv_proj"]), "% Individual Project, ", int(roster[deletion_index][0]["total_points"]["total_lab"]), "% Labs, ", int(roster[deletion_index][0]["total_points"]["total_quiz"]), "% Quizzes, ", int(float(roster[deletion_index][0]["grades"]["midterm"])), "% Midterm, ", int(float(roster[deletion_index][0]["grades"]["final"])), "% Final", "\nCourse grade: ", int(roster[deletion_index][0]["overall_grades"]["course_grade"]), "%, ", roster[deletion_index][0]["overall_grades"]["letter_grade"],"\n", sep='')
					user_confirm = input("Would you like to remove all records of this student?:\n")
					if user_confirm in confirm:
						del roster[deletion_index]
					user_confirm = input("Would you like to search for another student?:\n")
					move_on = True
					break
			else:
				move_on = False
		if move_on == False:
			print("No matching student has been found.\n")
			user_confirm = input("Would you like to search for another student?:\n")

def search(roster):
	user_confirm = "yes"
	move_on = False
	while user_confirm in confirm:
		search = input("\nPlease enter the first or last name of the student or the student's ID you wish to search:\n")
		for student in roster:
			if (search.lower() == student[0]["first"].lower()
				or search.lower() == student[0]["last"].lower() 
				or search == student[0]["id"]):
					print("\nName: ", student[0]["last"], ", ", student[0]["first"], "\nStudent ID: ", student[0]["id"], "\nScores: ", int(float(student[0]["grades"]["group_project"])), "% Group Project, ", int(student[0]["total_points"]["total_indiv_proj"]), "% Individual Project, ", int(student[0]["total_points"]["total_lab"]), "% Labs, ", int(student[0]["total_points"]["total_quiz"]), "% Quizzes, ", int(float(student[0]["grades"]["midterm"])), "% Midterm, ", int(float(student[0]["grades"]["final"])), "% Final", "\nCourse grade: ", int(student[0]["overall_grades"]["course_grade"]), "%, ", student[0]["overall_grades"]["letter_grade"],"\n", sep='')
					user_confirm = input("Would you like to search for another student?:\n")
					move_on = True
					break
			else:
				move_on = False
		if move_on == False:
			print("No matching student has been found.\n")
			user_confirm = input("Would you like to search for another student?:\n")

def sort_roster(roster):
	sorted_roster = []
	sub_list = roster[0:]
	for substring in range (0,len(roster)):
		smallest = sub_list[0][0]['last'][0]
		smallest_index = 0
		for letter in range (1,len(sub_list)):
			if (smallest.lower() > sub_list[letter][0]['last'][0].lower()):
				smallest = sub_list[letter][0]['last'][0]
				smallest_index = letter
		sorted_roster.append(sub_list[smallest_index])
		sub_list = sub_list[0:smallest_index] + sub_list[smallest_index+1:]
	return sorted_roster

def access_roster(roster):
	user_confirm = "yes"
	menu_interface = input("Please enter the digit corresponding to the action you would like performed:\n(1) Add students to grade book\n(2) Search for students by name or ID\n(3) Delete a student from records\n(4) Display roster in alphabetical order by last names\n(5) Print overall grade averages or grade ranges\n")
	while user_confirm in confirm:
		if int(menu_interface) == 1:
			add_student(roster)
			calculate_individual_grade(roster)
			calculate_class_avg(roster)
		elif int(menu_interface) == 2:
			if len(roster) > 0:
				search(roster)
			else:
				print("There are no students in the grade book.\n")
		elif int(menu_interface) == 3:
			if len(roster) > 0:
				del_student(roster)
			else:
				print("There are no students in the grade book.\n")
		elif int(menu_interface) == 4:
			if len(roster) > 0:
				sorted_roster = sort_roster(roster)
			else:
				print("There are no students in the grade book.\n")
			for student in sorted_roster:
				print("\nName: ", student[0]["last"], ", ", student[0]["first"], sep = '')
				print("Student ID: ", student[0]["id"], sep = '')
				print("Scores: ", int(float(student[0]["grades"]["group_project"])), "% Group Project, ", int(student[0]["total_points"]["total_indiv_proj"]), "% Individual Project, ", int(student[0]["total_points"]["total_lab"]), "% Labs, ", int(student[0]["total_points"]["total_quiz"]), "% Quizzes, ", int(float(student[0]["grades"]["midterm"])), "% Midterm, ", int(float(student[0]["grades"]["final"])), "% Final", sep = '')
				print("Course grade: ", int(student[0]["overall_grades"]["course_grade"]), "%, ", student[0]["overall_grades"]["letter_grade"],"\n", sep='')
		elif int(menu_interface) == 5:
			if len(roster) > 0:
				graded_avg_and_range = class_range(roster)
				sub_menu_0 = input("Please enter the digit corresponding to the sub menu you wish you access:\n(1) Grade Averages\n(2) Grade Ranges\n")
				while user_confirm in confirm:
					if int(sub_menu_0) == 1:
						sub_menu_1 = input("Please enter the digit corresponding to the average you would like to view:\n(1) Group Projects\n(2) Individual Projects\n(3) Labs\n(4) Quizzes\n(5) Midterm Exam\n(6) Final Exam\n(7) Overall Course Grade\n")
						if int(sub_menu_1) == 1:
							print("The average score for the group project is: ", int(graded_avg_and_range[0][0][2]), "%", sep = '')
						elif int(sub_menu_1) == 2:
							print("The average score for the individual projects is: ", int(graded_avg_and_range[0][0][5]), "%", sep = '')
						elif int(sub_menu_1) == 3:
							print("The average score for the labs is: ", int(graded_avg_and_range[0][0][4]), "%", sep = '')
						elif int(sub_menu_1) == 4:
							print("The average score for the quizzes is: ", int(graded_avg_and_range[0][0][3]), "%", sep = '')
						elif int(sub_menu_1) == 5:
							print("\nThe average score for the midterm exam is: ", int(graded_avg_and_range[0][0][0]), "%", sep = '')
						elif int(sub_menu_1) == 6:
							print("The average score for the final exam is: ", int(graded_avg_and_range[0][0][1]), "%", sep = '')
						elif int(sub_menu_1) == 7:
							print("The average grade overall in the class is: ", int(graded_avg_and_range[0][0][6]), "%", sep = '')
					elif int(sub_menu_0) == 2:
						sub_menu_2 = input("Please enter the digit corresponding to the grade range you would like to view:\n(1) Group Projects\n(2) Individual Projects\n(3) Labs\n(4) Quizzes\n(5) Midterm Exam\n(6) Final Exam\n")
						if int(sub_menu_2) == 1:
							print("The lowest recorded score for the group project is: ", int(graded_avg_and_range[1][4]), "%", sep = '')
							print("The highest recorded score for the group project is: ", int(graded_avg_and_range[1][5]), "%\n", sep = '')
						elif int(sub_menu_2) == 2:
							print("The lowest recorded score for the individual projects is: ", int(graded_avg_and_range[1][10]), "%", sep = '')
							print("The highest recorded score for the individual projects is: ", int(graded_avg_and_range[1][11]), "%\n", sep = '')
						elif int(sub_menu_2) == 3:
							print("The lowest recorded score for the labs is: ", int(graded_avg_and_range[1][8]), "%", sep = '')
							print("The highest recorded score for the labs is: ", int(graded_avg_and_range[1][9]), "%\n", sep = '')
						elif int(sub_menu_2) == 4:
							print("The lowest recorded score for the quizzes is: ", int(graded_avg_and_range[1][6]), "%", sep = '')
							print("The highest recorded score for the quizzes is: ", int(graded_avg_and_range[1][7]), "%\n", sep = '')
						elif int(sub_menu_2) == 5:
							print("The lowest recorded score for the midterm exam is: ", int(graded_avg_and_range[1][0]), "%", sep = '')
							print("The highest recorded score for the midterm exam is: ", int(graded_avg_and_range[1][1]), "%\n", sep = '')
						elif int(sub_menu_2) == 6:
							print("The lowest recorded score for the final exam is: ", int(graded_avg_and_range[1][2]), "%", sep = '')
							print("The highest recorded score for the final exam is: ", int(graded_avg_and_range[1][3]), "%\n", sep = '')
					else:
						print("\nEnter either a '1' or a '2' (without the quotation marks).\n")
					if int(sub_menu_0) == 1:
						user_confirm = input("Would you like to view another average?\n")
					elif int(sub_menu_0) == 2:
						user_confirm = input("Would you like to view the range of another category?\n")
					else:
						break
			else:
				print("There are no students in the grade book.\n")
		else:
			print("That feature is not implemented yet.")
		user_confirm = input("\nWould you like to return to the main menu?: \n")
		if user_confirm in confirm:
			menu_interface = input("Please enter the digit corresponding to the action you would like performed:\n(1) Add students to grade book\n(2) Search for students by name or ID\n(3) Delete a student from records\n(4) Display roster in alphabetical order by last names\n(5) Print overall grade averages or grade ranges\n")