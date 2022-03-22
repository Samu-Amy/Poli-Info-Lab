from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Sketchpad")
root.geometry("+500+200")
root.rowconfigure(1, weight=1)

colorVar = StringVar()
colorVar.set("black")

def addLine(event):
    (x, y) = event.x, event.y
    canvas.create_line(250, 0, x, y, fill=colorVar.get())

def setColor(color):
    colorVar.set(color)


canvas = Canvas(root, width=500, height=500)
canvas.grid(row=0, column=0)

canvas.bind("<B1-Motion>", addLine)

frame = ttk.Frame(root)
frame.grid(row=1, column=0)

for i in range(5):
    frame.columnconfigure(i, weight=1)

black = Button(frame, text=" "*10, background="black", command=lambda: setColor("black"))
black.grid(row=0, column=0, padx=15, pady=10)

red = Button(frame, text=" "*10, background="red", command=lambda: setColor("red"))
red.grid(row=0, column=1, padx=15, pady=10)

blue = Button(frame, text=" "*10, background="blue", command=lambda: setColor("blue"))
blue.grid(row=0, column=2, padx=15, pady=10)

green = Button(frame, text=" "*10, background="green", command=lambda: setColor("green"))
green.grid(row=0, column=3, padx=15, pady=10)

orange = Button(frame, text=" "*10, background="orange", command=lambda: setColor("orange"))
orange.grid(row=0, column=4, padx=15, pady=10)


root.mainloop()