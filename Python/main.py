from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from random import randint
import numpy as np

# Main Tk
window = Tk()
window.title('Kolko i krzyzyk')
window.iconbitmap('images/ikonka.ico')
window.attributes('-fullscreen', True)

# Integers
queue = 0
gameType = -1
botTime = 1000 * 2

# Booleans
trwaGra = False
board = np.array(2*[5*[5*[False]]])
wyniki = np.array(21*[5*[5*[False]]])

# Lists
playerMoves = []
botMoves = []

# Variables
bot = IntVar()

# Photos
from photos import *

# Labels
player = Label(window)
player1 = Label(window)
player2 = Label(window)
computer = Label(window)

win = Label(window, image=photoTrwaGra)
withComputerPhoto = Label(window, image=photoPlayWithComputer)
withoutComputerPhoto = Label(window, image=photoPlayWithoutComputer)
gameTypeLabal = Label(window, image=photoGameType)
rozdzielczoscLabal = Label(window, image=photoRozdzielczosc)

# Buttons
field = []
field.append(Button(window, command=lambda: pressGame(0), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(1), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(2), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(3), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(4), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(5), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(6), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(7), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(8), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(9), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(10), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(11), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(12), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(13), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(14), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(15), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(16), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(17), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(18), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(19), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(20), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(21), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(22), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(23), image=photoBlank))
field.append(Button(window, command=lambda: pressGame(24), image=photoBlank))

buttonStart = Button(window, command=lambda: startGame(), image=photoStart)
buttonSettings = Button(window, command=lambda: settingsMenu(rozdzielczosc), image=photoUstawienia)
buttonExit = Button(window, command=lambda: closeWindow(), image=photoExit)
buttonAgain = Button(window, command=lambda: reset(), image=photoNowaGra)
buttonBack = Button(window, command=lambda: startMenu(), image=photoBack)

# Radio button
withComputer = Radiobutton(window, variable=bot, value=1)
withoutComputer = Radiobutton(window, variable=bot, value=0)

# Combo box
combo = Combobox(window, state='readonly', values=('3x3', '4x4', '5x5'))
combo.current(0)

rozdzielczosc = Combobox(window, state='readonly', values=('1920x1080', '-inna'))
rozdzielczosc.current(1)

# Functions
def closeWindow():
    if trwaGra:
        result = messagebox.askquestion('Wyjście z gry', 'Czy na pewno chcesz wyjść?')
        if result == 'yes':
            window.destroy()
            return
        elif result == 'no':
            return

    window.destroy()

def clearWindow():
    for x in field:
        x.grid_forget()
    withComputer.grid_forget()
    withoutComputer.grid_forget()
    withComputerPhoto.grid_forget()
    withoutComputerPhoto.grid_forget()
    buttonBack.grid_forget()
    combo.grid_forget()
    gameTypeLabal.grid_forget()
    player.grid_forget()
    player1.grid_forget()
    player2.grid_forget()
    computer.grid_forget()
    buttonAgain.grid_forget()
    win.grid_forget()
    rozdzielczosc.grid_forget()
    rozdzielczoscLabal.grid_forget()
    buttonStart.grid_forget()
    buttonSettings.grid_forget()
    buttonExit.grid_forget()

    for x in field:
        x.place_forget()
    withComputer.place_forget()
    withoutComputer.place_forget()
    withComputerPhoto.place_forget()
    withoutComputerPhoto.place_forget()
    buttonBack.place_forget()
    combo.place_forget()
    gameTypeLabal.place_forget()
    player.place_forget()
    player1.place_forget()
    player2.place_forget()
    computer.place_forget()
    buttonAgain.place_forget()
    win.place_forget()
    rozdzielczosc.place_forget()
    rozdzielczoscLabal.place_forget()
    buttonStart.place_forget()
    buttonSettings.place_forget()
    buttonExit.place_forget()

def addFieldToPlayer(num):
    if num >= 0 and num < 3 + gameType:
        board[queue % 2][0][num] = True
    elif num >= 3 + gameType and num < 6 + (gameType * 2):
        board[queue % 2][1][num - (3 + gameType)] = True
    elif num >= 6 + (gameType * 2) and num < 9 + (gameType * 3):
        board[queue % 2][2][num - (6 + (gameType * 2))] = True
    elif num >= 9 + (gameType * 3) and num < 12 + (gameType * 4):
        board[queue % 2][3][num - (9 + (gameType * 3))] = True
    else:
        board[queue % 2][4][num - (12 + (gameType * 4))] = True

def highlight():
    if bot.get():
        if queue % 2 == 0:
            player.configure(image=photoGraczHighlighted)
            computer.configure(image=photoKomputer)
        else:
            computer.configure(image=photoKomputerHighlighted)
            player.configure(image=photoGracz)
    else:
        if queue % 2 == 0:
            player1.configure(image=photoGracz1Highlighted)
            player2.configure(image=photoGracz2)
        else:
            player2.configure(image=photoGracz2Highlighted)
            player1.configure(image=photoGracz1)

def checkFieldState(num):
    for i in range(0, len(botMoves)):
        if num == botMoves[i]:
            return True
    for i in range(0, len(playerMoves)):
        if num == playerMoves[i]:
            return True
    return False

def botMove():
    if not trwaGra:
        return

    los = 0
    while True:
        los = randint(0, ((gameType + 3) * (gameType + 3)) - 1)
        if checkFieldState(los):
            continue
        else:
            break

    botMoves.append(los)
    field[los].config(image=checkImage(queue%2))

    for i in range(0, ((gameType + 3) * (gameType + 3))):
        if not checkFieldState(i):
            field[i].config(state='')

    addFieldToPlayer(los)
    playerCheck(queue%2)

def endImage(num):
    if bot.get():
        if num == 0:
            return photoWygralGracz
        if num == 1:
            return photoWygralKomputer
    else:
        if num == 0:
            return photoWygralGracz1
        if num == 1:
            return photoWygralGracz2
    return photoRemis

def endMessage(num, field1, field2, field3, type):
    global trwaGra
    trwaGra = False
    win.configure(image=endImage(num))
    if num == 2:
        return

    fields = (field1, field2, field3)
    win.configure(image=endImage(num))
    if num == 0:
        for x in fields:
            x.configure(image=photoCircleEndList[type])
    else:
        for x in fields:
            x.configure(image=photoCrossEndList[type])

    for x in field:
        x.config(state='disabled')

def playerCheck(num):
    for i in range(0, len(wyniki)):
        fields = np.array(5*[0])
        fields_num = 0
        for w in range(0, 3+gameType):
            for k in range(0, 3+gameType):
                if wyniki[i][w][k] and board[num][w][k]:
                    fields[fields_num] = k + (w * (3 + gameType))
                    fields_num += 1
        if fields_num >= 3:
            if fields[0] == fields[1]-1:
                if fields[1] == fields[2]-1:
                    endMessage(num, field[fields[0]], field[fields[1]], field[fields[2]], 0)
                    return
            if fields[0]+3+gameType == fields[1]:
                if fields[1]+3+gameType == fields[2]:
                    endMessage(num, field[fields[0]], field[fields[1]], field[fields[2]], 1)
                    return
            if fields[0]+4+gameType == fields[1]:
                if fields[1]+4+gameType == fields[2]:
                    endMessage(num, field[fields[0]], field[fields[1]], field[fields[2]], 2)
                    return
            if fields[0]+2+gameType == fields[1]:
                if fields[1]+2+gameType == fields[2]:
                    endMessage(num, field[fields[0]], field[fields[1]], field[fields[2]], 3)
                    return

    remis = 0
    for x in range(0, 2):
        for w in range(0, 5):
            for k in range(0, 5):
                if board[x][w][k]:
                    remis += 1

    if remis == (gameType+3) * (gameType+3):
        endMessage(2, 0, 0, 0, 0)
        return

    global queue, trwaGra
    queue += 1
    highlight()

    if bot.get() and queue%2 == 1 and trwaGra:
        trwaGra = True
        for x in field:
            x.config(state='disabled')
        window.after(botTime, botMove)

def reset():
    result = messagebox.askquestion('Nowa gra', 'Czy na pewno chcesz ponownie zagrać?')
    if result == 'yes':
        global queue, trwaGra
        global playerMoves, botMoves
        queue = 0
        trwaGra = True
        botMoves = []
        playerMoves = []

        highlight()
        win.configure(image=photoTrwaGra)
        for x in field:
            x.config(state='normal', image=photoBlank)
        for x in range(0, 2):
            for i in range(0, 5):
                for k in range(0, 5):
                    board[x][i][k] = False

def checkImage(num):
    if num == 0:
        return photoCircle
    return photoCross

def pressGame(num):
    field[num].config(state='disabled', image=checkImage(queue%2))
    addFieldToPlayer(num)
    playerMoves.append(num)

    playerCheck(queue%2)

def startGame():
    global gameType
    gameType = int(str(combo.get())[0]) - 3

    buttonStart.grid_forget()
    buttonSettings.grid_forget()

    global trwaGra
    trwaGra = True

    clearWindow()
    if str(rozdzielczosc.get()) == '-inna':
        for i in range(0, (gameType+3) * (gameType+3)):
            if i >= 0 and i < 3 + gameType:
                field[i].grid(row=0, column=i + 2)
            elif i >= 3 + gameType and i < 6 + (gameType*2):
                field[i].grid(row=1, column=i - 1 - gameType)
            elif i >= 6 + (gameType*2) and i < 9 + (gameType*3):
                field[i].grid(row=2, column=i - 4 - (gameType*2))
            elif i >= 9 + (gameType*3) and i < 12 + (gameType*4):
                field[i].grid(row=3, column=i - 7 - (gameType*3))
            else:
                field[i].grid(row=4, column=i - 10 - (gameType*4))
            field[i].config(image=photoBlank)

        if bot.get():
            player.grid(row=1, column=0)
            computer.grid(row=1, column=5 + gameType)
        else:
            player1.grid(row=1, column=0)
            player2.grid(row=1, column=5 + gameType)

        if gameType == 0:
            win.grid(row=3, column=3)
            buttonBack.grid(row=3, column=4)
            buttonAgain.grid(row=3, column=5)
            buttonExit.grid(row=4, column=5)
        elif gameType == 1:
            win.grid(row=4, column=3)
            buttonBack.grid(row=4, column=5)
            buttonAgain.grid(row=4, column=6)
            buttonExit.grid(row=4, column=7)
        else:
            win.grid(row=3, column=7)
            buttonBack.grid(row=3, column=8)
            buttonAgain.grid(row=4, column=7)
            buttonExit.grid(row=4, column=8)
    else:
        for i in range(0, (gameType+3) * (gameType+3)):
            if i >= 0 and i < 3 + gameType:
                field[i].place(x=300 + (i*210), y=90-(40*gameType))
            elif i >= 3 + gameType and i < 6 + (gameType*2):
                field[i].place(x=300 + ((i - (3 + gameType))*210), y=300-(40*gameType))
            elif i >= 6 + (gameType*2) and i < 9 + (gameType*3):
                field[i].place(x=300 + ((i - (3 + gameType)*2)*210), y=510-(40*gameType))
            elif i >= 9 + (gameType*3) and i < 12 + (gameType*4):
                field[i].place(x=300 + ((i - (3 + gameType)*3)*210), y=720-(40*gameType))
            else:
                field[i].place(x=300 + ((i - (3 + gameType)*4)*210), y=930-(40*gameType))
            field[i].config(image=photoBlank)

        if bot.get():
            player.place(x=90, y=300)
            computer.place(x=300 + ((3 + gameType)*210), y=300)
        else:
            player1.place(x=90, y=300)
            player2.place(x=300 + ((3 + gameType)*210), y=300)

        win.place(x=1440, y=10)
        buttonAgain.place(x=1650, y=10)
        buttonBack.place(x=1440, y=825)
        buttonExit.place(x=1650, y=825)

    highlight()

def settingsMenu(eventObject):
    clearWindow()
    if str(rozdzielczosc.get()) == '-inna':
        withoutComputer.grid(row=0, column=0)
        withoutComputerPhoto.grid(row=0, column=1)
        withComputer.grid(row=1, column=0)
        withComputerPhoto.grid(row=1, column=1)

        combo.grid(row=2, column=0)
        gameTypeLabal.grid(row=2, column=1)
        rozdzielczosc.grid(row=3, column=0)
        rozdzielczoscLabal.grid(row=3, column=1)

        buttonBack.grid(row=4, column=0)
        buttonExit.grid(row=4, column=1)
    else:
        withoutComputer.place(x=340, y=300)
        withoutComputerPhoto.place(x=250, y=100)
        withComputer.place(x=560, y=300)
        withComputerPhoto.place(x=460, y=100)

        combo.place(x=290, y=650)
        gameTypeLabal.place(x=250, y=450)
        rozdzielczosc.place(x=500, y=650)
        rozdzielczoscLabal.place(x=460, y=450)

        buttonBack.place(x=1440, y=825)
        buttonExit.place(x=1650, y=825)
rozdzielczosc.bind('<<ComboboxSelected>>', settingsMenu)

def startMenu():
    global trwaGra
    global playerMoves, botMoves
    if trwaGra:
        result = messagebox.askquestion('Wyjście', 'Czy na pewno chcesz wyjść?')
        if result == 'yes':
            trwaGra = False
            return startMenu()
        elif result == 'no':
            return

    for x in range(0, 2):
        for w in range(0, 5):
            for k in range(0, 5):
                board[x][w][k] = False

    clearWindow()
    if str(rozdzielczosc.get()) == '-inna':
        buttonStart.grid(row=0, column=0)
        buttonSettings.grid(row=1, column=0)
        buttonExit.grid(row=2, column=0)
    else:
        buttonStart.place(x=800, y=200)
        buttonSettings.place(x=800, y=410)
        buttonExit.place(x=1650, y=825)


    botMoves = []
    playerMoves = []

    global queue
    queue = 0
    highlight()
    win.configure(image=photoTrwaGra)
    for x in field:
        x.config(state='normal', image=photoBlank)
    for x in range(0, 2):
        for i in range(0, 5):
            for k in range(0, 5):
                board[x][i][k] = False

def loadConfig():
    file = open("config.txt", "r")

    for i in range(0, len(wyniki)):
        for w in range(0, 5):
            temp = file.readline()
            for k in range(0, 5):
                wyniki[i][w][k] = bool(int(temp[k]))
            if w == 4:
                temp = file.readline()

    file.close()



# Start app
loadConfig()
startMenu()

# Open Tk
window.mainloop()