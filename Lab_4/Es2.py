from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Tris")
root.geometry("+500+200")
root.columnconfigure(0, weight=1)


# Variabili

vittoria = False
winner = ""
player1 ="Giocatore 1" #TODO: inserimento nomi giocatori, tasti reset e close, e forse menu (magari per il reset)
player2 = "Giocatore 2"

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

    if not vittoria:

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
    global vittoria
    if table[0][0] == table[1][1] == table[2][2] != "":
        vittoria = True
        winner = table[0][0]
    elif table[0][2] == table[1][1] == table[2][0] != "":
        vittoria = True
        winner = table[0][2]
    else:
        for i in range(3):
            if table[i][0] == table[i][1] == table[i][2] != "":
                vittoria = True
                winner = table[i][0]
            elif table[0][i] == table[1][i] == table[2][i] != "":
                vittoria = True
                winner = table[0][i]

    if vittoria:
        if winner == "X":
            winner = player1
        elif winner == "O":
            winner = player2

        messagebox.showinfo(title="Fine partita", message="Ha vinto " + winner)
        #TODO: crea una finestra apposta, invece di usare questa (sia per i nomi, sia per la vittoria)


# Grafica


def init():
    global canvas
    canvas = Canvas(root, width=302, height=302)
    canvas.grid(row=0, column=0, sticky="n")

    canvas.create_line(101, 0, 101, 302)
    canvas.create_line(202, 0, 202, 302)
    canvas.create_line(0, 101, 302, 101)
    canvas.create_line(0, 202, 302, 202)

    canvas.bind("<Button-1>", addSymbol)

init()

window = Toplevel(root) #TODO: Dovrebbe aprirsi sopra
window.title("Nomi")
window.geometry("+500+200")

# Inserimento nomi


root.mainloop()