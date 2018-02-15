########################################################
###                      CS - 21                     ###
###                  Group Project                   ###
### By Jung Kim, Eric Liu, Christine Nguyen, Anna Sy ###
########################################################


from tkinter import*
from os import path
import sys

def open_file(file):
	fp = open(file, "r")
	lines = []
	for line in fp:
		lines.append(line.replace("%", "\n"))
	fp.close()
	return lines

text_script = open_file(path.abspath("scripts\\textscript.txt"))
cg_script = [path.abspath("cg\\background\\bg_000.gif"), path.abspath("cg\\background\\bg_001.gif"), path.abspath("cg\\background\\bg_002.gif"), path.abspath("cg\\background\\bg_003.gif"), path.abspath("cg\\background\\bg_004.gif"), path.abspath("cg\\background\\bg_005.gif"), path.abspath("cg\\background\\bg_006.gif"), path.abspath("cg\\background\\bg_007.gif"), path.abspath("cg\\background\\bg_008.gif"), path.abspath("cg\\background\\bg_009.gif"), path.abspath("cg\\background\\loading.gif")]
char_script = [path.abspath("cg\\charactersprites\\pikachu.gif"), path.abspath("cg\\charactersprites\\nosepass.gif"), path.abspath("cg\\charactersprites\\skitty.gif"), path.abspath("cg\\charactersprites\\eevee.gif"), path.abspath("cg\\charactersprites\\mew.gif")]

class VisualGame(object): 
	def __init__(self):
	
		self.root = Tk() #Makes the window
		self.root.wm_title("Pokecode v1.1") #Makes the title that will appear in the top left
		self.root.config(background = "#FFFFFF") #sets background color to white
		
		self.cg_counter = 10
		self.text_counter = 0
		self.char_counter = 0
		self.read_counter = 0
		
		self.cg_var = StringVar()
		self.cg_var.set(cg_script[self.cg_counter])
		
		self.text_var = StringVar()
		self.text_var.set(text_script[self.text_counter])
		
		self.char_var = StringVar()
		self.char_var.set(char_script[self.char_counter])
		
		####################
		### title screen ###
		####################
		
		self.titleFrame = Frame(self.root, width = 1280, height = 720)
		self.titleFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.Frame1 = Frame(self.titleFrame)
		self.Frame1.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.titleimage = PhotoImage(file = path.abspath('cg\\background\\titlecg.gif'))
		Label(self.Frame1, image = self.titleimage, width = 1280, height = 720,).grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.firstLabel = Label(self.Frame1, text = "Pokecode: the Tale of Coding Pokemons", font=("Helvetica", 16))
		self.firstLabel.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		self.Frame2 = Frame(self.titleFrame)
		self.Frame2.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		### title screen buttons ###

		self.startButton = Button(self.Frame2, text = "Start Game", command = self.game_screen_home)
		self.startButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.loadButton = Button(self.Frame2, text = "Load", command = self.load_screen)
		self.loadButton.grid(row = 0, column = 1, padx = 30, pady = 2)
		
		self.exitButton = Button(self.Frame2, text = "Exit Game", command = self.exit_game)
		self.exitButton.grid(row = 0, column = 2, padx = 30, pady = 2)
		
	def game_screen_frame(self):
	
		###################
		### game screen ###
		###################
	
		self.gameFrame = Frame(self.root, width = 1280, height = 720,)
		self.gameFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.Frame3 = Frame(self.gameFrame)
		self.Frame3.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.gameImage = PhotoImage(file = self.cg_var.get())
		self.gameImage_Label = Label(self.Frame3, image = self.gameImage, width = 1280, height = 690)
		self.gameImage_Label.grid(row = 0, column = 0, padx = 0, pady = 2)
		
		self.gameLabel = Label(self.Frame3, textvariable = self.text_var, 
							   font = (14), anchor = W, justify = LEFT, 
							   width = 128, height = 3, bg = "white", bd = 3)
		self.gameLabel.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		self.gameFrame.bind('<Button-1>', self.callback)
		self.gameImage_Label.bind('<Button-1>', self.callback)
		self.gameLabel.bind('<Button-1>', self.callback)
		
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
		
		self.gameFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
	
	def save_screen_frame(self):
		
		###################
		### save screen ###
		###################
		
		self.saveFrame = Frame(self.root, width = 650, height = 650, bd = 3, relief = GROOVE)
		self.saveFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.saveFrame_Title = Label(self.saveFrame, text = "Saved Files", font = ("Helvetica", 16))
		self.saveFrame_Title.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		### save screen buttons ###
		
		self.savefolder1_image = PhotoImage(file = path.abspath("cg\\icons\\folder.gif"))
		self.savefolder1_button = Button(self.saveFrame, text = "        Save 1", height = 100, width = 180, 
										 image = self.savefolder1_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE, command = self.save1) 
		self.savefolder1_button.grid(row = 1, column = 0, padx = 30, pady = 2)
		
		self.savefolder2_image = PhotoImage(file = path.abspath("cg\\icons\\folder.gif"))
		self.savefolder2_button = Button(self.saveFrame, text = "        Save 2", height = 100, width = 180, 
										 image = self.savefolder2_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE, command = self.save2) 
		self.savefolder2_button.grid(row = 2, column = 0, padx = 30, pady = 2)
		
		self.saveButtonFrame = Frame(self.saveFrame)
		self.saveButtonFrame.grid(row = 3, column = 0, padx = 10, pady = 2)
		
		self.loadButton = Button(self.saveButtonFrame, text = "Load", command = self.load_screen_fromsave)
		self.loadButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.return_to_gameButton = Button(self.saveButtonFrame, text = "Return to game", command = self.return_to_game)
		self.return_to_gameButton.grid(row = 0, column = 1, padx = 30, pady = 2)
		
		self.homeButton = Button(self.saveButtonFrame, text = "Main Menu", command = self.return_to_home_fromsave)
		self.homeButton.grid(row = 0, column = 2, padx = 30, pady = 2)
		
		self.saveFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
	def load_screen_frame(self):
		
		###################
		### load screen ###
		###################
		
		self.loadFrame = Frame(self.root, width = 650, height = 650, bd = 3, relief = GROOVE)
		self.loadFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.loadFrameTitle = Label(self.loadFrame, text = "Load Files", font = ("Helvetica", 16))
		self.loadFrameTitle.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		### load screen buttons ###
		
		self.loadfolder1_image = PhotoImage(file = path.abspath("cg\\icons\\folder.gif"))
		self.loadfolder1_button = Button(self.loadFrame, text = "        File 1", height = 100, width = 180, 
										 image = self.loadfolder1_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE, command = self.load1) 
		self.loadfolder1_button.grid(row = 1, column = 0, padx = 30, pady = 2)
		
		self.loadfolder2_image = PhotoImage(file = path.abspath("cg\\icons\\folder.gif"))
		self.loadfolder2_button = Button(self.loadFrame, text = "        File 2", height = 100, width = 180, 
										 image = self.loadfolder2_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE, command = self.load2) 
		self.loadfolder2_button.grid(row = 2, column = 0, padx = 30, pady = 2)
		
		self.loadButtonFrame = Frame(self.loadFrame)
		self.loadButtonFrame.grid(row = 3, column = 0, padx = 10, pady = 2)
		
		self.loadButton = Button(self.loadButtonFrame, text = "Save", command = self.save_screen_fromload)
		self.loadButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.return_to_gameButton = Button(self.loadButtonFrame, text = "Return to game", command = self.return_load)
		self.return_to_gameButton.grid(row = 0, column = 1, padx = 30, pady = 2)
		
		self.loadFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
	def how_to_play_frame(self):
		
		###################
		### How To Play ###
		###################
		
		self.HowToPlayFrame = Frame(self.root, width = 1280, height = 720)
		self.HowToPlayFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.instructionFrame = Frame(self.HowToPlayFrame)
		self.instructionFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.welcomeLabel = Label(self.instructionFrame, text = "How To Play", font = ("Helvetica", 16))
		self.welcomeLabel.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		self.instructLabel = Label(self.instructionFrame, 
								   text = "Welcome to our game!\nThis is a linear text based game known as a 'Visual Novel'\nTo progress through the story, left click on the text box.\nYou can save or load at any point in the game\nSo don't forget to save your game to come back to it later!\nWe hope you enjoy our game!", 
								   font = ("Helvetica", 14), bg="white")
		self.instructLabel.grid(row = 2, column = 0, padx = 10, pady = 2)
		
		### How to Play buttons ###
		
		self.howtoplaybuttonFrame = Frame(self.HowToPlayFrame)
		self.howtoplaybuttonFrame.grid(row = 2, column = 0, padx = 10, pady = 2)
		
		self.exitButton = Button(self.howtoplaybuttonFrame, text = "Close", command = self.quit_frame)
		self.exitButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.HowToPlayFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
	def return_to_home(self):
		self.gameFrame.grid_forget()
		self.cg_counter = 10
		self.text_counter = 0
		self.char_counter = 0
		self.cg_var.set(cg_script[self.cg_counter])
		self.text_var.set(text_script[self.text_counter])
		self.char_var.set(char_script[self.char_counter])
		self.titleFrame.grid(row=0, column=0, padx=10, pady=2)
	
	def return_to_home_fromsave(self):
		self.saveFrame.grid_forget()
		self.gameFrame.grid_forget()  
		self.cg_counter = 10
		self.text_counter = 0
		self.char_counter = 0
		self.cg_var.set(cg_script[self.cg_counter])
		self.text_var.set(text_script[self.text_counter])
		self.char_var.set(char_script[self.char_counter])
		self.titleFrame.grid(row=0, column=0, padx=10, pady=2)
	
	def game_screen_home(self):
		self.titleFrame.grid_forget()
		self.game_screen_frame()
		self.how_to_play_frame()

	def save_screen(self):
		self.save_screen_frame()
	
	def save_screen_fromload(self):
		self.loadFrame.grid_forget()
		self.save_screen_frame()
	
	def load_screen(self):
		self.load_screen_frame()
	
	def load_screen_fromsave(self):
		self.saveFrame.grid_forget()
		self.load_screen_frame()
	
	def return_to_game(self):
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
		noButton.grid(row = 0, column = 1, padx = 30, pady = 2)

	def quit(self):
		self.root.destroy()
		
	def quit_frame(self):
		self.HowToPlayFrame.grid_forget()
	
	def save1(self):
		fp = open((path.abspath("saves\\save1.txt")), "w")
		fp.write(str(self.cg_counter))
		fp.write("\n")
		fp.write(str(self.text_counter))
		fp.write("\n")
		fp.write(str(self.char_counter))
		fp.write("\n")
		fp.close()
	
	def save2(self):
		fp = open((path.abspath("saves\\save2.txt")), "w")
		fp.write(str(self.cg_counter))
		fp.write("\n")
		fp.write(str(self.text_counter))
		fp.write("\n")
		fp.write(str(self.char_counter))
		fp.write("\n")
		fp.close()
		
	def load1(self):
		file1 = open_file(path.abspath("saves\\save1.txt"))
		
		self.cg_counter = int(file1[0])
		self.cg_var.set(cg_script[self.cg_counter])
		
		self.text_counter = int(file1[1])
		self.text_var.set(text_script[self.text_counter])
		
		self.char_counter = int(file1[2])
		self.char_var.set(char_script[self.char_counter])
		
		self.gameFrame.grid_forget()
		self.gameImage_Label.grid_forget()
		
		self.gameImage = PhotoImage(file = self.cg_var.get())
		self.gameImage_Label = Label(self.Frame3, image = self.gameImage, width = 1280, height = 690)
		
		self.gameImage_Label.grid(row = 0, column = 0, padx = 0, pady = 2)
		self.gameFrame.grid(row=0, column=0, padx=10, pady=2)
		
		self.titleFrame.grid_forget()
	
	def load2(self):
		file2 = open_file(path.abspath("saves\\save2.txt"))
		
		self.cg_counter = int(file2[0])
		self.cg_var.set(cg_script[self.cg_counter])
		
		self.text_counter = int(file2[1])
		self.text_var.set(text_script[self.text_counter])
		
		self.char_counter = int(file2[2])
		self.char_var.set(char_script[self.char_counter])
		
		self.gameFrame.grid_forget()
		self.gameImage_Label.grid_forget()
		
		self.gameImage = PhotoImage(file = self.cg_var.get())
		self.gameImage_Label = Label(self.Frame3, image = self.gameImage, width = 1280, height = 690)
		
		self.gameImage_Label.grid(row = 0, column = 0, padx = 0, pady = 2)
		self.gameFrame.grid(row=0, column=0, padx=10, pady=2)
		
		self.titleFrame.grid_forget()
	
	def next_frame(self):
		if self.text_counter < len(text_script) - 1:
		
			self.text_counter = self.text_counter + 1
			self.text_var.set(text_script[self.text_counter])
			
			
			if self.text_counter == 0 or self.text_counter == 9:
			
				self.gameImage_Label.grid_forget()
				self.cg_counter = 10
				self.cg_var.set(cg_script[self.cg_counter])
				self.gameImage = PhotoImage(file = self.cg_var.get())
				self.gameImage_Label = Label(self.Frame3, image = self.gameImage, width = 1280, height = 690)
				self.gameImage_Label.grid(row = 0, column = 0, padx = 0, pady = 2)
				
				
			elif self.text_counter == 1:
			
				self.gameImage_Label.grid_forget()
				self.cg_counter = 5
				self.cg_var.set(cg_script[self.cg_counter])
				self.gameImage = PhotoImage(file = self.cg_var.get())
				self.gameImage_Label = Label(self.Frame3, image = self.gameImage, width = 1280, height = 690)
				self.gameImage_Label.grid(row = 0, column = 0, padx = 0, pady = 2)
				
				
			elif self.text_counter == 10:
			
				self.gameImage_Label.grid_forget()
				self.cg_counter = 0
				self.cg_var.set(cg_script[self.cg_counter])
				self.gameImage = PhotoImage(file = self.cg_var.get())
				self.gameImage_Label = Label(self.Frame3, image = self.gameImage, width = 1280, height = 690)
				self.gameImage_Label.grid(row = 0, column = 0, padx = 0, pady = 2)
				
				
			elif self.text_counter == 18:
			
				self.gameImage_Label.grid_forget()
				self.cg_counter == 3
				self.cg_var.set(cg_script[self.cg_counter])
				self.gameImage = PhotoImage(file = self.cg_var.get())
				self.gameImage_Label = Label(self.Frame3, image = self.gameImage, width = 1280, height = 690)
				self.gameImage_Label.grid(row = 0, column = 0, padx = 0, pady = 2)
				
		else:
			self.return_to_home()
			

	def callback(self, event):
		self.next_frame()
				
def main():
	VisualGame()
main()
		
