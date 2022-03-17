from tkinter import *
from tkinter import ttk


def colorChange(color):
    testo["background"] = color


root = Tk()
root.title("Esercizio 1")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


testo = ttk.Label(root, text=" ", background="white", padding=(100,50))
testo.grid(column=0, row=0, columnspan=3, sticky="n")

rosso = Button(root, text=" "*10, bg="red", command=colorChange("red"))
rosso.grid(column=0, row=1, anchor="padx")

blu = Button(root, text=" "*10, bg="blue", command=colorChange("blue"))
blu.grid(column=1, row=1, anchor="padx")

verde = Button(root, text=" "*10, bg="green", command=colorChange("green"))
verde.grid(column=2, row=1, anchor="padx")



root.mainloop()