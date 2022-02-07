#------------- Boilerplate Code Start------
import socket
import random
from tkinter import *
from  threading import Thread
from PIL import ImageTk, Image

screen_width = None
screen_height = None

SERVER = None
PORT = None
IP_ADDRESS = None
playerName = None

canvas1 = None
canvas2 = None

nameEntry = None
nameWindow = None
gameWindow = None

leftBoxes = []
rightBoxes = []
finishingBox = None

playerType = None
playerTurn = None
dice = None
rollButton = None

#------------- Boilerplate Code End------


# Student write saveName() here

def rollDice():
    global SERVER
    diceChoices = ['/u2680', '/u2681', '/u2682', '/u2683', '/u2684', '/u2685']
    value = random.choice(diceChoices)
    global playerType
    global playerTurn
    global rollButton
    playerTurn = False
    if(playerType == 'player1'):
        SERVER.send(f'{value}player2Turn'.encode()) 
    
    if(playerType == 'player2'):
        SERVER.send(f'{value}player1Turn'.encode())

def leftBoard():
    global gameWindow
    global leftBoxes
    global screen_height

    xPos = 10
    for box in range(0,11):
        if(box == 0):
            boxLabel = Label(gameWindow, font=("Helvetica",30), width=2, height=1, relief='ridge', borderwidth=1, bg="red")
            boxLabel.place(x=xPos, y=screen_height/2 - 100)
            leftBoxes.append(boxLabel)
            xPos +=55
        else:
            boxLabel = Label(gameWindow, font=("Helvetica",30), width=2, height=1, relief='ridge', borderwidth=2, bg="white")
            boxLabel.place(x=xPos, y=screen_height/2- 100)
            leftBoxes.append(boxLabel)
            xPos +=55

def rightBoard():
    global gameWindow
    global rightBoxes
    global screen_height

    xPos = screen_width/2 + 70
    for box in range(0,11):
        if(box == 10):
            boxLabel = Label(gameWindow, font=("Helvetica",30), width=2, height=1, relief='ridge', borderwidth=1, bg="yellow")
            boxLabel.place(x=xPos, y=screen_height/2-100)
            rightBoxes.append(boxLabel)
            xPos +=55
        else:
            boxLabel = Label(gameWindow, font=("Helvetica",30), width=2, height=1, relief='ridge', borderwidth=2, bg="white")
            boxLabel.place(x=xPos, y=screen_height/2 - 100)
            rightBoxes.append(boxLabel)
            xPos +=55

def finishingBox():
    global gameWindow
    global finishingBox
    global screen_width
    global screen_height

    finishingBox = Label(gameWindow, text="Home", font=("Chalkboard SE", 30), width=5, height=2, borderwidth=0, bg="green", fg="white")
    finishingBox.place(x=screen_width/2 - 58, y=screen_height/2 -120)

def gameWindow():

    global gameWindow
    global canvas2
    global screen_width
    global screen_height
    global dice
    global playerTurn
    


    gameWindow = Tk()
    gameWindow.title("Ludo Ladder")
    #gameWindow.attributes('-fullscreen',True)

    screen_width = gameWindow.winfo_screenwidth()
    screen_height = gameWindow.winfo_screenheight()

    #bg = ImageTk.PhotoImage(file = "./assets/background.png")
    
    img1_old=Image.open("/Users/vanshbafna/Desktop/module5/C204/assets/background.png") 
    img1_resized=img1_old.resize((screen_width, screen_height)) 
    # new width & height 
    my_img1=ImageTk.PhotoImage(img1_resized)
    
    canvas2 = Canvas( gameWindow, width = 500,height = 500)
    canvas2.pack(fill = "both", expand = True)

    # Display image
    canvas2.create_image( 0, 0, image = my_img1, anchor = "nw")

    # Add Text
    canvas2.create_text( screen_width/2, screen_height/5, text = "Ludo Ladder", font=("Chalkboard SE",100), fill="white")

    


    # Teacher Activity
    leftBoard()
    rightBoard()

   
    finishingBox()
    global rollButton 

    rollButton = Button(gameWindow,text="Roll Dice", fg='black', font=("Chalkboard SE", 15), bg="grey",command=rollDice, width=20, height=5)
    
    global playerTurn
    global playerType
    global playerName


   # if(playerType == 'player1' and playerTurn):
       # rollButton.place(x=screen_width / 2 - 80, y=screen_height/2  + 250)
    #else:
       # rollButton.pack_forget()


    

    # Creating Dice with value 1
    dice = canvas2.create_text(screen_width/2 , screen_height/2 + 100, text = "\u2680", font=("Chalkboard SE",250), fill="white")

    gameWindow.resizable(True, True)
    gameWindow.mainloop()



def saveName():
    global SERVER 
    global playerName 
    global nameWindow 
    global nameEntry 
    playerName = nameEntry.get() 
    nameEntry.delete(0, END) 
    nameWindow.destroy() 
    # Sending Message to Server 
    SERVER.send(playerName.encode())
    gameWindow()


def askPlayerName():
    global playerName
    global nameEntry
    global nameWindow
    global canvas1
    global screen_width
    global screen_height

    nameWindow  = Tk()
    nameWindow.title("Ludo Ladder")
    nameWindow.attributes('-fullscreen',True)


    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    #bg = ImageTk.PhotoImage(file = "./assets/background.png")

    img_old=Image.open("/Users/vanshbafna/Desktop/module5/C204/assets/background.png") 
    img_resized=img_old.resize((screen_width, screen_height)) 
    # new width & height 
    my_img=ImageTk.PhotoImage(img_resized)


    canvas1 = Canvas( nameWindow, width = 500,height = 500)
    canvas1.pack(fill = "both", expand = True)
    # Display image
    #canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    canvas1.create_image( 0, 0, image = my_img, anchor = "nw")
    canvas1.create_text( screen_width/2, screen_height/5, text = "Enter Name", font=("Chalkboard SE",100), fill="white")

    nameEntry = Entry(nameWindow, width=15, justify='center', font=('Chalkboard SE', 50), bd=5, bg='white')
    nameEntry.place(x = screen_width/2 - 220, y=screen_height/4 + 100)

    button = Button(nameWindow, text="Save", font=("Chalkboard SE", 30),width=15, command=saveName, height=2, bg="#80deea", bd=3)
    button.place(x = screen_width/2 - 130, y=screen_height/2 - 30)

    nameWindow.resizable(True, True)
    nameWindow.mainloop()

def recivedMsg():
    pass

# Boilerplate Code
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Creating First Window
    askPlayerName()




setup()
