from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Tris")
root.geometry("+500+200")
root.lift()
root.columnconfigure(0, weight=1)


# Variabili

win = False
winner = ""

temp1 = StringVar()
temp2 = StringVar()
temp1.set("")
temp2.set("")

player1 = StringVar()
player2 = StringVar()

player1.set("Giocatore 1")
player2.set("Giocatore 2")

article = ""

counter = 0
table=[]
for i in range(3):
    table.append(["", "", ""])


# Funzioni

def addSymbol(event):
    global  counter
    (x, y) = event.x, event.y
    tableX = 0
    tableY = 0
    xIncrement = 0
    yIncrement = 0

    if not win:

        if 0<=x<101:
            if 0<=y<101:  # Prima sezione
                xIncrement = 0
                yIncrement = 0
                tableX = 0
                tableY = 0
            elif 101<y<202:  # Seconda sezione
                xIncrement = 0
                yIncrement = 101
                tableX = 1
                tableY = 0
            elif 202<y<302: # Terza sezione
                xIncrement = 0
                yIncrement = 202
                tableX = 2
                tableY = 0
        elif 101<x<202:
            if 0<=y<101:  # Quarta sezione
                xIncrement = 101
                yIncrement = 0
                tableX = 0
                tableY = 1
            elif 101<y<202:  # Quinta sezione
                xIncrement = 101
                yIncrement = 101
                tableX = 1
                tableY = 1
            elif 202<y<302: # Sesta sezione
                xIncrement = 101
                yIncrement = 202
                tableX = 2
                tableY = 1
        elif 202<x<302:
            if 0<=y<101:  # Settima sezione
                xIncrement = 202
                yIncrement = 0
                tableX = 0
                tableY = 2
            elif 101<y<202:  # Ottava sezione
                xIncrement = 202
                yIncrement = 101
                tableX = 1
                tableY = 2
            elif 202<y<302: # Nona sezione
                xIncrement = 202
                yIncrement = 202
                tableX = 2
                tableY = 2


        if counter%2 == 0: # Primo giocatore
            if table[tableY][tableX] == "":
                table[tableY][tableX] = "X"
                canvas.create_line(20+xIncrement, 20+yIncrement, 80+xIncrement, 80+yIncrement)
                canvas.create_line(20+xIncrement, 80+yIncrement, 80+xIncrement, 20+yIncrement)
                counter += 1
        else:              # Secondo giocatore
            if table[tableY][tableX] == "":
                table[tableY][tableX] = "O"
                canvas.create_oval(20+xIncrement, 20+yIncrement, 80+xIncrement, 80+yIncrement)
                counter += 1

        checkWin()


def checkWin():
    global win
    global article
    if table[0][0] == table[1][1] == table[2][2] != "":
        win = True
        winner = table[0][0]
    elif table[0][2] == table[1][1] == table[2][0] != "":
        win = True
        winner = table[0][2]
    else:
        for i in range(3):
            if table[i][0] == table[i][1] == table[i][2] != "":
                win = True
                winner = table[i][0]
            elif table[0][i] == table[1][i] == table[2][i] != "":
                win = True
                winner = table[0][i]

    if win:
        if winner == "X":
            winner = player1.get()

        elif winner == "O":
            winner = player2.get()

        if winner == "Giocatore 1" or winner == "Giocatore 2":
            article = "il "

        print("Ha vinto " + article + winner)

        message("Ha vinto " + article + winner)


    # Creazione finestra vincitore

def message(mex):
    winnerWindow = Toplevel()
    winnerWindow.title("Fine partita")
    winnerWindow.geometry("+500+200")
    winnerWindow.lift(root)
    window.focus()

    for i in range(2):
        winnerWindow.rowconfigure(i, weight=1)
    for i in range(2):
        winnerWindow.columnconfigure(i, weight=1)

    text = ttk.Label(winnerWindow, text=mex)
    text.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=20)

    retryB = ttk.Button(winnerWindow, text="Retry")
    retryB.grid(row=1, column=0)

    closeB = ttk.Button(winnerWindow, text="Close", command=lambda: close(root))
    closeB.grid(row=1, column=1)


def submitFunct():
    if temp1.get() != "":
        player1.set(temp1.get())

    if temp2.get() != "":
        player2.set(temp2.get())

    close(window)


def close(win):
    win.destroy()


# Grafica

global canvas
canvas = Canvas(root, width=302, height=302)
canvas.grid(row=0, column=0, sticky="n")

canvas.create_line(101, 0, 101, 302)
canvas.create_line(202, 0, 202, 302)
canvas.create_line(0, 101, 302, 101)
canvas.create_line(0, 202, 302, 202)

canvas.bind("<Button-1>", addSymbol)


# Inserimento nomi

window = Toplevel()
window.title("Inserire i nomi")
window.geometry("+500+200")
window.lift(root)

for i in range(3):
    window.rowconfigure(i, weight=1)
for i in range(2):
    window.columnconfigure(i, weight=1)


frame1 = ttk.Frame(window)
frame1.grid(row=0, column=0, rowspan=2, sticky="ne", padx=10, pady=(20, 10))

text1 = ttk.Label(frame1, text="Nome primo giocatore:")
text1.grid(row=0, column=0, sticky="nw", pady=(10, 20))
input1 = ttk.Entry(frame1, textvariable=temp1)
input1.grid(row=1, column=0, sticky="nw")


frame2 = ttk.Frame(window)
frame2.grid(row=0, column=1, rowspan=3, sticky="nw", padx=10, pady=(20, 10))

text2 = ttk.Label(frame2, text="Nome secondo giocatore:")
text2.grid(row=0, column=0, sticky="nw", pady=(10, 20))
input2 = ttk.Entry(frame2, textvariable=temp2)
input2.grid(row=1, column=0, sticky="nw")

submitB = ttk.Button(frame2, text="Submit", command=submitFunct)
submitB.grid(row=2, column=0, sticky="se", pady=(40, 0))


root.mainloop()
