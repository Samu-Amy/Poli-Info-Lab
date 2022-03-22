from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Tris")
root.geometry("+500+200")
root.columnconfigure(0, weight=1)


counter = 0
table=[]
for i in range(3):
    table.append(["", "", ""])


def addSymbol(event):
    global  counter
    (x, y) = event.x, event.y
    tableX = 0
    tableY = 0
    xIncrement = 0
    yIncrement = 0

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
    # continua

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



    print(table)


canvas = Canvas(root, width=302, height=302)
canvas.grid(row=0, column=0, sticky="n")

canvas.create_line(101, 0, 101, 302)
canvas.create_line(202, 0, 202, 302)
canvas.create_line(0, 101, 302, 101)
canvas.create_line(0, 202, 302, 202)

canvas.bind("<Button-1>", addSymbol)


root.mainloop()