from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Punteggi")
root.geometry("300x350+800+250")

for i in range(1, 2):
    root.rowconfigure(i, weight=1)
for i in range(2):
    root.columnconfigure(i, weight=1)


# Variabili

errorMessage = StringVar()


# Algoritmo




# Primo frame

bestPlayersNameFrame = ttk.Frame(root)
bestPlayersNameFrame.grid(row=0, column=0, sticky="ne", padx=10, pady=(20, 0))

bestPlayersScoreFrame = ttk.Frame(root)
bestPlayersScoreFrame.grid(row=0, column=1, sticky="nw", padx=10, pady=(20, 0))


# Frame nomi

bestPlayersName = ttk.Label(bestPlayersNameFrame, text="Migliori giocatori:")
bestPlayersName.grid(row=0, column=0, sticky="nw")

bestPlayersNameList = Listbox(bestPlayersNameFrame)
bestPlayersNameList.grid(row=1, column=0, sticky="nw")


# Frame punteggi

bestPlayersName = ttk.Label(bestPlayersScoreFrame, text="Migliori punteggi:")
bestPlayersName.grid(row=0, column=0, sticky="nw")

bestPlayersScoreList = Listbox(bestPlayersScoreFrame)
bestPlayersScoreList.grid(row=1, column=0, sticky="nw")


# Secondo frame

inputNameFrame = ttk.Frame(root)
inputNameFrame.grid(row=1, column=0, sticky="se", padx=10, pady=(0, 20))

inputScoreFrame = ttk.Frame(root)
inputScoreFrame.grid(row=1, column=1, sticky="sw", padx=10, pady=(0, 20))


# Frame input nomi

bestPlayersName = ttk.Label(inputNameFrame, text="Inserisci giocatore:")
bestPlayersName.grid(row=0, column=0, sticky="nw")

bestPlayersNameList = Entry(inputNameFrame)
bestPlayersNameList.grid(row=1, column=0, sticky="nw")


# Frame input punteggi

bestPlayersName = ttk.Label(inputScoreFrame, text="Inserisci punteggio:")
bestPlayersName.grid(row=0, column=0, sticky="nw")

bestPlayersScoreList = Entry(inputScoreFrame)
bestPlayersScoreList.grid(row=1, column=0, sticky="nw")


# Terza riga

errorMessageLabel = ttk.Label(root, textvariable=errorMessage)
errorMessageLabel.grid(row=2, column=0, sticky="sw", padx=10, pady=(0, 20))

enterButton = ttk.Button(root, text="Insert")
enterButton.grid(row=2, column=1, sticky="se", padx=10, pady=(0, 20))


root.mainloop()
