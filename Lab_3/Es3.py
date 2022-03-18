from tkinter import *
from tkinter import ttk

fullText=[]

inFile=open("sabato.txt", "r")
for line in inFile:
    fullText.append(line)


root = Tk()
root.title("Il sabato del villaggio") # Upgrade: prendilo dal file
root.geometry("+500+200")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

textDisplay = Text(root, state="")
textDisplay.grid(row=0, column=0)

for index in range(len(fullText)):
    textDisplay.insert(str(index) + ".0", fullText[index])

scrollBar = ttk.Scrollbar(root, orient="vertical", command=textDisplay.yview)
scrollBar.grid(row=0, column=1)


root.mainloop()
