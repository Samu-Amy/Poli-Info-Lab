from university import *
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("University")

# Comandi:
# set/get nome, set/get rector, add/get student, add/get course, register, get student/course

# Variabili
title = StringVar()


# Funzioni
def submit_title():
    uni = University(str(title))
    window.destroy()


# Grafica

# - Finestra iniziale
window = Toplevel(root)
window.title("Insert name")

frame = ttk.Frame(window)
frame.grid(row=0, column=0, padx=20, pady=20)

text = ttk.Label(frame, text="Insert university name:")
text.grid(row=0, column=0)

textEntry = ttk.Entry(frame, textvariable=title)
textEntry.grid(row=0, column=1, padx=(20, 0))
textEntry.focus_set()

button = ttk.Button(frame, text="Set name", command=submit_title)
button.grid(row=1, column=1, pady=(20, 0))


# - Finestra principale
frameMain = ttk.Frame(root)
frameMain.grid(row=0, column=0, padx=20, pady=20)

name = ttk.Label(root, textvariable=title, anchor="center", font=(", 14"))
name.grid(row=0, column=0)


window.attributes('-topmost',True)


root.mainloop()
