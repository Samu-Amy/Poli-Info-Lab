from tkinter import *
from tkinter import ttk


def colorChange(color):
    testo["background"] = color


root = Tk()
root.title("Esercizio 2")
root.geometry("+500+200")
root.rowconfigure(0, weight=1)
for i in range(3):
    root.columnconfigure(i, weight=1)


testo = ttk.Label(root, text=" ", background="white", padding=(100, 50))
testo.grid(column=0, row=0, columnspan=3, sticky="n", padx=(25, 25), pady=(25, 20))

rosso = Button(root, text=" "*10, bg="red", command=lambda: colorChange("red"))
rosso.grid(column=0, row=1, sticky="s", pady=(20, 25))

blu = Button(root, text=" "*10, bg="blue", command=lambda: colorChange("blue"))
blu.grid(column=1, row=1, sticky="s", pady=(20, 25))

verde = Button(root, text=" "*10, bg="green", command=lambda: colorChange("green"))
verde.grid(column=2, row=1, sticky="s", pady=(20, 25))


root.mainloop()
