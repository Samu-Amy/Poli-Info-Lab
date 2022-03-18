from tkinter import *
from tkinter import ttk

fullText=[]

inFile=open("sabato.txt", "r")
for line in inFile:
    fullText.append(line)


root = Tk()
root.title("Il sabato del villaggio") # Upgrade: prendilo dal file
root.geometry("+500+200")

fullTextVar = StringVar(value=fullText)

textDisplay = Listbox(root, listvariable=fullTextVar, width=50, height=25)
textDisplay.pack(side=LEFT, fill=BOTH)

scrollBar = ttk.Scrollbar(root, orient="vertical", command=textDisplay.yview)
scrollBar.pack(side=RIGHT, fill=Y)

textDisplay["yscrollcommand"] = scrollBar.set


root.mainloop()
