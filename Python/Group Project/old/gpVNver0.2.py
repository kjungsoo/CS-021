from tkinter import*
from os import path
import sys

def open_file(file):
	fp = open(file, "r")
	lines = fp.readlines()
	fp.close()
	return lines

text_script = open_file("gamescript.txt")
cg_script = [path.abspath("cg\\background\\titlecg.gif"), path.abspath("cg\\background\\bg_000"), path.abspath("cg\\background\\bg_001"), path.abspath("cg\\background\\bg_002"), path.abspath("cg\\background\\bg_003"), path.abspath("cg\\background\\bg_004"), path.abspath("cg\\background\\bg_005"), path.abspath("cg\\background\\bg_006"), path.abspath("cg\\background\\bg_007"), path.abspath("cg\\background\\bg_008"), path.abspath("cg\\background\\bg_009")]
char_script = [path.abspath("cg\\charactersprites\\pikachu.gif"), path.abspath("cg\\charactersprites\\nosepass.gif"), path.abspath("cg\\charactersprites\\skitty.gif"), path.abspath("cg\\charactersprites\\eevee.gif"), path.abspath("cg\\charactersprites\\mew.gif")]

class VisualGame(object):
	def __init__(self):
	
		self.root = Tk() #Makes the window
		self.root.wm_title("Window Title") #Makes the title that will appear in the top left
		self.root.config(background = "#FFFFFF") #sets background color to white
		self.cg_var = cg_script[0]
		self.text_var = text_script[0]
		self.char_var = char_script[0]
		self.cg_counter = 0
		self.text_counter = 0
		self.char_counter = 0
		
		###################
		### game screen ###
		###################
		
		self.gameFrame = Frame(self.root, width = 1280, height = 720,)
		self.gameFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.Frame3 = Frame(self.gameFrame)
		self.Frame3.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.gameImage = PhotoImage(file = path.abspath('cg\\background\\bg_001.gif'))
		Label(self.Frame3, image = self.gameImage, width = 1280, height = 690).grid(row = 0, 
																			   column = 0, 
																			   padx = 0, pady = 2)
		
		self.gameLabel = Label(self.Frame3, text = "Label goes here.", 
							   width = 182, height = 4, bg = "white", bd = 3)
		self.gameLabel.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		### game screen buttons ###
		
		self.Frame4 = Frame(self.gameFrame)
		self.Frame4.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		self.homeButton = Button(self.Frame4, text = "Home", command = self.return_to_home)
		self.homeButton.grid(row = 0, column = 0, padx = 30, pady = 2)

		self.loadButton = Button(self.Frame4, text = "Load", command = self.load_screen)
		self.loadButton.grid(row = 0, column = 1, padx = 30, pady = 2)

		self.saveButton = Button(self.Frame4, text = "Save", command = self.save_screen)
		self.saveButton.grid(row = 0, column = 2, padx = 30, pady = 2)

		self.exitButton = Button(self.Frame4, text = "Exit", command = self.exit_game)
		self.exitButton.grid(row = 0, column = 3, padx = 30, pady = 2)
		
		###################
		### save screen ###
		###################
		
		self.saveFrame = Frame(self.root, width = 650, height = 650, bd = 3, relief = GROOVE)
		self.saveFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.saveFrame_Title = Label(self.saveFrame, text = "Saved Files", font = ("Helvetica", 16))
		self.saveFrame_Title.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		### save screeb buttons ###
		
		self.savefolder1_image = PhotoImage(file = path.abspath("cg\\icons\\folder.gif"))
		self.savefolder1_button = Button(self.saveFrame, text = "        Save 1", height = 100, width = 180, 
										 image = self.savefolder1_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE)
		self.savefolder1_button.grid(row = 1, column = 0, padx = 30, pady = 2)
		
		self.savefolder2_image = PhotoImage(file = path.abspath("cg\\icons\\folder.gif"))
		self.savefolder2_button = Button(self.saveFrame, text = "        Save 2", height = 100, width = 180, 
										 image = self.savefolder2_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE)
		self.savefolder2_button.grid(row = 2, column = 0, padx = 30, pady = 2)
		
		self.saveButtonFrame = Frame(self.saveFrame)
		self.saveButtonFrame.grid(row = 3, column = 0, padx = 10, pady = 2)
		
		self.loadButton = Button(self.saveButtonFrame, text = "Load", command = self.load_screen)
		self.loadButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.return_to_gameButton = Button(self.saveButtonFrame, text = "Return to game", command = self.return_save)
		self.return_to_gameButton.grid(row = 0, column = 1, padx = 30, pady = 2)
		
		self.homeButton = Button(self.saveButtonFrame, text = "Main Menu", command = self.return_to_home)
		self.homeButton.grid(row = 0, column = 2, padx = 30, pady = 2)
		
		###################
		### load screen ###
		###################
		
		self.loadFrame = Frame(self.root, width=650, height = 650, bd=3, relief=GROOVE)
		self.loadFrame.grid(row=0, column=0, padx=10, pady=2)
		
		self.loadFrameTitle = Label(self.loadFrame, text = "Load Files", font = ("Helvetica", 16))
		self.loadFrameTitle.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		### load screen buttons ###
		
		self.loadfolder1_image = PhotoImage(file = path.abspath("cg\\icons\\folder.gif"))
		self.loadfolder1_button = Button(self.loadFrame, text = "        File 1", height = 100, width = 180, 
										 image = self.loadfolder1_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE)
		self.loadfolder1_button.grid(row = 1, column = 0, padx = 30, pady = 2)
		
		self.loadfolder2_image = PhotoImage(file = path.abspath("cg\\icons\\folder.gif"))
		self.loadfolder2_button = Button(self.loadFrame, text = "        File 2", height = 100, width = 180, 
										 image = self.loadfolder2_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE)
		self.loadfolder2_button.grid(row = 2, column = 0, padx = 30, pady = 2)
		
		self.loadButtonFrame = Frame(self.loadFrame)
		self.loadButtonFrame.grid(row = 3, column = 0, padx = 10, pady = 2)
		
		self.loadButton = Button(self.loadButtonFrame, text = "Save", command = self.save_screen)
		self.loadButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.return_to_gameButton = Button(self.loadButtonFrame, text = "Return to game", command = self.return_load)
		self.return_to_gameButton.grid(row = 0, column = 1, padx = 30, pady = 2)
		
		self.homeButton = Button(self.loadButtonFrame, text = "Main Menu", command = self.return_to_home)
		self.homeButton.grid(row = 0, column = 2, padx = 30, pady = 2)
		
		###################
		### How To Play ###
		###################
		
		
		
		####################
		### title screen ###
		####################
		
		self.titleFrame = Frame(self.root, width = 1280, height = 720)
		self.titleFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.Frame1 = Frame(self.titleFrame)
		self.Frame1.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.titleimage = PhotoImage(file = cg_script[0])
		Label(self.Frame1, image = self.titleimage, width = 1280, height = 720,).grid(row = 0, column = 0, 
																				 padx = 10, pady = 2)
		
		self.firstLabel = Label(self.Frame1, text = "Group Project", font=("Helvetica", 16))
		self.firstLabel.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		self.Frame2 = Frame(self.titleFrame)
		self.Frame2.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		### title screen buttons ###

		self.startButton = Button(self.Frame2, text = "Start Game", command = self.game_screen)
		self.startButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.loadButton = Button(self.Frame2, text = "Load", command = self.load_screen)
		self.loadButton.grid(row = 0, column = 1, padx = 30, pady = 2)
		
		self.exitButton = Button(self.Frame2, text = "Exit Game", command = self.exit_game)
		self.exitButton.grid(row = 0, column = 2, padx = 30, pady = 2)
		
		#self.root.mainloop()
		
	def return_to_home(self):
		self.gameFrame.grid_forget()    
		self.saveFrame.grid_forget()
		self.loadFrame.grid_forget()
		self.titleFrame.grid(row=0, column=0, padx=10, pady=2)

	def game_screen(self):
		self.titleFrame.grid_forget()
		self.saveFrame.grid_forget()
		self.loadFrame.grid_forget()
		self.gameFrame.grid(row=0, column=0, padx=10, pady=2)

	def save_screen(self):
		self.titleFrame.grid_forget()
		self.loadFrame.grid_forget()
		self.saveFrame.grid(row=0, column=0, padx=10, pady=2)

	def load_screen(self):
		self.titleFrame.grid_forget()
		self.saveFrame.grid_forget()
		self.loadFrame.grid(row=0, column=0, padx=10, pady=2)

	def return_save(self):
		self.saveFrame.grid_forget()

	def return_load(self):
		self.loadFrame.grid_forget()
		
	def exit_game(self):
		top = Toplevel()
		top.title("Confirm")
		
		quittingFrame = Frame(top, width = 300, height = 100)
		quittingFrame.grid(row = 0, column = 0, padx = 10, pady = 10)
		
		confirm_messageFrame = Frame(quittingFrame)
		confirm_messageFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		msg = Message(confirm_messageFrame, text = "Would you like to quit?", width = 500)
		msg.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		confirm_buttonFrame = Frame(quittingFrame)
		confirm_buttonFrame.grid(row = 1, column = 0, padx = 30, pady = 2)
		
		yesButton = Button(confirm_buttonFrame, text = "Yes", command = quit)
		yesButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		noButton = Button(confirm_buttonFrame, text = "No", command = top.destroy)
		noButton.grid(row = 0, column = 1, padx = 30, pady =2)

	def quit(self):
		self.root.destroy()
	
	def save(self, file):
		fp = open(file, "w")
		f.write(self.cg_counter, "\n")
		f.write(self.text_counter, "\n")
		f.write(self.char_counter, "\n")
		fp.close()
		
	def load(self, lines):
		self.cg_var = cg_script[lines[0]]
		self.text_var = text_script[lines[1]]
		self.char_var = char_script[lines[2]]
	
	def next_frame(self, decision):
		if decision == 1:
			self.cg_counter = self.cg_counter + 1
			self.cg_var = cg_script[self.cg_counter]
		elif decision == 2:
			self.text_counter = self.text_counter + 1
			self.text_var = text_script[self.text_counter]
		elif decision == 3:
			self.char_counter = self.char_counter + 1
			self.char_var = char_script[self.char_counter]

		
def main():
	VisualGame()
main()