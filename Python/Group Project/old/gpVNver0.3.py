from tkinter import*
import sys

class VisualGame(object):
	def __init__(self):
	
		self.root = Tk() #Makes the window
		self.root.wm_title("Pokecode v1.7") #Makes the title that will appear in the top left
		self.root.config(background = "#FFFFFF") #sets background color to white
	
		###################
		### game screen ###
		###################
		
		self.gameFrame = Frame(self.root, width = 1280, height = 720,)
		self.gameFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.Frame3 = Frame(self.gameFrame)
		self.Frame3.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.gameImage = PhotoImage(file = 'C:\\Users\\JSK\\Desktop\\cg\\background\\bg_001.gif')
		Label(self.Frame3, image = self.gameImage, width = 1280, height = 690).grid(row = 0, 
																			   column = 0, 
																			   padx = 0, pady = 2)
		
		self.gameLabel = Label(self.Frame3, text = "Name\nDialogue line 1\nDialogue line 2", 
							   font = (14), anchor = W, justify = LEFT, 
							   width = 128, height = 3, bg = "white", bd = 3)
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
		
		self.savefolder1_image = PhotoImage(file = "C:\\Users\\JSK\\Desktop\\cg\\icons\\folder.gif")
		self.savefolder1_button = Button(self.saveFrame, text = "        Save 1", height = 100, width = 180, 
										 image = self.savefolder1_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE)
		self.savefolder1_button.grid(row = 1, column = 0, padx = 30, pady = 2)
		
		self.savefolder2_image = PhotoImage(file = "C:\\Users\\JSK\\Desktop\\cg\\icons\\folder.gif")
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
		
		self.loadfolder1_image = PhotoImage(file = "C:\\Users\\JSK\\Desktop\\cg\\icons\\folder.gif")
		self.loadfolder1_button = Button(self.loadFrame, text = "        File 1", height = 100, width = 180, 
										 image = self.loadfolder1_image, compound = "left", 
										 padx = 10, pady = 10, relief = GROOVE)
		self.loadfolder1_button.grid(row = 1, column = 0, padx = 30, pady = 2)
		
		self.loadfolder2_image = PhotoImage(file = "C:\\Users\\JSK\\Desktop\\cg\\icons\\folder.gif")
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
		
		self.HowToPlayFrame = Frame(self.root, width = 1280, height = 720)
		self.HowToPlayFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.instructionFrame = Frame(self.HowToPlayFrame)
		self.instructionFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.welcomeLabel = Label(self.instructionFrame, text = "How To Play", font = ("Helvetica", 16))
		self.welcomeLabel.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		self.instructLabel = Label(self.instructionFrame, 
		                           text = "Welcome to our game!\nThis is a linear text based game known as a 'Visual Novel'\nTo progress through the story, press the Enter key.\nYou can save or load at any point in the game\nSo don't forget to save your game to come back to it later!\nWe hope you enjoy our game!", 
								   font = ("Helvetica", 14), bg="white")
		self.instructLabel.grid(row = 2, column = 0, padx = 10, pady = 2)
		
		### How to Play buttons ###
		
		self.howtoplaybuttonFrame = Frame(self.HowToPlayFrame)
		self.howtoplaybuttonFrame.grid(row = 2, column = 0, padx = 10, pady = 2)
		
		#self.backButton = Button(self.howtoplaybuttonFrame, text = "Back to Title", command = self.return_to_home)
		#self.backButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.exitButton = Button(self.howtoplaybuttonFrame, text = "Close", command = self.quit_frame)
		self.exitButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		####################
		### title screen ###
		####################
		
		self.titleFrame = Frame(self.root, width = 1280, height = 720)
		self.titleFrame.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.Frame1 = Frame(self.titleFrame)
		self.Frame1.grid(row = 0, column = 0, padx = 10, pady = 2)
		
		self.titleimage = PhotoImage(file = 'C:\\Users\\JSK\\Desktop\\cg\\background\\titlecg.gif')
		Label(self.Frame1, image = self.titleimage, width = 1280, height = 720,).grid(row = 0, column = 0, 
																				 padx = 10, pady = 2)
		
		self.firstLabel = Label(self.Frame1, text = "Pokecode: the Tale of Coding Pokemons", font=("Helvetica", 16))
		self.firstLabel.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		self.Frame2 = Frame(self.titleFrame)
		self.Frame2.grid(row = 1, column = 0, padx = 10, pady = 2)
		
		### title screen buttons ###

		self.startButton = Button(self.Frame2, text = "Start Game", command = self.game_screen)
		self.startButton.grid(row = 0, column = 0, padx = 30, pady = 2)
		
		self.loadButton = Button(self.Frame2, text = "Load", command = self.load_screen_title)
		self.loadButton.grid(row = 0, column = 1, padx = 30, pady = 2)
		
		self.exitButton = Button(self.Frame2, text = "Exit Game", command = self.exit_game)
		self.exitButton.grid(row = 0, column = 2, padx = 30, pady = 2)
		
		#self.root.mainloop()
		
	def return_to_home(self):
		self.HowToPlayFrame.grid_forget()
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
		self.HowToPlayFrame.grid_forget()
		self.titleFrame.grid_forget()
		self.saveFrame.grid_forget()
		self.loadFrame.grid(row=0, column=0, padx=10, pady=2)
		
	def load_screen_title(self):
		self.HowToPlayFrame.grid_forget()
		self.gameFrame.grid_forget()
		self.saveFrame.grid_forget()
		self.titleFrame.grid_forget()
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
		
	def quit_frame(self):
		self.HowToPlayFrame.grid_forget()
		
def main():
	VisualGame()
main()