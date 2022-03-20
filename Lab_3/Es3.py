from tkinter import *
from tkinter import ttk

fullText=[]

inFile=open("sabato.txt", "r", encoding="UTF-8")
for line in inFile:
    fullText.append(line)

# Titolo del testo

title = fullText[0][0].upper() + fullText[0][1:].lower()

#

if fullText[1].strip() == "":
    fullText.pop(1)

fullText.pop(0)


root = Tk()
root.title(title)
root.geometry("+500+200")

fullTextVar = StringVar(value=fullText)

textDisplay = Listbox(root, listvariable=fullTextVar, width=50, height=25)
textDisplay.pack(side=LEFT, fill=BOTH)

scrollBar = ttk.Scrollbar(root, orient="vertical", command=textDisplay.yview)
scrollBar.pack(side=RIGHT, fill=Y)

textDisplay["yscrollcommand"] = scrollBar.set


root.mainloop()
