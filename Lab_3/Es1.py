from tkinter import *
from tkinter import ttk

i = 0
colors = ["red", "green", "yellow", "blue", "purple", "white"]


def colorChange():
    global i
    if i < len(colors) - 1:
        i += 1;
    else:
        i = 0
    testo["background"] = colors[i]


root = Tk()
root.title("Esercizio 1")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


testo = ttk.Label(root, text=" ", background="white", padding=(100,50))
testo.grid(column=0, row=0, sticky="n")

tasto = ttk.Button(root, text="Change color", command=colorChange)
tasto.grid(column=0, row=1, sticky="s")



root.mainloop()
