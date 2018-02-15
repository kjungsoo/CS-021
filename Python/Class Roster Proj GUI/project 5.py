#Jung Kim
#CS-21 Project 5 - Object-Oriented Programming

from tkinter import*

class Roster(object):
	def __init__(self):
		self.roster = []
		self.sorted_roster = []
		
	def add_students_txt(self, textfile):
		roster_data = []
		read_student_info = open(textfile, "r")
		
		for line in read_student_info:
			roster_data.append(line.replace('%', '.0').strip('\n').split('; ')) #just parsing strings from a text
		
		for student in roster_data:
			for n in range(0, len(student)): #and putting each of the students in that text in a list for more parsing stuff
				student[n] = student[n].split(', ')
			
			student[2][0] = student[2][0].strip("Midterm ") #probably could've done this before splitting up the students but...I did it this way
			student[3][0] = student[3][0].strip("Final ")
			student[4][0] = student[4][0].strip("Group project ")
			student[5][0] = student[5][0].strip("Quizzes ")
			student[6][0] = student[6][0].strip("Labs ")
			student[7][0] = student[7][0].strip("Individual projects ")
			
			for quiz in range(0, len(student[5])): #making sure that the numbers are floats and not strings
				student[5][quiz] = float(student[5][quiz])
			
			for labs in range(0, len(student[6])):
				student[6][labs] = float(student[6][labs])
			
			for indiv_proj in range(0, len(student[7])):
				student[7][indiv_proj] = float(student[7][indiv_proj])
			
			new_student = Student() #I was having trouble with appending new objects and running functions on that (probably just minor syntax errors) so I did it this way
			self.roster.append(new_student)
			
			new_student.fname = student[0][0] #since student information is already on the text document, no need to re-input them
			new_student.lname = student[0][1]
			new_student.id = student[1][0]
			new_student.midterm = student[2][0]
			new_student.final = student[3][0]
			new_student.group_project = student[4][0]
			new_student.quizzes = student[5]
			new_student.labs = student[6]
			new_student.individual_projects = student[7]
			new_student.search_for = [new_student.fname, 
												   new_student.lname, 
												   new_student.id]
			new_student.calc_course_grade() #and finishing up their information by calculating stuff
		
		read_student_info.close()
		
	def add_students(self):
		if len(self.roster) == 0:
			student = "Student1" #pretty unnecessary stuff here but I decided to do it this way because it was easier

		else:
			student = "Student" + str(len(self.roster))
		self.roster.append(student)
		self.roster[len(self.roster) - 1] = Student()
		self.roster[len(self.roster) - 1].student_info()
		self.roster[len(self.roster) - 1].calc_course_grade()
	
	def search_Roster(self): #because binary search searches for a specific thing that it needs to be sorted by I needed to do this to allow users to search up for first, last or id
		search_query = eval(input("What would you like to search by?\n(1)First name, (2)Last name, (3)Student ID\n"))
		search_target = input("Please enter their first or last name or student ID number: ")
		
		while type(search_query) != type(0):
			print("re enter")
			search_query = eval(input("What would you like to search by?\n(1)First name, (2)Last name, (3)Student ID\n"))
		
		if search_query == 1:
			search_by = 0
			self.sorted_Roster = merge_sort(self.roster, search_by) #sorting but the query before searching for them
			bin_search(self.sorted_Roster, search_target, search_by)
			
		elif search_query == 2:
			search_by = 1
			self.sorted_Roster = merge_sort(self.roster, search_by)
			bin_search(self.sorted_Roster, search_target, search_by)
			
		elif search_query == 3:
			search_by = 2
			self.sorted_Roster = merge_sort(self.roster, search_by)
			bin_search(self.sorted_Roster, search_target, search_by)
	
	def sort_Roster(self): #this calls the sort function from project 4
		self.sorted_roster = merge_sort(self.roster, 1)

	def print_Roster(self): #printing stuff for users to see
		for student in self.sorted_roster:
			print("\nName: ", student.lname, ", ", student.fname, sep = '')
			print("Student ID: ", student.id, sep = '')
			print("Scores: ", int(float(student.group_project)), "% Group Project, ", 
				  int(student.total_indiv_proj), "% Individual Project, ", 
				  int(student.total_lab), "% Labs, ", 
				  int(student.total_quiz), "% Quizzes, ", 
				  int(float(student.midterm)), "% Midterm, ", 
				  int(float(student.final)), "% Final", sep = '')
			print("Course grade: ", int(student.course_grade), "%, ", 
				  student.letter_grade,"\n", sep='')

class Student(object): #student class to make students for the roster
	def __init__(self):
		self.fname = "" #first name
		self.lname = "" #last name
		self.id = "" #ID number
		self.labs = [] #there should be a total of 10
		self.quizzes = [] #total 10
		self.individual_projects = [] #total 5
		self.group_project = 0
		self.midterm = 0
		self.final = 0
		self.total_quiz = 0
		self.total_lab = 0
		self.total_indiv_proj = 0
		self.course_grade = 0
		self.letter_grade = ""
		self.search_for = [] #this is the workaround for binary search
		
	def student_info(self):
		self.fname = input("First name: ")
		self.lname = input("Last name: ")
		self.id = input("Student ID: ")
		self.labs = eval(input("Lab grades: "))
		self.quizzes = eval(input("Quiz grades: "))
		self.individual_projects = eval(input("Individual project grades: "))
		self.group_project = input("Group project grade: ")
		self.midterm = input("Midterm grade: ")
		self.final = input("Final exam grade: ")
		self.search_for = [self.fname, self.lname, self.id]
		
		if type(self.quizzes) == type(0): #making sure that quizzes, labs and individual projects are stored in a list
			self.quizzes = [self.quizzes]
		else:
			self.quizzes = list(self.quizzes)
		while len(self.quizzes) < 10:
			self.quizzes = self.quizzes + [0.0]

		if type(self.labs) == type(0):
			self.labs = [self.labs]
		else:
			self.labs = list(self.labs)
		while len(self.labs) < 10:
			self.labs = self.labs + [0.0]

		if type(self.individual_projects) == type(0):
			self.individual_projects = [self.individual_projects]
		else:
			self.individual_projects = list(self.individual_projects)
		while len(self.individual_projects) < 5:
			self.individual_projects = self.individual_projects + [0.0]
	
	def calc_course_grade(self): #calculations for student grades
		sorted_quiz_sum = sorted(self.quizzes)
		quiz_sum = (int(sum(sorted_quiz_sum)) - int(sorted_quiz_sum[0]) - 
						int(sorted_quiz_sum[1]))/(len(self.quizzes) - 2)
		self.total_quiz = quiz_sum
		
		sorted_lab_sum = sorted(self.labs)
		lab_sum = (int(sum(sorted_lab_sum)) - int(sorted_lab_sum[0]) - 
					   int(sorted_lab_sum[1]))/(len(self.labs) - 2)
		self.total_lab = lab_sum
		
		sorted_proj_sum = sorted(self.individual_projects)
		indiv_proj_sum = (int(sum(sorted_proj_sum)) - 
							  int(sorted_proj_sum[0]))/(len(self.individual_projects) - 1)
		self.total_indiv_proj = indiv_proj_sum
		
		self.course_grade = int((float(self.midterm) * 1.5 + float(self.final) * 1.5 + 
								 float(self.group_project) + quiz_sum + lab_sum + 
								 indiv_proj_sum * (len(self.individual_projects) - 1)) / 10)
		grade = self.course_grade
		if grade >= 94: #normal grading scale
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
		self.letter_grade = letter
		
	def print_student_info(self): #printing stuff
		print("\nName: ", self.lname, ",", self.fname, sep = "")
		print("Student ID: ", self.id, sep = "")
		print("Scores: ", int(float(self.group_project)), "% Group Project, ", 
			  int(self.total_indiv_proj), "% Individual Project, ", 
			  int(self.total_lab), "% Labs, ", int(self.total_quiz), "% Quizzes, ", 
			  int(float(self.midterm)), "% Midterm, ", int(float(self.final)), "% Final", sep = '')
		print("Course grade: ", self.course_grade, "%, ", self.letter_grade, sep = "")
		
class Menu(object): #implemented a GUI with tkinter for fun, hopefully everything works the way it did for me. Enjoy :)

	def __init__(self, Roster):
		root = Tk() #window, if I understand correctly, root = Tk() is the equivalent to def main() but for windows
		root.wm_title("CS-21 Gradebook") #the title of the window I made is CS-21 Gradebook
		root.config(background = "#FFFFFF") #white background
		
		Rosterframe = Frame(root, width = 100, height = 300,) 
		#creating a frame and some scaling to the window (not sure if it did anything because I think it rescaled with the buttons)
		Rosterframe.grid(row = 0, column = 0, padx = 1, pady = 1)
		#placing the frame on the window
		
		Frame1 = Frame(Rosterframe) #this frame is for buttons
		Frame1.grid(row = 1, column = 0, padx = 1, pady = 1)
		
		Frame2 = Frame(Rosterframe) #this frame is for labels for description of the buttons
		Frame2.grid(row = 1, column = 1, padx = 1, pady = 1)
		
		self.RosterButton_1 = Button(Frame1, text = "Option 1", command = self.menu_option_1)
		self.RosterButton_1.grid(row = 0, column = 0, padx = 1, pady = 3)
		#the first button, when user clicks it allows user to add students to the roster
		
		self.RosterButton_2 = Button(Frame1, text = "Option 2", command = self.menu_option_2)
		self.RosterButton_2.grid(row = 1, column = 0, padx = 1, pady = 3)
		#button for searching students in the roster
		
		RosterButton_4 = Button(Frame1, text = "Option 3", command = self.menu_option_3)
		RosterButton_4.grid(row = 2, column = 0, padx = 1, pady = 3)
		#button for sorting and printing stuff
		
		RosterButton_1_label = Label(Frame2, text = 
									 "Add students to the roster.                                                        ", bg = "white", bd = 3)
		RosterButton_1_label.grid(row = 0, column = 0, padx = 1, pady = 5)
		
		RosterButton_2_label = Label(Frame2, text = 
									 "Search for students by name or ID number.                            ", bg = "white", bd = 3)
		RosterButton_2_label.grid(row = 1, column = 0, padx = 1, pady = 5)
		
		RosterButton_3_label = Label(Frame2, text = 
									 "Display the entire roster in alphabetical order by last names", 
									 bg = "white", bd = 3)
		RosterButton_3_label.grid(row = 2, column = 0, padx = 1, pady = 5)
		
		self.roster = Roster #because there weren't input variables in any of my class functions (for the most part) I just set an attribute of the menu to a roster object
		self.roster.add_students_txt("gradebooktest.txt") #reading from a text to initially add students since that was part of project 4
		
		root.mainloop() #the equivalent to main() I believe
		
	def menu_option_1(self):
		self.roster.add_students()

	def menu_option_2(self):
		self.roster.search_Roster()
		
	def menu_option_3(self):
		self.roster.sort_Roster()
		self.roster.print_Roster()
		
def merge_sort(roster, search_by): #the merge sort, using a "search-by" index so that users can sort by first name, last name or ID
	if len(roster) == 1:
		return roster
		
	else:
		mid = len(roster)//2
		short_roster_1 = roster[:mid]
		short_roster_2 = roster[mid:]
		
		sorted1 = merge_sort(short_roster_1, search_by)
		sorted2 = merge_sort(short_roster_2, search_by)
		return merge(sorted1, sorted2, search_by)

def merge(sorted1, sorted2, search_by): #sorting by comparing "search-by"
	merged = []
	while len(sorted1) > 0 and len(sorted2) > 0:
		if sorted1[0].search_for[search_by] < sorted2[0].search_for[search_by]:
			merged.append(sorted1[0])
			sorted1.remove(sorted1[0])
			
		elif sorted1[0].search_for[search_by] > sorted2[0].search_for[search_by]:
			merged.append(sorted2[0])
			sorted2.remove(sorted2[0])
			
		else:
			merged.append(sorted1[0])
			merged.append(sorted2[0])
			sorted1.remove(sorted1[0])
			sorted2.remove(sorted2[0])
			
	if len(sorted1) > 0:
		sortedlist = merged + sorted1
		return sortedlist
		
	else:
		sortedlist = merged + sorted2
		return sortedlist

def bin_search(roster, search_target, search_by): 
	#search_by in this too because merge_sort sorts the list by a specified thing, the binary search only works for what the roster was sorted by
	if roster == []: 
		print("No matching student has been found.\n")
		user_confirm = input("Would you like to search for another student?:\n")
	else:
		mid = len(roster)//2 
		if roster[mid].search_for[search_by] == search_target:
			roster[mid].print_student_info()
			
		elif roster[mid].search_for[search_by] > search_target:
			search_result = bin_search(roster[:mid], search_target, search_by)
			return search_result
			
		elif roster[mid].search_for[search_by] < search_target:
			search_result = bin_search(roster[mid+1:], search_target, search_by)
			return search_result

def main(): #such a short main!
	roster = Roster()
	menu = Menu(roster)
main() #thank you Professor Pan, I learned a lot and enjoyed your class very much! Have a great summer!