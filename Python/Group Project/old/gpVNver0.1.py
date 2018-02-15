from tkinter import *
from os import path
import sys

root = Tk() #Makes the window
root.wm_title("Window Title") #Makes the title that will appear in the top left
root.config(background = "#FFFFFF") #sets background color to white


#Definitions to Switch Between Frames
def load_home():        #Game Frame 1, 2, and Last are removed and Title Frame positioning set
    Gameframe1.grid_forget()    
    Gameframe2.grid_forget()
    LastGameframe.grid_forget()
    SaveFrame.grid_forget()
    LoadFrame.grid_forget()
    Titleframe.grid(row=0, column=0, padx=10, pady=2)

def load_game1():       #Similar to 'load_home', but applies to different frames.
    Titleframe.grid_forget()
    #Gameframe2.grid_forget()
    #LastGameframe.grid_forget()
    SaveFrame.grid_forget()
    LoadFrame.grid_forget()
    Gameframe1.grid(row=0, column=0, padx=10, pady=2)

def load_game2():       #Similar to 'load_home', but applies to different frames.
    #Titleframe.grid_forget()
    Gameframe1.grid_forget()
    #LastGameframe.grid_forget()
    #SaveFrame.grid_forget()
    #LoadFrame.grid_forget()
    #Gameframe2.grid(row=0, column=0, padx=10, pady=2)

def load_gamelast():    #Similar to 'load_home', but applies to different frames.
    #Titleframe.grid_forget()
    #Gameframe1.grid_forget()
    Gameframe2.grid_forget()
    #SaveFrame.grid_forget()
    #LoadFrame.grid_forget()
    #LastGameframe.grid(row=0, column=0, padx=10, pady=2)

def load_save():        #Similar to 'load_home', but applies to different frames.
    Titleframe.grid_forget()
    LoadFrame.grid_forget()
    SaveFrame.grid(row=0, column=0)

def load_load_frame():    #Similar to 'load_home', but applies to different frames.
    Titleframe.grid_forget()
    SaveFrame.grid_forget()
    LoadFrame.grid(row=0, column=0)

def back_from_save():    #This bring the user back to the story page the user was on from the Save Frame.
    SaveFrame.grid_forget()

def back_from_load():    #This bring the user back to the story page the user was on from the Save Frame.
    LoadFrame.grid_forget()

#Start Game Frame 1
#Game Frame 1 Picture Frame
Gameframe1 = Frame(root, width=650, height = 650,)
Gameframe1.grid(row=0, column=0, padx=10, pady=2)

Frame3 = Frame(Gameframe1)
Frame3.grid(row=0, column=0, padx=10, pady=2)

Gameimage1 = PhotoImage(file = path.abspath('cg\\background\\bg_001.gif'))
Label(Frame3, image = Gameimage1, width=650, height = 650).grid(row=0, column=0, padx=10, pady=2)


GameLabel1 = Label(Frame3, text = "Lable goes here.", bg = "white", bd = 3)
GameLabel1.grid(row=1, column=0, padx=10, pady=2)

#Start Last Game Frame
#Last Game Frame Picture Frame
LastGameframe = Frame(root, width=650, height = 650,)
LastGameframe.grid(row=0, column=0, padx=10, pady=2)

Frame7 = Frame(LastGameframe)
Frame7.grid(row=0, column=0, padx=10, pady=2)

Lastimage = PhotoImage(file = path.abspath('cg\\background\\bg_003.gif'))
Label(Frame7, image=Lastimage, width=650, height = 650,).grid(row=0, column=0, padx=10, pady=2)

GameLabel2 = Label(Frame7, text = "Lable goes here.", bg = "white", bd = 3)
GameLabel2.grid(row=1, column=0, padx=10, pady=2)

#Last Game Frame Button Frame
Frame8 = Frame(LastGameframe)
Frame8.grid(row=1, column=0, padx=10, pady=2)

BackButton = Button(Frame8, text="Back", command = load_game2)
BackButton.grid(row=0, column=0, padx=30, pady=2)

LoadButton = Button(Frame8, text="Load", command = load_load_frame)
LoadButton.grid(row=0, column=1, padx=30, pady=2)

MenuButton = Button(Frame8, text="Menu", command = load_save)
MenuButton.grid(row=0, column=2, padx=30, pady=2)

ExitButton = Button(Frame8, text="Exit")
ExitButton.grid(row=0, column=3, padx=30, pady=2)

#End Last Frame

#Start Game Frame 2
#Game Frame 2 Picture Frame
Gameframe2 = Frame(root, width=650, height = 650,)
Gameframe2.grid(row=0, column=0, padx=10, pady=2)

Frame5 = Frame(Gameframe2)
Frame5.grid(row=0, column=0, padx=10, pady=2)

Gameimage2 = PhotoImage(file = path.abspath('cg\\background\\bg_002.gif'))
Label(Frame5, image = Gameimage2, width=650, height = 650,).grid(row=0, column=0, padx=10, pady=2)

GameLabel2 = Label(Frame5, text = "Lable goes here.", bg = "white", bd = 3)
GameLabel2.grid(row=1, column=0, padx=10, pady=2)

#Game Frame 2 Button Frame
Frame6 = Frame(Gameframe2)
Frame6.grid(row=1, column=0, padx=10, pady=2)

BackButton = Button(Frame6, text="Back", command = load_game1)
BackButton.grid(row=0, column=0, padx=30, pady=2)

LoadButton = Button(Frame6, text="Load", command = load_load_frame)
LoadButton.grid(row=0, column=1, padx=30, pady=2)

MenuButton = Button(Frame6, text="Menu", command = load_save)
MenuButton.grid(row=0, column=2, padx=30, pady=2)

ExitButton = Button(Frame6, text="Exit")
ExitButton.grid(row=0, column=3, padx=30, pady=2)

NextButton = Button(Frame6, text="Next", command = load_gamelast)
NextButton.grid(row=0, column=4, padx=30, pady=2)

root.bind('<Right>', load_gamelast())

#End Game Frame 2

#Game Frame 1 Button Frame
Frame4 = Frame(Gameframe1)
Frame4.grid(row=1, column=0, padx=10, pady=2)

HomeButton = Button(Frame4, text="Home", command = load_home)
HomeButton.grid(row=0, column=0, padx=30, pady=2)

LoadButton = Button(Frame4, text="Load", command = load_load_frame)
LoadButton.grid(row=0, column=1, padx=30, pady=2)

MenuButton = Button(Frame4, text="Menu", command = load_save)
MenuButton.grid(row=0, column=2, padx=30, pady=2)

ExitButton = Button(Frame4, text="Exit")
ExitButton.grid(row=0, column=3, padx=30, pady=2)

NextButton = Button(Frame4, text="Next", command = load_game2)
NextButton.grid(row=0, column=4, padx=30, pady=2) 

root.bind('<Right>', load_game2())
 
#End of Game Frame 1

#Start Save Frame
SaveFrame = Frame(root, width=650, height = 650, bd=3, relief=GROOVE)
SaveFrame.grid(row=0, column=0, padx=10, pady=2)

SaveFrameTitle = Label(SaveFrame, text = "Saved Files", font=("Helvetica", 16))
SaveFrameTitle.grid(row=0, column=0, padx=285, pady=10)

#Save File Buttons
savefolder1image = PhotoImage(file='cg\\icons\\folder.gif')
savefolder1button = Button(SaveFrame, text = "        Save 1", height = 100, width = 180, image = savefolder1image, compound = "left", padx = 10, pady = 10, relief = GROOVE)
savefolder1button.grid(row=1, column=0, padx=100, pady=85)

savefolder2image = PhotoImage(file='cg\\icons\\folder.gif')
savefolder2button = Button(SaveFrame, text = "        Save 2", height = 100, width = 180, image = savefolder2image, compound = "left", padx = 10, pady = 10, relief = GROOVE)
savefolder2button.grid(row=2, column=0, padx=100, pady=85)

#Save Frame Buttons
SaveButtonFrame = Frame(SaveFrame)
SaveButtonFrame.grid(row=3, column=0, padx=10, pady=2)

LoadButton = Button(SaveButtonFrame, text="Load", command = load_load_frame)
LoadButton.grid(row=0, column=0, padx=30, pady=20)

BacktoStoryButton = Button(SaveButtonFrame, text="Back to Story", command = back_from_save)
BacktoStoryButton.grid(row=0, column=1, padx=30, pady=20)

HomeButton = Button(SaveButtonFrame, text="Home", command = load_home)
HomeButton.grid(row=0, column=2, padx=30, pady=20)
#End Save Frame


#Start Load Frame
LoadFrame = Frame(root, width=650, height = 650, bd=3, relief=GROOVE)
LoadFrame.grid(row=0, column=0, padx=10, pady=2)

LoadFrameTitle = Label(LoadFrame, text = "Load Files", font=("Helvetica", 16))
LoadFrameTitle.grid(row=0, column=0, padx=285, pady=10)

#Load File Buttons
loadfolder1image = PhotoImage(file=path.abspath('cg\\icons\\folder.gif'))
loadfolder1button = Button(LoadFrame, text = "        File 1", height = 100, width = 180, image = loadfolder1image, compound = "left", padx = 10, pady = 10, relief = GROOVE)
loadfolder1button.grid(row=1, column=0, padx=100, pady=85)

loadfolder2image = PhotoImage(file= path.abspath('cg\\icons\\folder.gif'))
loadfolder2button = Button(LoadFrame, text = "        File 2", height = 100, width = 180, image = loadfolder2image, compound = "left", padx = 10, pady = 10, relief = GROOVE)
loadfolder2button.grid(row=2, column=0, padx=100, pady=85)

#Load Frame Buttons
LoadButtonFrame = Frame(LoadFrame)
LoadButtonFrame.grid(row=3, column=0, padx=10, pady=2)

LoadButton = Button(LoadButtonFrame, text="Save", command = load_save)
LoadButton.grid(row=0, column=0, padx=30, pady=20)

BacktoStoryButton = Button(LoadButtonFrame, text="Back to Story", command = back_from_load)
BacktoStoryButton.grid(row=0, column=1, padx=30, pady=20)

HomeButton = Button(LoadButtonFrame, text="Home", command = load_home)
HomeButton.grid(row=0, column=2, padx=30, pady=20)
#End Load Frame




#Start Title Frame
#I put the Title Frame Last so it shows ontop of the other frames
#Title Frame Picture Frame
Titleframe = Frame(root, width=600, height = 600)
Titleframe.grid(row=0, column=0, padx=10, pady=2)

Frame1 = Frame(Titleframe)
Frame1.grid(row=0, column=0, padx=10, pady=2)

titleimage = PhotoImage(file = path.abspath('cg\\background\\bg_000.gif'))
Label(Frame1, image = titleimage, width=650, height = 650,).grid(row=0, column=0, padx=10, pady=2)


firstLabel = Label(Frame1, text = "Welcome to the title page.", font=("Helvetica", 16))
firstLabel.grid(row=1, column=0, padx=10, pady=2)

#Title Frame Button Frame
Frame2 = Frame(Titleframe)
Frame2.grid(row=1, column=0, padx=10, pady=2)

StartButton = Button(Frame2, text="Start", command = load_game1)
StartButton.grid(row=0, column=0, padx=30, pady=2)

LoadButton = Button(Frame2, text="Load", command = load_load_frame)
LoadButton.grid(row=0, column=1, padx=30, pady=2)

ExitButton = Button(Frame2, text="Exit")
ExitButton.grid(row=0, column=2, padx=30, pady=2)

#How To Play Frame

#HowToPlay = Frame(root, width=600, height=600)
#HowToPlay.grid(row=0, column=0, padx=10, pady=2)

#Frame9 = Frame(HowToPlay)
#Frame9.grid(row=0, column=0, padx=10, pady=2)

#welcomeLabel = Label(Frame9, text = "How To Play", font=("Helvetica", 16))
#welcomeLabel.grid(row=1, column=0, padx=10, pady=2)

#instructLabel = Label(Frame9, text = "Welcome to our game!\n To play, press Start. To progress through the story, press the Right arrow key.\n We hope you enjoy our game, and don't forget to save your game so you can come back to it later!", bg="white")
#instructLabel.grid(row=2, column=0, padx=10, pady=2)

#How To Play Button Frame

#Frame10 = Frame(HowToPlay)
#Frame10.grid(row=1, column=0, padx=10, pady=2)

#BackButton = Button(Frame10, text="Back to Title", command = load_home)
#BackButton.grid(row=0, column=0, padx=30, pady=2)

#ExitButton = Button(Frame10, text="Exit")
#ExitButton.grid(row=0, column=1, padx=30, pady=2)



#Pop Up Code
#I put the code in a function so if you want to make the pop_up window appear by a button command
#def load_pop_up():
#    top = Toplevel()			#This creates the pop up window
#    top.title("Testing Pop Up")		#This is the title of the pop up window
#    msg = Message(top, text="This is a test")	
#This is the message that appears in the pop up window
#    msg.grid(row=0, column=0, padx=10, pady=2)	
#This controls the arrangements of the text in the pop up window. You can add other widgets to the pop up, just assign them to appear in the pop up window.

root.mainloop()