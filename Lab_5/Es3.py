import gc
from tkinter import *
from tkinter import ttk
from random import randint

root = Tk()
root.title("Asteroid")
root.geometry("+500+200")
root.columnconfigure(0, weight=1)

# Variabili

end = False
score = 0
scoreVar = StringVar()
scoreVar.set("Score: " + str(score))
errorMessageVar = StringVar()
list = []


# Grafica


scoreText = ttk.Label(root, textvariable=scoreVar, font=("", 16))
scoreText.grid(row=0, column=0)


canvas = Canvas(root, width=300, height=300, background="#0d1a51")
canvas.grid(row=1, column=0)

player = canvas.create_polygon(150, 150, 160, 180, 140, 180, 150, 150, outline="white", fill="#0d1a51")


# Funzioni e classi

def movePlayer(event, direction):
    if not end:
        coord = canvas.coords(player)
        if direction == "up" and coord[1] > 8:
            canvas.move(player, 0, -8)
        elif direction == "right" and coord[2] < 296:
            canvas.move(player, 8, 0)
        elif direction == "left" and coord[4] > 4:
            canvas.move(player, -8, 0)
        elif direction == "down" and coord[3] < 292:
            canvas.move(player, 0, 8)


class Meteor:
    id = 0 #TODO: rimuovi

    def __init__(self):
        Meteor.id += 1 #TODO: rimuovi
        self.passed = False
        self.size = randint(25, 50)
        self.xCoord = randint(0 + self.size, 300 - self.size)
        self.spawnObject()
        self.collision()
        self.scoreUpdate(self.meteor)

    def getObject(self):
        return self.meteor

    def spawnObject(self):
        self.size = randint(25, 50)
        self.xCoord = randint(0 + self.size, 300 - self.size)
        self.meteor = canvas.create_oval(self.xCoord, 0, self.xCoord + self.size, self.size, outline="white")
        self.moveObject(self.meteor)

    def cleanUp(self):
        if self.passed:
            del self
            gc.collect()

    def moveObject(self, meteor):
        canvas.move(meteor, 0, 5)
        canvas.after(50, lambda: self.moveObject(meteor))

    def collision(self):
        global end
        coord = canvas.coords(player)
        if not end:
            if canvas.find_overlapping(coord[0], coord[1], coord[2], coord[3]) != (1, ) or canvas.find_overlapping(coord[2], coord[3], coord[4], coord[5]) != (1,) or canvas.find_overlapping(coord[4], coord[5], coord[0], coord[1]) != (1, ):
                end = True
                canvas.delete("all")
                endRound()
        canvas.after(1, self.collision)

    def scoreUpdate(self, meteor):
        global score
        if not end:
            if canvas.coords(meteor)[1] >= 300 and not self.passed:
                score += 1
                scoreVar.set("Score: " + str(score))
                self.passed = True
            canvas.after(200, lambda: self.scoreUpdate(self.meteor))

    def __del__(self):
        print("Rimosso") #TODO: rimuovi


def spawn():
    if not end:
        temp = Meteor()
        list.append(temp)
        root.after(800, spawn)
    else:
        for object in list:
            del object

def remove():
    i = 0
    if not end:
        while i < len(list):
            object = list[i]
            if object.passed:
                object.destroy()
                list.remove(object) # NON FUNZIONA (distrugge gli oggetti solo alla fine)
                del object
                i = 0
                print(list) #TODO: rimuovi
                print(Meteor.id) #TODO: rimuovi
            else:
                i += 1

    root.after(50, remove)

def endRound():
    window = Toplevel()
    window.title("Game over")
    window.geometry("200x200+550+300")
    window.focus()
    window.columnconfigure(0, weight=1)

    scoreVar.set("Your score is: " + str(score))
    message = ttk.Label(window, textvariable=scoreVar)
    message.grid(row=0, column=0, padx=20, pady=20)

    resetButton = ttk.Button(window, text="Reset", command=lambda: reset(window))
    resetButton.grid(row=1, column=0, padx=20, pady=20)

    errorMessage = ttk.Label(window, textvariable=errorMessageVar)
    errorMessage.grid(row=2, column=0)

def reset(window): #NON FUNZIONA
    global end, player
    try:
        window.destroy()
        end = False
        player = canvas.create_polygon(150, 150, 160, 180, 140, 180, 150, 150, outline="white", fill="#0d1a51")
        spawn()
        remove()
    except:
        errorMessageVar.set("Errore")

spawn()
remove()


root.bind("<Up>", lambda event: movePlayer(event, "up"))
root.bind("<Right>", lambda event: movePlayer(event, "right"))
root.bind("<Left>", lambda event: movePlayer(event, "left"))
root.bind("<Down>", lambda event: movePlayer(event, "down"))


root.mainloop()
