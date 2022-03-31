import time
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
scoreVar.set(str(score))


# Grafica

scoreFrame = ttk.Frame(root)
scoreFrame.grid(row=0, column=0, pady=10)

text = ttk.Label(scoreFrame, text="Score:", font=("", 16))
text.grid(row=0, column=0, padx=(0, 20))

scoreText = ttk.Label(scoreFrame, textvariable=scoreVar, font=("", 16))
scoreText.grid(row=0, column=1)


canvas = Canvas(root, width=300, height=300, background="#0d1a51")
canvas.grid(row=1, column=0)

player = canvas.create_polygon(150, 150, 160, 180, 140, 180, 150, 150, outline="white", fill="#0d1a51")


# Funzioni

def movePlayer(event, direction):
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

    def __init__(self):
        self.size = randint(25, 50)
        self.xCoord = randint(0 + self.size, 300 - self.size)
        self.spawnObject()
        self.collision()
        canvas.after(1, self.collision)

    def spawnObject(self):
        self.size = randint(25, 50)
        self.xCoord = randint(0 + self.size, 300 - self.size)
        self.meteor = canvas.create_oval(self.xCoord, 0, self.xCoord + self.size, self.size, outline="white")
        self.moveObject(self.meteor)

    def moveObject(self, meteor):
        canvas.move(meteor, 0, 5)
        canvas.after(50, lambda: self.moveObject(meteor))

    def collision(self):
        global end
        coord = canvas.coords(player)
        if canvas.find_overlapping(coord[0], coord[1], coord[2], coord[3]) != (1, ):
            end = True
            print("Fine")

def spawn():
    if not end:
        Meteor()
        root.after(800, spawn)

spawn()


root.bind("<Up>", lambda event: movePlayer(event, "up"))
root.bind("<Right>", lambda event: movePlayer(event, "right"))
root.bind("<Left>", lambda event: movePlayer(event, "left"))
root.bind("<Down>", lambda event: movePlayer(event, "down"))


root.mainloop()
