from tkinter import *
from tkinter import ttk
from operator import itemgetter

# PARTE GRAFICA

root = Tk()
root.title("Punteggi")
root.geometry("+800+250")

for i in range(1, 2):
    root.rowconfigure(i, weight=1)
for i in range(2):
    root.columnconfigure(i, weight=1)

# PARTE DI ALGORITMO

# Variabili

playersList = {}

errorMessage = StringVar()
playerVar = StringVar()
scoreVar = StringVar()
bestPlayers = [""] * 3
bestScores = [""] * 3
bestPlayersVar = StringVar(value=bestPlayers)
bestScoresVar = StringVar(value=bestScores)


# Inserimento dati

def submit(event):
    player = playerVar.get()
    score = scoreVar.get()

    playerClear = player.strip().replace(" ", "")

    if playerClear.isalpha():
        try:
            playersList[player.strip()] = float(score)
            errorMessage.set("")
            playerVar.set("")
            scoreVar.set("")

            bestPlayersList = sorted(playersList.items(), key=lambda item: item[1], reverse=True)

            # Creo le liste con i valori
            if len(bestPlayersList) <= 3:
                for index in range(len(bestPlayersList)):
                    bestPlayers[index] = bestPlayersList[index][0]
                    bestScores[index] = bestPlayersList[index][1]
                    bestPlayersVar.set(bestPlayers)
                    bestScoresVar.set(bestScores)
            else:
                for index in range(3):
                    bestPlayers[index] = bestPlayersList[index][0]
                    bestScores[index] = bestPlayersList[index][1]
                    bestPlayersVar.set(bestPlayers)
                    bestScoresVar.set(bestScores)


        except ValueError:
            errorMessage.set("Punteggio non valido")

    elif player == "":
        errorMessage.set("Inserire i dati")

    else:
        errorMessage.set("Nome non valido")


# PARTE GRAFICA

# Primo frame

bestPlayersNameFrame = ttk.Frame(root)
bestPlayersNameFrame.grid(row=0, column=0, sticky="ne", padx=10, pady=(20, 40))

bestPlayersScoreFrame = ttk.Frame(root)
bestPlayersScoreFrame.grid(row=0, column=1, sticky="nw", padx=10, pady=(20, 40))

# Frame nomi

bestPlayersName = ttk.Label(bestPlayersNameFrame, text="Migliori giocatori:")
bestPlayersName.grid(row=0, column=0, sticky="nw")

bestPlayersNameList = Listbox(bestPlayersNameFrame, listvariable=bestPlayersVar, height=3)
bestPlayersNameList.grid(row=1, column=0, sticky="nw")

# Frame punteggi

bestPlayersName = ttk.Label(bestPlayersScoreFrame, text="Migliori punteggi:")
bestPlayersName.grid(row=0, column=0, sticky="nw")

bestPlayersScoreList = Listbox(bestPlayersScoreFrame, listvariable=bestScoresVar, height=3)
bestPlayersScoreList.grid(row=1, column=0, sticky="nw")

# Secondo frame

inputNameFrame = ttk.Frame(root)
inputNameFrame.grid(row=1, column=0, sticky="se", padx=10, pady=(0, 20))

inputScoreFrame = ttk.Frame(root)
inputScoreFrame.grid(row=1, column=1, sticky="sw", padx=10, pady=(0, 20))

# Frame input nomi

bestPlayersName = ttk.Label(inputNameFrame, text="Inserisci giocatore:")
bestPlayersName.grid(row=0, column=0, sticky="nw")

bestPlayersNameList = Entry(inputNameFrame, textvariable=playerVar)
bestPlayersNameList.grid(row=1, column=0, sticky="nw")

# Frame input punteggi

bestPlayersName = ttk.Label(inputScoreFrame, text="Inserisci punteggio:")
bestPlayersName.grid(row=0, column=0, sticky="nw")

bestPlayersScoreList = Entry(inputScoreFrame, textvariable=scoreVar)
bestPlayersScoreList.grid(row=1, column=0, sticky="nw")

# Terza riga

errorMessageLabel = ttk.Label(root, textvariable=errorMessage)
errorMessageLabel.grid(row=2, column=0, sticky="sw", padx=10, pady=(0, 20))

enterButton = ttk.Button(root, text="Insert", command=lambda: submit(""))
enterButton.grid(row=2, column=1, sticky="se", padx=10, pady=(0, 20))

root.bind("<Return>", submit)

root.mainloop()
